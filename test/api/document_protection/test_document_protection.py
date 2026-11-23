# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_document_protection.py">
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
# Example of how to set document protection.
#
class TestDocumentProtection(BaseTestContext):
    #
    # Test for setting document protection.
    #
    def test_protect_document(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestProtectDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_protection_request = asposewordscloud.ProtectionRequestV2(protection_password='123', protection_type='ReadOnly')
        request = asposewordscloud.models.requests.ProtectDocumentRequest(name=remote_file_name, protection_request=request_protection_request, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.protect_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.protection_data, 'Validate ProtectDocument response')


    #
    # Test for setting document protection.
    #
    def test_protect_document_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_protection_request = asposewordscloud.ProtectionRequestV2(protection_password='123', protection_type='ReadOnly')
        request = asposewordscloud.models.requests.ProtectDocumentOnlineRequest(document=request_document, protection_request=request_protection_request)

        result = self.words_api.protect_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting document protection.
    #
    def test_get_document_protection(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        local_file_path = 'DocumentActions/DocumentProtection/SampleProtectedBlankWordDocument.docx'
        remote_file_name = 'TestGetDocumentProtection.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file_path), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentProtectionRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_document_protection(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting document protection.
    #
    def test_get_document_protection_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentProtectionOnlineRequest(document=request_document)

        result = self.words_api.get_document_protection_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting unprotect document.
    #
    def test_delete_unprotect_document(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DocumentProtection'
        local_file_path = 'DocumentActions/DocumentProtection/SampleProtectedBlankWordDocument.docx'
        remote_file_name = 'TestDeleteUnprotectDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file_path), 'rb'))

        request = asposewordscloud.models.requests.UnprotectDocumentRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.unprotect_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.protection_data, 'Validate DeleteUnprotectDocument response')


    #
    # Test for deleting unprotect document.
    #
    def test_delete_unprotect_document_online(self):
        local_file_path = 'DocumentActions/DocumentProtection/SampleProtectedBlankWordDocument.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file_path), 'rb')
        request = asposewordscloud.models.requests.UnprotectDocumentOnlineRequest(document=request_document)

        result = self.words_api.unprotect_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

