# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_hyperlink.py">
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
# Example of how to work with hyperlinks.
#
class TestHyperlink(BaseTestContext):
    #
    # Test for getting hyperlink by specified index.
    #
    def test_get_document_hyperlink_by_index(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Hyperlink'
        local_file = 'Common/test_doc.docx'
        remote_file_name = 'TestGetDocumentHyperlinkByIndex.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexRequest(name=remote_file_name, hyperlink_index=0, folder=remote_data_folder)

        result = self.words_api.get_document_hyperlink_by_index(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.hyperlink, 'Validate GetDocumentHyperlinkByIndex response')
        self.assertEqual('Aspose', result.hyperlink.display_text)

    #
    # Test for getting hyperlink by specified index online.
    #
    def test_get_document_hyperlink_by_index_online(self):
        local_file = 'Common/test_doc.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentHyperlinkByIndexOnlineRequest(document=request_document, hyperlink_index=0)

        result = self.words_api.get_document_hyperlink_by_index_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting hyperlinks.
    #
    def test_get_document_hyperlinks(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Hyperlink'
        local_file = 'Common/test_doc.docx'
        remote_file_name = 'TestGetDocumentHyperlinks.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentHyperlinksRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_document_hyperlinks(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.hyperlinks, 'Validate GetDocumentHyperlinks response')
        self.assertIsNotNone(result.hyperlinks.hyperlink_list, 'Validate GetDocumentHyperlinks response')
        self.assertEqual(2, len(result.hyperlinks.hyperlink_list))
        self.assertEqual('Aspose', result.hyperlinks.hyperlink_list[0].display_text)

    #
    # Test for getting hyperlinks online.
    #
    def test_get_document_hyperlinks_online(self):
        local_file = 'Common/test_doc.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentHyperlinksOnlineRequest(document=request_document)

        result = self.words_api.get_document_hyperlinks_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

