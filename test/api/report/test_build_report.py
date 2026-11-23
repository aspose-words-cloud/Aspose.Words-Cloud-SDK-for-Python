# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_build_report.py">
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
class TestBuildReport(BaseTestContext):
    #
    # Test for build report online.
    #
    def test_build_report_online(self):
        reporting_folder = 'DocumentActions/Reporting'
        local_document_file = 'ReportTemplate.docx'
        local_data_file = open(os.path.join(self.local_test_folder, reporting_folder + '/ReportData.json')).read()

        request_template = self.open_file(os.path.join(self.local_test_folder, reporting_folder + '/' + local_document_file), 'rb')
        request_report_engine_settings = asposewordscloud.ReportEngineSettings(data_source_type='Json', data_source_name='persons')
        request = asposewordscloud.models.requests.BuildReportOnlineRequest(template=request_template, data=local_data_file, report_engine_settings=request_report_engine_settings)

        result = self.words_api.build_report_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for build report.
    #
    def test_build_report(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Reporting'
        reporting_folder = 'DocumentActions/Reporting'
        local_document_file = 'ReportTemplate.docx'
        remote_file_name = 'TestBuildReport.docx'
        local_data_file = open(os.path.join(self.local_test_folder, reporting_folder + '/ReportData.json')).read()

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, reporting_folder + '/' + local_document_file), 'rb'))

        request_report_engine_settings_report_build_options = ['AllowMissingMembers', 'RemoveEmptyParagraphs']
        request_report_engine_settings = asposewordscloud.ReportEngineSettings(data_source_type='Json', report_build_options=request_report_engine_settings_report_build_options)
        request = asposewordscloud.models.requests.BuildReportRequest(name=remote_file_name, data=local_data_file, report_engine_settings=request_report_engine_settings, folder=remote_data_folder)

        result = self.words_api.build_report(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate BuildReport response')
        self.assertEqual('TestBuildReport.docx', result.document.file_name)
