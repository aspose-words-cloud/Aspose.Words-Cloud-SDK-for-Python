# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_signature.py">
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
# Example of how to work with signatures.
#
class TestSignature(BaseTestContext):
    #
    # Test for getting all document signatures.
    #
    def test_get_signatures(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/Signature'
        local_folder = 'DocumentActions/Signature'
        signed_document = 'signedDocument.docx'
        remote_name = 'TestGetSignatures.docx'

        self.upload_file(remote_folder + '/' + remote_name, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + signed_document), 'rb'))

        request = asposewordscloud.models.requests.GetSignaturesRequest(name=remote_name, folder=remote_folder)

        result = self.words_api.get_signatures(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.signatures, 'Validate GetSignatures response')
        self.assertEqual(1, len(result.signatures))

    #
    # Test for getting all document signatures online.
    #
    def test_get_signatures_online(self):
        local_folder = 'DocumentActions/Signature'
        signed_document = 'signedDocument.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + signed_document), 'rb')
        request = asposewordscloud.models.requests.GetSignaturesOnlineRequest(document=request_document)

        result = self.words_api.get_signatures_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.signatures, 'Validate GetSignaturesOnline response')
        self.assertEqual(1, len(result.signatures))

    #
    # Test for removing all document signatures.
    #
    def test_remove_all_signatures(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/Signature'
        local_folder = 'DocumentActions/Signature'
        signed_document = 'signedDocument.docx'
        remote_name = 'TestRemoveAllSignatures.docx'

        self.upload_file(remote_folder + '/' + remote_name, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + signed_document), 'rb'))

        request = asposewordscloud.models.requests.RemoveAllSignaturesRequest(name=remote_name, folder=remote_folder)

        result = self.words_api.remove_all_signatures(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.signatures, 'Validate RemoveAllSignatures response')
        self.assertEqual(0, len(result.signatures))

    #
    # Test for removing all document signatures online.
    #
    def test_remove_all_signatures_online(self):
        local_folder = 'DocumentActions/Signature'
        signed_document = 'signedDocument.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + signed_document), 'rb')
        request = asposewordscloud.models.requests.RemoveAllSignaturesOnlineRequest(document=request_document)

        result = self.words_api.remove_all_signatures_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.signatures, 'Validate RemoveAllSignaturesOnline response')
        self.assertEqual(0, len(result.model.signatures))

    #
    # Test for signing document.
    #
    def test_sign_document(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/Signature'
        local_folder = 'DocumentActions/Signature'
        unsigned_document = 'unsignedDocument.docx'
        certificate_name = 'morzal.pfx'
        certificate_password = 'aw'
        remote_name = 'TestSignDocument.docx'
        remote_certificate_name = 'TestCertificate.pfx'

        self.upload_file(remote_folder + '/' + remote_name, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + unsigned_document), 'rb'))
        self.upload_file(remote_folder + '/' + remote_certificate_name, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + certificate_name), 'rb'))

        request = asposewordscloud.models.requests.SignDocumentRequest(name=remote_name, certificate_path=remote_folder + '/' + remote_certificate_name, certificate_password=certificate_password, folder=remote_folder)

        result = self.words_api.sign_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.signatures, 'Validate SignDocument response')
        self.assertEqual(1, len(result.signatures))

    #
    # Test for signing document online.
    #
    def test_sign_document_online(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/Signature'
        local_folder = 'DocumentActions/Signature'
        unsigned_document = 'unsignedDocument.docx'
        certificate_name = 'morzal.pfx'
        certificate_password = 'aw'
        remote_certificate_name = 'TestCertificateOnline.pfx'

        self.upload_file(remote_folder + '/' + remote_certificate_name, self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + certificate_name), 'rb'))

        request_document = self.open_file(os.path.join(self.local_test_folder, local_folder + '/' + unsigned_document), 'rb')
        request = asposewordscloud.models.requests.SignDocumentOnlineRequest(document=request_document, certificate_path=remote_folder + '/' + remote_certificate_name, certificate_password=certificate_password)

        result = self.words_api.sign_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.signatures, 'Validate SignDocumentOnline response')
        self.assertEqual(1, len(result.model.signatures))
