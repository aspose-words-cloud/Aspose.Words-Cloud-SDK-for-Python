properties([
	gitLabConnection('gitlab'),
	[$class: 'ParametersDefinitionProperty', 
		parameterDefinitions: [
			[$class: 'StringParameterDefinition', name: 'branch', defaultValue: 'master', description: 'the branch to build'],
			[$class: 'StringParameterDefinition', name: 'apiUrl', defaultValue: 'https://api-qa.aspose.cloud', description: 'api url'],
            [$class: 'BooleanParameterDefinition', name: 'ignoreCiSkip', defaultValue: false, description: 'ignore CI Skip'],
            [$class: 'StringParameterDefinition', name: 'credentialsId', defaultValue: '6839cbe8-39fa-40c0-86ce-90706f0bae5d', description: 'credentials id'],
            [$class: 'BooleanParameterDefinition', name: 'packageTesting', defaultValue: false, description: 'Testing package from repository without local sources. Used for prodhealthcheck'],
		]
	]
])

def runtests(dockerImageVersion)
{
    def needToBuild = false

    dir(dockerImageVersion){
        try {
            stage('checkout'){
				checkout([$class: 'GitSCM', branches: [[name: params.branch]], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'LocalBranch', localBranch: "**"]], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '361885ba-9425-4230-950e-0af201d90547', url: 'https://git.auckland.dynabic.com/words-cloud/words-cloud-python.git']]])
                
                sh 'git show -s HEAD > gitMessage'
                def commitMessage = readFile('gitMessage').trim()
                echo commitMessage
                needToBuild = params.ignoreCiSkip || !commitMessage.contains('[ci skip]')               
                sh 'git clean -fdx'
                
                if (needToBuild) {
                    withCredentials([usernamePassword(credentialsId: params.credentialsId, passwordVariable: 'ClientSecret', usernameVariable: 'ClientId')]) {
                        sh 'mkdir -p Settings'
                        sh 'echo "{\\"ClientId\\": \\"$ClientId\\",\\"ClientSecret\\": \\"$ClientSecret\\", \\"BaseUrl\\": \\"$apiUrl\\"}" > Settings/servercreds.json'
                    }
                }
            }
            
            if (needToBuild) {
                // Root is needed so pip can write to the image's own site-packages, but it leaves
                // root-owned files in the mounted workspace that cleanWs() cannot delete. Capture the
                // agent's ids here and hand ownership back before leaving the container.
                def agentUid = sh(script: 'id -u', returnStdout: true).trim()
                def agentGid = sh(script: 'id -g', returnStdout: true).trim()
                docker.image('python:' + dockerImageVersion).inside('-u root'){
                    try {
                 if (params.packageTesting) {
                            sh "rm -rf asposewordscloud"
                            sh "mv requirements-test.txt requirements.txt"
                    }
                    stage('build'){
                        sh "python -m pip install -r requirements.txt && python -m pip install -r test-requirements.txt"
                    }
                
                    stage('tests'){
                        try {
                            sh "python -m xmlrunner discover -v -s --output-file testReport.xml ."
                        } 
                        finally {
                            junit '**\\testReport.xml'
                        }
                    }
                
                    stage('bdd-tests'){
                        
                    }
                    
                    stage('clean-compiled'){
                        sh "rm -rf %s"
                    }
                    } finally {
                        sh "chown -R ${agentUid}:${agentGid} ."
                    }
                } 
            }
        } finally {
			 cleanWs()
        }
    }
}

node('words-linux') {
	stage('oldpy'){
		try {
			runtests("3.8") 
		} finally {
			cleanWs()
		}
	}
    
    stage('newpy'){
		try {
			runtests("3.13") 
		} finally {
			cleanWs()
		}
	}
}
