# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_form_field.py">
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
# Example of how to work with form field.
#
class TestFormField(BaseTestContext):
    #
    # Test for posting form field.
    #
    def test_update_form_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestUpdateFormField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name', text_input_format='')
        request = asposewordscloud.models.requests.UpdateFormFieldRequest(name=remote_file_name, index=0, form_field=request_form_field, node_path='sections/0', folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.update_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_field, 'Validate UpdateFormField response')
        self.assertEqual('FullName', result.form_field.name)
        self.assertEqual('', result.form_field.status_text)

    #
    # Test for posting form field online.
    #
    def test_update_form_field_online(self):
        field_folder = 'DocumentElements/FormFields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb')
        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name', text_input_format='')
        request = asposewordscloud.models.requests.UpdateFormFieldOnlineRequest(document=request_document, index=0, form_field=request_form_field, node_path='sections/0')

        result = self.words_api.update_form_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for posting form field without node path.
    #
    def test_update_form_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestUpdateFormFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='No name', text_input_format='')
        request = asposewordscloud.models.requests.UpdateFormFieldRequest(name=remote_file_name, index=0, form_field=request_form_field, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.update_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_field, 'Validate UpdateFormFieldWithoutNodePath response')
        self.assertEqual('FullName', result.form_field.name)
        self.assertEqual('', result.form_field.status_text)

    #
    # Test for getting form field.
    #
    def test_get_form_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestGetFormField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldRequest(name=remote_file_name, index=0, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_field, 'Validate GetFormField response')
        self.assertEqual('FullName', result.form_field.name)

    #
    # Test for getting form field online.
    #
    def test_get_form_field_online(self):
        field_folder = 'DocumentElements/FormFields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFormFieldOnlineRequest(document=request_document, index=0, node_path='sections/0')

        result = self.words_api.get_form_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting form field without node path.
    #
    def test_get_form_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestGetFormFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_field, 'Validate GetFormFieldWithoutNodePath response')
        self.assertEqual('FullName', result.form_field.name)

    #
    # Test for getting form fields.
    #
    def test_get_form_fields(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestGetFormFields.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldsRequest(name=remote_file_name, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_form_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_fields, 'Validate GetFormFields response')
        self.assertIsNotNone(result.form_fields.list, 'Validate GetFormFields response')
        self.assertEqual(5, len(result.form_fields.list))
        self.assertEqual('FullName', result.form_fields.list[0].name)

    #
    # Test for getting form fields online.
    #
    def test_get_form_fields_online(self):
        field_folder = 'DocumentElements/FormFields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb')
        request = asposewordscloud.models.requests.GetFormFieldsOnlineRequest(document=request_document, node_path='sections/0')

        result = self.words_api.get_form_fields_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting form fields without node path.
    #
    def test_get_form_fields_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestGetFormFieldsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetFormFieldsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_form_fields(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_fields, 'Validate GetFormFieldsWithoutNodePath response')
        self.assertIsNotNone(result.form_fields.list, 'Validate GetFormFieldsWithoutNodePath response')
        self.assertEqual(5, len(result.form_fields.list))
        self.assertEqual('FullName', result.form_fields.list[0].name)

    #
    # Test for insert form field without node path.
    #
    def test_insert_form_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        remote_file_name = 'TestInsertFormField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/test_multi_pages.docx'), 'rb'))

        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        request = asposewordscloud.models.requests.InsertFormFieldRequest(name=remote_file_name, form_field=request_form_field, node_path='sections/0/paragraphs/0', folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.insert_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_field, 'Validate InsertFormField response')
        self.assertEqual('FullName', result.form_field.name)
        self.assertEqual('', result.form_field.status_text)

    #
    # Test for insert form field without node path online.
    #
    def test_insert_form_field_online(self):
        field_folder = 'DocumentElements/FormFields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb')
        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        request = asposewordscloud.models.requests.InsertFormFieldOnlineRequest(document=request_document, form_field=request_form_field, node_path='sections/0/paragraphs/0')

        result = self.words_api.insert_form_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for insert form field without node path.
    #
    def test_insert_form_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        remote_file_name = 'TestInsertFormFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'Common/test_multi_pages.docx'), 'rb'))

        request_form_field = asposewordscloud.FormFieldTextInput(name='FullName', enabled=True, calculate_on_exit=True, status_text='', text_input_type='Regular', text_input_default='123', text_input_format='UPPERCASE')
        request = asposewordscloud.models.requests.InsertFormFieldRequest(name=remote_file_name, form_field=request_form_field, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.insert_form_field(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.form_field, 'Validate InsertFormFieldWithoutNodePath response')
        self.assertEqual('FullName', result.form_field.name)
        self.assertEqual('', result.form_field.status_text)

    #
    # Test for deleting form field.
    #
    def test_delete_form_field(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestDeleteFormField.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFormFieldRequest(name=remote_file_name, index=0, node_path='sections/0', folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        self.words_api.delete_form_field(request)


    #
    # Test for deleting form field online.
    #
    def test_delete_form_field_online(self):
        field_folder = 'DocumentElements/FormFields'

        request_document = open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb')
        request = asposewordscloud.models.requests.DeleteFormFieldOnlineRequest(document=request_document, index=0, node_path='sections/0')

        result = self.words_api.delete_form_field_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting form field without node path.
    #
    def test_delete_form_field_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/FormFields'
        field_folder = 'DocumentElements/FormFields'
        remote_file_name = 'TestDeleteFormFieldWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, field_folder + '/FormFilled.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFormFieldRequest(name=remote_file_name, index=0, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        self.words_api.delete_form_field(request)

