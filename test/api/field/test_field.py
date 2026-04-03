# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_field.py">
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
# Example of how to work with field.
#
class TestField(BaseTestContext):
    #
    # Test for getting fields.
    #
    def test_get_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestGetFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.GetFieldsRequest(name=remote_file_name, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.fields, 'Validate GetFields response')
        self.assertIsNotNone(result.fields.list, 'Validate GetFields response')
        self.assertEqual(1, len(result.fields.list))
        self.assertEqual('1', result.fields.list[0].result)

    #
    # Test for getting fields online.
    #
    def test_get_fields_online(self):
        field_folder = 'DocumentElements/Fields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/GetField.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFieldsOnlineRequest(document=request_document, node_path='sections/0')

        result = self.words_api.get_fields_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting fields without node path.
    #
    def test_get_fields_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestGetFieldsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.GetFieldsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.fields, 'Validate GetFieldsWithoutNodePath response')
        self.assertIsNotNone(result.fields.list, 'Validate GetFieldsWithoutNodePath response')
        self.assertEqual(1, len(result.fields.list))
        self.assertEqual('1', result.fields.list[0].result)

    #
    # Test for getting field by index.
    #
    def test_get_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestGetField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.GetFieldRequest(name=remote_file_name, index=0, node_path='sections/0/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate GetField response')
        self.assertEqual('1', result.field.result)

    #
    # Test for getting field by index online.
    #
    def test_get_field_online(self):
        field_folder = 'DocumentElements/Fields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/GetField.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFieldOnlineRequest(document=request_document, index=0, node_path='sections/0/paragraphs/0')

        result = self.words_api.get_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting field by index without node path.
    #
    def test_get_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestGetFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.GetFieldRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate GetFieldWithoutNodePath response')
        self.assertEqual('1', result.field.result)

    #
    # Test for putting field.
    #
    def test_insert_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        text_folder = 'DocumentElements/Text'
        local_file_name = 'SampleWordDocument.docx'
        remote_file_name = 'TestInsertField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, text_folder + '/' + local_file_name), 'rb'))

        request_field = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldRequest(name=remote_file_name, field=request_field, node_path='sections/0/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate InsertField response')
        self.assertEqual('{ NUMPAGES }', result.field.field_code)
        self.assertEqual('0.0.0.1', result.field.node_id)

    #
    # Test for putting field online.
    #
    def test_insert_field_online(self):
        field_folder = 'DocumentElements/Fields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/GetField.docx'), 'rb')
        request_field = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldOnlineRequest(document=request_document, field=request_field, node_path='sections/0/paragraphs/0')

        result = self.words_api.insert_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for putting field without node path.
    #
    def test_insert_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        text_folder = 'DocumentElements/Text'
        local_file_name = 'SampleWordDocument.docx'
        remote_file_name = 'TestInsertFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, text_folder + '/' + local_file_name), 'rb'))

        request_field = asposewordscloud.FieldInsert(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.InsertFieldRequest(name=remote_file_name, field=request_field, folder=remote_data_folder)

        result = self.words_api.insert_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate InsertFieldWithoutNodePath response')
        self.assertEqual('{ NUMPAGES }', result.field.field_code)
        self.assertEqual('5.0.22.0', result.field.node_id)

    #
    # Test for posting field.
    #
    def test_update_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestUpdateField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request_field = asposewordscloud.FieldUpdate(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.UpdateFieldRequest(name=remote_file_name, index=0, field=request_field, node_path='sections/0/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.update_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.field, 'Validate UpdateField response')
        self.assertEqual('{ NUMPAGES }', result.field.field_code)
        self.assertEqual('0.0.0.0', result.field.node_id)

    #
    # Test for posting field online.
    #
    def test_update_field_online(self):
        field_folder = 'DocumentElements/Fields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/GetField.docx'), 'rb')
        request_field = asposewordscloud.FieldUpdate(field_code='{ NUMPAGES }')
        request = asposewordscloud.models.requests.UpdateFieldOnlineRequest(document=request_document, index=0, field=request_field, node_path='sections/0/paragraphs/0')

        result = self.words_api.update_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting page numbers field.
    #
    def test_insert_page_numbers(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestInsertPageNumbers.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request_page_number = asposewordscloud.PageNumber(alignment='center', format='{PAGE} of {NUMPAGES}', is_top=True, set_page_number_on_first_page=True)
        request = asposewordscloud.models.requests.InsertPageNumbersRequest(name=remote_file_name, page_number=request_page_number, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.insert_page_numbers(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate InsertPageNumbers response')
        self.assertEqual('TestInsertPageNumbers.docx', result.document.file_name)

    #
    # Test for inserting page numbers field online.
    #
    def test_insert_page_numbers_online(self):
        local_file_name = 'test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb')
        request_page_number = asposewordscloud.PageNumber(alignment='center', format='{PAGE} of {NUMPAGES}', is_top=True, set_page_number_on_first_page=True)
        request = asposewordscloud.models.requests.InsertPageNumbersOnlineRequest(document=request_document, page_number=request_page_number)

        result = self.words_api.insert_page_numbers_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting field.
    #
    def test_delete_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestDeleteField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldRequest(name=remote_file_name, index=0, node_path='sections/0/paragraphs/0', folder=remote_data_folder)

        self.words_api.delete_field(request)


    #
    # Test for deleting field online.
    #
    def test_delete_field_online(self):
        field_folder = 'DocumentElements/Fields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/GetField.docx'), 'rb')
        request = asposewordscloud.models.requests.DeleteFieldOnlineRequest(document=request_document, index=0, node_path='sections/0/paragraphs/0')

        result = self.words_api.delete_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting field without node path.
    #
    def test_delete_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        field_folder = 'DocumentElements/Fields'
        local_file_name = 'GetField.docx'
        remote_file_name = 'TestDeleteFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        self.words_api.delete_field(request)


    #
    # Test for deleting paragraph fields.
    #
    def test_delete_paragraph_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestDeleteParagraphFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remote_file_name, node_path='paragraphs/0', folder=remote_data_folder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting paragraph fields without node path.
    #
    def test_delete_paragraph_fields_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestDeleteParagraphFieldsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remote_file_name, folder=remote_data_folder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting section fields.
    #
    def test_delete_section_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestDeleteSectionFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remote_file_name, node_path='sections/0', folder=remote_data_folder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting section fields without node path.
    #
    def test_delete_section_fields_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestDeleteSectionFieldsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remote_file_name, folder=remote_data_folder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting paragraph fields in section.
    #
    def test_delete_section_paragraph_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestDeleteSectionParagraphFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remote_file_name, node_path='sections/0/paragraphs/0', folder=remote_data_folder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting fields.
    #
    def test_delete_document_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestDeleteSectionParagraphFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.DeleteFieldsRequest(name=remote_file_name, node_path='', folder=remote_data_folder)

        self.words_api.delete_fields(request)


    #
    # Test for deleting fields online.
    #
    def test_delete_document_fields_online(self):
        local_file_name = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file_name), 'rb')
        request = asposewordscloud.models.requests.DeleteFieldsOnlineRequest(document=request_document, node_path='')

        result = self.words_api.delete_fields_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for posting updated fields.
    #
    def test_update_document_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Fields'
        local_file_name = 'test_multi_pages.docx'
        remote_file_name = 'TestUpdateDocumentFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/' + local_file_name), 'rb'))

        request = asposewordscloud.models.requests.UpdateFieldsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.update_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate UpdateDocumentFields response')
        self.assertEqual('TestUpdateDocumentFields.docx', result.document.file_name)

    #
    # Test for posting updated fields online.
    #
    def test_update_document_fields_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.UpdateFieldsOnlineRequest(document=request_document)

        result = self.words_api.update_fields_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

