# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_structured_document_tag.py">
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
# Example of how to use structured document tags.
#
class TestStructuredDocumentTag(BaseTestContext):
    #
    # Test for getting SDT objects from document.
    #
    def test_get_structured_document_tags(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/StructuredDocumentTag'
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'
        remote_file_name = 'TestGetStructuredDocumentTags.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetStructuredDocumentTagsRequest(name=remote_file_name, node_path='sections/0/body/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.get_structured_document_tags(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting SDT objects from document online.
    #
    def test_get_structured_document_tags_online(self):
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetStructuredDocumentTagsOnlineRequest(document=request_document, node_path='sections/0/body/paragraphs/0')

        result = self.words_api.get_structured_document_tags_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting SDT object from document.
    #
    def test_get_structured_document_tag(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/StructuredDocumentTag'
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'
        remote_file_name = 'TestGetStructuredDocumentTag.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetStructuredDocumentTagRequest(name=remote_file_name, node_path='sections/0/body/paragraphs/0', index=0, folder=remote_data_folder)

        result = self.words_api.get_structured_document_tag(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting SDT object from document online.
    #
    def test_get_structured_document_tag_online(self):
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetStructuredDocumentTagOnlineRequest(document=request_document, node_path='sections/0/body/paragraphs/0', index=0)

        result = self.words_api.get_structured_document_tag_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding SDT object.
    #
    def test_insert_structured_document_tag(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/StructuredDocumentTag'
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'
        remote_file_name = 'TestInsetStructuredDocumentTag.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_structured_document_tag = asposewordscloud.StructuredDocumentTagInsert(sdt_type='ComboBox', level='Inline')
        request = asposewordscloud.models.requests.InsertStructuredDocumentTagRequest(name=remote_file_name, structured_document_tag=request_structured_document_tag, node_path='sections/0/body/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.insert_structured_document_tag(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding SDT object online.
    #
    def test_insert_structured_document_tag_online(self):
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_structured_document_tag = asposewordscloud.StructuredDocumentTagInsert(sdt_type='ComboBox', level='Inline')
        request = asposewordscloud.models.requests.InsertStructuredDocumentTagOnlineRequest(document=request_document, structured_document_tag=request_structured_document_tag, node_path='sections/0/body/paragraphs/0')

        result = self.words_api.insert_structured_document_tag_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting SDT object.
    #
    def test_delete_structured_document_tag(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/StructuredDocumentTag'
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'
        remote_file_name = 'TestDeleteStructuredDocumentTag.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteStructuredDocumentTagRequest(name=remote_file_name, index=0, node_path='sections/0/body/paragraphs/0', folder=remote_data_folder)

        self.words_api.delete_structured_document_tag(request)


    #
    # Test for deleting SDT object online.
    #
    def test_delete_structured_document_tag_online(self):
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteStructuredDocumentTagOnlineRequest(document=request_document, index=0, node_path='sections/0/body/paragraphs/0')

        result = self.words_api.delete_structured_document_tag_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating SDT object.
    #
    def test_update_structured_document_tag(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/StructuredDocumentTag'
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'
        remote_file_name = 'TestUpdateStructuredDocumentTag.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_structured_document_tag_list_items0 = asposewordscloud.StructuredDocumentTagListItem(display_text='Aspose Words', value='1')
        request_structured_document_tag_list_items1 = asposewordscloud.StructuredDocumentTagListItem(display_text='Hello world', value='2')
        request_structured_document_tag_list_items = [request_structured_document_tag_list_items0, request_structured_document_tag_list_items1]
        request_structured_document_tag = asposewordscloud.StructuredDocumentTagUpdate(list_items=request_structured_document_tag_list_items)
        request = asposewordscloud.models.requests.UpdateStructuredDocumentTagRequest(name=remote_file_name, structured_document_tag=request_structured_document_tag, index=0, node_path='sections/0/body/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.update_structured_document_tag(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating SDT object online.
    #
    def test_update_structured_document_tag_online(self):
        local_file = 'DocumentElements/StructuredDocumentTag/StructuredDocumentTag.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_structured_document_tag_list_items0 = asposewordscloud.StructuredDocumentTagListItem(display_text='Aspose Words', value='1')
        request_structured_document_tag_list_items1 = asposewordscloud.StructuredDocumentTagListItem(display_text='Hello world', value='2')
        request_structured_document_tag_list_items = [request_structured_document_tag_list_items0, request_structured_document_tag_list_items1]
        request_structured_document_tag = asposewordscloud.StructuredDocumentTagUpdate(list_items=request_structured_document_tag_list_items)
        request = asposewordscloud.models.requests.UpdateStructuredDocumentTagOnlineRequest(document=request_document, structured_document_tag=request_structured_document_tag, index=0, node_path='sections/0/body/paragraphs/0')

        result = self.words_api.update_structured_document_tag_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

