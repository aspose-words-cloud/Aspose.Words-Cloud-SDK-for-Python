# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_revisions.py">
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
# Example of how to accept all revisions in document.
#
class TestRevisions(BaseTestContext):
    #
    # Test for accepting revisions in document.
    #
    def test_accept_all_revisions(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Revisions'
        local_file = 'DocumentElements/Revisions/TestRevisions.doc'
        remote_file_name = 'TestAcceptAllRevisions.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name=remote_file_name, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.accept_all_revisions(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.result, 'Validate AcceptAllRevisions response')
        self.assertIsNotNone(result.result.dest, 'Validate AcceptAllRevisions response')

    #
    # Test for accepting revisions in document online.
    #
    def test_accept_all_revisions_online(self):
        local_file = 'DocumentElements/Revisions/TestRevisions.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document=request_document)

        result = self.words_api.accept_all_revisions_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate AcceptAllRevisionsOnline response')
        self.assertIsNotNone(result.model, 'Validate AcceptAllRevisionsOnline response')
        self.assertIsNotNone(result.model.result, 'Validate AcceptAllRevisionsOnline response')
        self.assertIsNotNone(result.model.result.dest, 'Validate AcceptAllRevisionsOnline response')

    #
    # Test for rejecting revisions in document.
    #
    def test_reject_all_revisions(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Revisions'
        local_file = 'DocumentElements/Revisions/TestRevisions.doc'
        remote_file_name = 'TestRejectAllRevisions.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RejectAllRevisionsRequest(name=remote_file_name, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.reject_all_revisions(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.result, 'Validate RejectAllRevisions response')
        self.assertIsNotNone(result.result.dest, 'Validate RejectAllRevisions response')

    #
    # Test for rejecting revisions in document online.
    #
    def test_reject_all_revisions_online(self):
        local_file = 'DocumentElements/Revisions/TestRevisions.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.RejectAllRevisionsOnlineRequest(document=request_document)

        result = self.words_api.reject_all_revisions_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate RejectAllRevisionsOnline response')
        self.assertIsNotNone(result.model, 'Validate RejectAllRevisionsOnline response')
        self.assertIsNotNone(result.model.result, 'Validate RejectAllRevisionsOnline response')
        self.assertIsNotNone(result.model.result.dest, 'Validate RejectAllRevisionsOnline response')

    #
    # Test for getting revisions from document.
    #
    def test_get_all_revisions(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Revisions'
        local_file = 'DocumentElements/Revisions/TestRevisions.doc'
        remote_file_name = 'TestAcceptAllRevisions.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetAllRevisionsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_all_revisions(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.revisions, 'Validate GetAllRevisions response')
        self.assertEqual(6, len(result.revisions.revisions))

    #
    # Test for getting revisions online from document.
    #
    def test_get_all_revisions_online(self):
        local_file = 'DocumentElements/Revisions/TestRevisions.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetAllRevisionsOnlineRequest(document=request_document)

        result = self.words_api.get_all_revisions_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.revisions, 'Validate GetAllRevisionsOnline response')
        self.assertEqual(6, len(result.revisions.revisions))
