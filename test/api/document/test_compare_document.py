# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_compare_document.py">
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
# Example of document comparison.
#
class TestCompareDocument(BaseTestContext):
    #
    # Test for document comparison.
    #
    def test_compare_document(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/CompareDocument'
        local_folder = 'DocumentActions/CompareDocument'
        local_name1 = 'compareTestDoc1.doc'
        local_name2 = 'compareTestDoc2.doc'
        remote_name1 = 'TestCompareDocument1.doc'
        remote_name2 = 'TestCompareDocument2.doc'

        self.upload_file(remote_folder + '/' + remote_name1, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name1), 'rb'))
        self.upload_file(remote_folder + '/' + remote_name2, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name2), 'rb'))

        request_compare_data_file_reference = asposewordscloud.FileReference.fromRemoteFilePath(remote_folder + '/' + remote_name2)
        request_compare_data = asposewordscloud.CompareData(author='author', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'), file_reference=request_compare_data_file_reference)
        request = asposewordscloud.models.requests.CompareDocumentRequest(name=remote_name1, compare_data=request_compare_data, folder=remote_folder, dest_file_name=self.remote_test_out + '/TestCompareDocumentOut.doc')

        result = self.words_api.compare_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate CompareDocument response')
        self.assertEqual('TestCompareDocumentOut.doc', result.document.file_name)

    #
    # Test for document comparison online.
    #
    def test_compare_document_online(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/CompareDocument'
        local_folder = 'DocumentActions/CompareDocument'
        local_name1 = 'compareTestDoc1.doc'
        local_name2 = 'compareTestDoc2.doc'
        remote_name2 = 'TestCompareDocument2.doc'

        self.upload_file(remote_folder + '/' + remote_name2, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name2), 'rb'))

        request_document = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name1), 'rb')
        request_compare_data_file_reference = asposewordscloud.FileReference.fromRemoteFilePath(remote_folder + '/' + remote_name2)
        request_compare_data = asposewordscloud.CompareData(author='author', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'), file_reference=request_compare_data_file_reference)
        request = asposewordscloud.models.requests.CompareDocumentOnlineRequest(document=request_document, compare_data=request_compare_data, dest_file_name=self.remote_test_out + '/TestCompareDocumentOut.doc')

        result = self.words_api.compare_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for document comparison online.
    #
    def test_compare_two_document_online(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/CompareDocument'
        local_folder = 'DocumentActions/CompareDocument'
        local_name1 = 'compareTestDoc1.doc'
        local_name2 = 'compareTestDoc2.doc'
        remote_name2 = 'TestCompareDocument2.doc'

        self.upload_file(remote_folder + '/' + remote_name2, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name2), 'rb'))

        request_document = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name1), 'rb')
        request_compare_data_file_reference_stream = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + local_name2), 'rb')
        request_compare_data_file_reference = asposewordscloud.FileReference.fromLocalFileContent(request_compare_data_file_reference_stream)
        request_compare_data = asposewordscloud.CompareData(author='author', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'), file_reference=request_compare_data_file_reference)
        request = asposewordscloud.models.requests.CompareDocumentOnlineRequest(document=request_document, compare_data=request_compare_data, dest_file_name=self.remote_test_out + '/TestCompareDocumentOut.doc')

        result = self.words_api.compare_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for document comparison with password protection.
    #
    def test_compare_document_with_password(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/CompareDocument'
        local_name = 'DocWithPassword.docx'
        remote_name1 = 'TestCompareDocument1.docx'
        remote_name2 = 'TestCompareDocument2.docx'

        self.upload_file(remote_folder + '/' + remote_name1, self.open_file(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb'))
        self.upload_file(remote_folder + '/' + remote_name2, self.open_file(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb'))

        request_compare_data_file_reference = asposewordscloud.FileReference.fromRemoteFilePath(remote_folder + '/' + remote_name2, "12345")
        request_compare_data = asposewordscloud.CompareData(author='author', date_time=dateutil.parser.isoparse('2015-10-26T00:00:00.0000000Z'), file_reference=request_compare_data_file_reference)
        request = asposewordscloud.models.requests.CompareDocumentRequest(name=remote_name1, compare_data=request_compare_data, folder=remote_folder, password='12345', dest_file_name=self.remote_test_out + '/TestCompareDocumentOut.docx')

        result = self.words_api.compare_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate CompareDocumentWithPassword response')
        self.assertEqual('TestCompareDocumentOut.docx', result.document.file_name)
