# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_execute_mail_merge.py">
#   Copyright (c) 2026 Aspose.Words for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import os
import dateutil.parser
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext

#
# Example of how to perform mail merge.
#
class TestExecuteMailMerge(BaseTestContext):
    #
    # Test for executing mail merge online.
    #
    def test_execute_mail_merge_online(self):
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'SampleExecuteTemplate.docx'
        local_data_file = 'SampleExecuteTemplateData.txt'

        request_template = open(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb')
        request_data = open(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_data_file), 'rb')
        request = asposewordscloud.models.requests.ExecuteMailMergeOnlineRequest(template=request_template, data=request_data, with_regions=True)

        result = self.words_api.execute_mail_merge_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for executing mail merge online job.
    #
    def test_execute_mail_merge_online_job(self):
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'SampleExecuteTemplate.docx'
        local_data_file = 'SampleExecuteTemplateData.txt'

        request_template = open(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb')
        request_data = open(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_data_file), 'rb')
        request = asposewordscloud.models.requests.ExecuteMailMergeOnlineJobRequest(template=request_template, data=request_data, with_regions=True)

        job_handler = self.words_api.execute_mail_merge_online_job(request)
        self.assertIsNotNone(job_handler, 'Error has occurred.')


    #
    # Test for executing mail merge.
    #
    def test_execute_mail_merge(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/MailMerge'
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'SampleExecuteTemplate.docx'
        remote_file_name = 'TestExecuteMailMerge.docx'
        local_data_file = open(os.path.join(self.local_test_folder, mail_merge_folder + '/SampleMailMergeTemplateData.txt')).read()

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb'))

        request = asposewordscloud.models.requests.ExecuteMailMergeRequest(name=remote_file_name, data=local_data_file, folder=remote_data_folder, with_regions=True, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.execute_mail_merge(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate ExecuteMailMerge response')
        self.assertEqual('TestExecuteMailMerge.docx', result.document.file_name)

    #
    # Test for executing mail merge job.
    #
    def test_execute_mail_merge_job(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/MailMerge'
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'SampleExecuteTemplate.docx'
        remote_file_name = 'TestExecuteMailMerge.docx'
        local_data_file = open(os.path.join(self.local_test_folder, mail_merge_folder + '/SampleMailMergeTemplateData.txt')).read()

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb'))

        request = asposewordscloud.models.requests.ExecuteMailMergeJobRequest(name=remote_file_name, data=local_data_file, folder=remote_data_folder, with_regions=True, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        job_handler = self.words_api.execute_mail_merge_job(request)
        self.assertIsNotNone(job_handler, 'Error has occurred.')
        result = job_handler.wait_result(3)
        self.assertIsNotNone(result.document, 'Validate ExecuteMailMergeJob response')
        self.assertEqual('TestExecuteMailMerge.docx', result.document.file_name)
