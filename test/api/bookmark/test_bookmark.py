# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_bookmark.py">
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
# Example of how to get all bookmarks from document.
#
class TestBookmark(BaseTestContext):
    #
    # Test for getting bookmarks from document.
    #
    def test_get_bookmarks(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentBookmarks.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetBookmarksRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_bookmarks(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting bookmarks from document online.
    #
    def test_get_bookmarks_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetBookmarksOnlineRequest(document=request_document)

        result = self.words_api.get_bookmarks_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting bookmark by specified name.
    #
    def test_get_bookmark_by_name(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        local_file = 'Common/test_multi_pages.docx'
        bookmark_name = 'aspose'
        remote_file_name = 'TestGetDocumentBookmarkByName.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetBookmarkByNameRequest(name=remote_file_name, bookmark_name=bookmark_name, folder=remote_data_folder)

        result = self.words_api.get_bookmark_by_name(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting bookmark by specified name online.
    #
    def test_get_bookmark_by_name_online(self):
        local_file = 'Common/test_multi_pages.docx'
        bookmark_name = 'aspose'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetBookmarkByNameOnlineRequest(document=request_document, bookmark_name=bookmark_name)

        result = self.words_api.get_bookmark_by_name_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating existed bookmark.
    #
    def test_update_bookmark(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        local_file = 'Common/test_multi_pages.docx'
        bookmark_name = 'aspose'
        remote_file_name = 'TestUpdateDocumentBookmark.docx'
        bookmark_text = 'This will be the text for Aspose'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_bookmark_data = asposewordscloud.BookmarkData(name=bookmark_name, text=bookmark_text)
        request = asposewordscloud.models.requests.UpdateBookmarkRequest(name=remote_file_name, bookmark_name=bookmark_name, bookmark_data=request_bookmark_data, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.update_bookmark(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating existed bookmark online.
    #
    def test_update_bookmark_online(self):
        local_file = 'Common/test_multi_pages.docx'
        bookmark_name = 'aspose'
        remote_file_name = 'TestUpdateDocumentBookmark.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_bookmark_data = asposewordscloud.BookmarkData(name=bookmark_name, text='This will be the text for Aspose')
        request = asposewordscloud.models.requests.UpdateBookmarkOnlineRequest(document=request_document, bookmark_name=bookmark_name, bookmark_data=request_bookmark_data, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.update_bookmark_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting bookmark by specified name.
    #
    def test_delete_bookmark(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        local_file = 'Common/test_multi_pages.docx'
        bookmark_name = 'aspose'
        remote_file_name = 'TestDeleteBookmark.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteBookmarkRequest(name=remote_file_name, bookmark_name=bookmark_name, folder=remote_data_folder)

        self.words_api.delete_bookmark(request)


    #
    # Test for deleting bookmark by specified name online.
    #
    def test_delete_bookmark_online(self):
        local_file = 'Common/test_multi_pages.docx'
        bookmark_name = 'aspose'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteBookmarkOnlineRequest(document=request_document, bookmark_name=bookmark_name)

        result = self.words_api.delete_bookmark_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting all bookmarks from document.
    #
    def test_delete_bookmarks(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteBookmarks.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteBookmarksRequest(name=remote_file_name, folder=remote_data_folder)

        self.words_api.delete_bookmarks(request)


    #
    # Test for deleting all bookmarks from document online.
    #
    def test_delete_bookmarks_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteBookmarksOnlineRequest(document=request_document)

        result = self.words_api.delete_bookmarks_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting new bookmark.
    #
    def test_insert_bookmark(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Bookmarks'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertBookmark.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_bookmark_start_range = asposewordscloud.PositionInsideNode(node_id='0.0.0.0', offset=0)
        request_bookmark_end_range = asposewordscloud.PositionInsideNode(node_id='0.0.0.0', offset=0)
        request_bookmark = asposewordscloud.BookmarkInsert(start_range=request_bookmark_start_range, end_range=request_bookmark_end_range, name='new_bookmark', text='Some text')
        request = asposewordscloud.models.requests.InsertBookmarkRequest(name=remote_file_name, bookmark=request_bookmark, folder=remote_data_folder)

        result = self.words_api.insert_bookmark(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting new bookmark online.
    #
    def test_insert_bookmark_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_bookmark_start_range = asposewordscloud.PositionInsideNode(node_id='0.0.0.0', offset=0)
        request_bookmark_end_range = asposewordscloud.PositionInsideNode(node_id='0.0.0.0', offset=0)
        request_bookmark = asposewordscloud.BookmarkInsert(start_range=request_bookmark_start_range, end_range=request_bookmark_end_range, name='new_bookmark', text='Some text')
        request = asposewordscloud.models.requests.InsertBookmarkOnlineRequest(document=request_document, bookmark=request_bookmark)

        result = self.words_api.insert_bookmark_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

