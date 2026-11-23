# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_lists.py">
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
# Example of how to work with lists.
#
class TestLists(BaseTestContext):
    #
    # Test for getting lists from document.
    #
    def test_get_lists(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Lists'
        local_file = 'DocumentElements/Lists/ListsGet.doc'
        remote_file_name = 'TestGetLists.doc'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetListsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_lists(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.lists, 'Validate GetLists response')
        self.assertIsNotNone(result.lists.list_info, 'Validate GetLists response')
        self.assertEqual(2, len(result.lists.list_info))
        self.assertEqual(1, result.lists.list_info[0].list_id)

    #
    # Test for getting lists from document online.
    #
    def test_get_lists_online(self):
        local_file = 'DocumentElements/Lists/ListsGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetListsOnlineRequest(document=request_document)

        result = self.words_api.get_lists_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting list from document.
    #
    def test_get_list(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Lists'
        local_file = 'DocumentElements/Lists/ListsGet.doc'
        remote_file_name = 'TestGetList.doc'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetListRequest(name=remote_file_name, list_id=1, folder=remote_data_folder)

        result = self.words_api.get_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list, 'Validate GetList response')
        self.assertEqual(1, result.list.list_id)

    #
    # Test for getting list from document online.
    #
    def test_get_list_online(self):
        local_file = 'DocumentElements/Lists/ListsGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetListOnlineRequest(document=request_document, list_id=1)

        result = self.words_api.get_list_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating list from document.
    #
    def test_update_list(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Lists'
        local_file = 'DocumentElements/Lists/ListsGet.doc'
        remote_file_name = 'TestUpdateList.doc'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_list_update = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
        request = asposewordscloud.models.requests.UpdateListRequest(name=remote_file_name, list_id=1, list_update=request_list_update, folder=remote_data_folder)

        result = self.words_api.update_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating list from document online.
    #
    def test_update_list_online(self):
        local_file = 'DocumentElements/Lists/ListsGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_list_update = asposewordscloud.ListUpdate(is_restart_at_each_section=True)
        request = asposewordscloud.models.requests.UpdateListOnlineRequest(document=request_document, list_id=1, list_update=request_list_update)

        result = self.words_api.update_list_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.list, 'Validate UpdateListOnline response')
        self.assertEqual(1, result.model.list.list_id)
        self.assertTrue(result.model.list.is_restart_at_each_section, 'Validate UpdateListOnline response')

    #
    # Test for updating list level from document.
    #
    def test_update_list_level(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Lists'
        local_file = 'DocumentElements/Lists/ListsGet.doc'
        remote_file_name = 'TestUpdateListLevel.doc'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_list_update = asposewordscloud.ListLevelUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateListLevelRequest(name=remote_file_name, list_id=1, list_level=1, list_update=request_list_update, folder=remote_data_folder)

        result = self.words_api.update_list_level(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating list level from document online.
    #
    def test_update_list_level_online(self):
        local_file = 'DocumentElements/Lists/ListsGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_list_update = asposewordscloud.ListLevelUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateListLevelOnlineRequest(document=request_document, list_id=1, list_level=1, list_update=request_list_update)

        result = self.words_api.update_list_level_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.list, 'Validate UpdateListLevelOnline response')
        self.assertIsNotNone(result.model.list.list_levels, 'Validate UpdateListLevelOnline response')
        self.assertIsNotNone(result.model.list.list_levels.list_level, 'Validate UpdateListLevelOnline response')
        self.assertEqual(9, len(result.model.list.list_levels.list_level))


    #
    # Test for inserting list from document.
    #
    def test_insert_list(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Lists'
        local_file = 'DocumentElements/Lists/ListsGet.doc'
        remote_file_name = 'TestInsertList.doc'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_list_insert = asposewordscloud.ListInsert(template='OutlineLegal')
        request = asposewordscloud.models.requests.InsertListRequest(name=remote_file_name, list_insert=request_list_insert, folder=remote_data_folder)

        result = self.words_api.insert_list(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list, 'Validate InsertList response')
        self.assertEqual(3, result.list.list_id)

    #
    # Test for inserting list from document online.
    #
    def test_insert_list_online(self):
        local_file = 'DocumentElements/Lists/ListsGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_list_insert = asposewordscloud.ListInsert(template='OutlineLegal')
        request = asposewordscloud.models.requests.InsertListOnlineRequest(document=request_document, list_insert=request_list_insert)

        result = self.words_api.insert_list_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

