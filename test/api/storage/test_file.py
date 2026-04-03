# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_file.py">
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
# Example of how to work with files.
#
class TestFile(BaseTestContext):
    #
    # Test for uploading file.
    #
    def test_upload_file(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestUploadFile.docx'

        request_file_content = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.UploadFileRequest(file_content=request_file_content, path=remote_data_folder + '/' + remote_file_name)

        result = self.words_api.upload_file(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.uploaded, 'Validate UploadFile response')
        self.assertEqual(1, len(result.uploaded))
        self.assertEqual('TestUploadFile.docx', result.uploaded[0])

    #
    # Test for copy file.
    #
    def test_copy_file(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestCopyFileSrc.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.CopyFileRequest(dest_path=remote_data_folder + '/TestCopyFileDest.docx', src_path=remote_data_folder + '/' + remote_file_name)

        self.words_api.copy_file(request)


    #
    # Test for move file.
    #
    def test_move_file(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestMoveFileSrc.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.MoveFileRequest(dest_path=self.remote_test_out + '/TestMoveFileDest_' + self.create_random_guid() + '.docx', src_path=remote_data_folder + '/' + remote_file_name)

        self.words_api.move_file(request)


    #
    # Test for delete file.
    #
    def test_delete_file(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteFile.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteFileRequest(path=remote_data_folder + '/' + remote_file_name)

        self.words_api.delete_file(request)


    #
    # Test for download file.
    #
    def test_download_file(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDownloadFile.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DownloadFileRequest(path=remote_data_folder + '/' + remote_file_name)

        result = self.words_api.download_file(request)
        self.assertIsNotNone(result, 'Error has occurred.')

