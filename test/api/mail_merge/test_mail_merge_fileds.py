# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_mail_merge_fileds.py">
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
# Example of how to work with merge fields.
#
class TestMailMergeFileds(BaseTestContext):
    #
    # Test for putting new fields.
    #
    def test_get_document_field_names_online(self):
        mail_merge_folder = 'DocumentActions/MailMerge'
        local_document_file = 'SampleExecuteTemplate.docx'

        request_template = self.open_file(os.path.join(self.local_test_folder, mail_merge_folder + '/' + local_document_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentFieldNamesOnlineRequest(template=request_template, use_non_merge_fields=True)

        result = self.words_api.get_document_field_names_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field_names, 'Validate GetDocumentFieldNamesOnline response')
        self.assertIsNotNone(result.field_names.names, 'Validate GetDocumentFieldNamesOnline response')
        self.assertEqual(15, len(result.field_names.names))
        self.assertEqual('TableStart:Order', result.field_names.names[0])

    #
    # Test for getting mailmerge fields.
    #
    def test_get_document_field_names(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/MailMerge'
        remote_file_name = 'TestGetDocumentFieldNames.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, 'Common/test_multi_pages.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentFieldNamesRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_document_field_names(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field_names, 'Validate GetDocumentFieldNames response')
        self.assertIsNotNone(result.field_names.names, 'Validate GetDocumentFieldNames response')
        self.assertEqual(0, len(result.field_names.names))
