# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_execute_template_with_field_options.py">
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
# Example of how to perform template execution.
#
class TestExecuteTemplateWithFieldOptions(BaseTestContext):
    #
    # Test for posting execute template.
    #
    def test_execute_template_with_field_options(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/MailMerge'
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'TestMailMergeWithOptions.docx'
        remote_file_name = 'TestMailMergeWithOptions.docx'
        local_data_file = open(os.path.join(self.local_test_folder, mail_merge_folder + '/TestMailMergeData.xml')).read()

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb'))

        request_options_current_user = asposewordscloud.UserInformation(name='SdkTestUser')
        request_options = asposewordscloud.FieldOptions(current_user=request_options_current_user)
        request = asposewordscloud.models.requests.ExecuteMailMergeRequest(name=remote_file_name, data=local_data_file, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name, options=request_options)

        result = self.words_api.execute_mail_merge(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate ExecuteTemplateWithFieldOptions response')
        self.assertEqual('TestMailMergeWithOptions.docx', result.document.file_name)

    #
    # Test for execute template online.
    #
    def test_execute_template_online_with_field_options(self):
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'TestMailMergeWithOptions.docx'
        local_data_file = 'TestMailMergeData.xml'

        request_template = self.open_file(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb')
        request_data = self.open_file(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_data_file), 'rb')
        request_options_current_user = asposewordscloud.UserInformation(name='SdkTestUser')
        request_options = asposewordscloud.FieldOptions(current_user=request_options_current_user)
        request = asposewordscloud.models.requests.ExecuteMailMergeOnlineRequest(template=request_template, data=request_data, options=request_options)

        result = self.words_api.execute_mail_merge_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

