# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_folder.py">
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
# Example of how to work with folders.
#
class TestFolder(BaseTestContext):
    #
    # Test for create folder.
    #
    def test_create_folder(self):
        remote_data_folder = self.remote_test_folder + '/Storage'

        request = asposewordscloud.models.requests.CreateFolderRequest(path=remote_data_folder + '/TestCreateFolder')

        self.words_api.create_folder(request)


    #
    # Test for delete folder.
    #
    def test_delete_folder(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        test_delete_folder = remote_data_folder + '/TestDeleteFolder'

        self.upload_file(test_delete_folder + '/TestDeleteFolder.docx', open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteFolderRequest(path=test_delete_folder, recursive=True)

        self.words_api.delete_folder(request)


    #
    # Test for get file list of folder.
    #
    def test_get_files_list(self):
        remote_data_folder = self.remote_test_folder + '/Storage'

        request = asposewordscloud.models.requests.GetFilesListRequest(path=remote_data_folder)

        result = self.words_api.get_files_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.value, 'Validate GetFilesList response')

    #
    # Test for copy folder.
    #
    def test_copy_folder(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'
        folder_to_copy = remote_data_folder + '/TestCopyFolder'

        self.upload_file(folder_to_copy + 'Src/TestCopyFolderSrc.docx', open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.CopyFolderRequest(dest_path=folder_to_copy + 'Dest', src_path=folder_to_copy + 'Src')

        self.words_api.copy_folder(request)


    #
    # Test for move folder.
    #
    def test_move_folder(self):
        remote_data_folder = self.remote_test_folder + '/Storage'
        local_file = 'Common/test_multi_pages.docx'

        self.upload_file(remote_data_folder + '/TestMoveFolderSrc/TestMoveFolderSrc.docx', open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.MoveFolderRequest(dest_path=self.remote_test_out + '/TestMoveFolderDest_' + self.create_random_guid(), src_path=remote_data_folder + '/TestMoveFolderSrc')

        self.words_api.move_folder(request)

