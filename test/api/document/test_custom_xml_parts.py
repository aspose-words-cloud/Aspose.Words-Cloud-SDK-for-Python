# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_custom_xml_parts.py">
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
# Example of how to use custom xml parts in documents.
#
class TestCustomXmlParts(BaseTestContext):
    #
    # Test for getting custom xml part by specified index.
    #
    def test_get_custom_xml_part(self):
        remote_data_folder = self.remote_test_folder + '/CustomXmlParts'
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'
        remote_file_name = 'TestGetCustomXmlPart.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetCustomXmlPartRequest(name=remote_file_name, custom_xml_part_index=0, folder=remote_data_folder)

        result = self.words_api.get_custom_xml_part(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.custom_xml_part, 'Validate GetCustomXmlPart response')
        self.assertEqual('aspose', result.custom_xml_part.id)
        self.assertEqual('<Metadata><Author>author1</Author><Initial>initial</Initial><DateTime>2015-01-22T00:00:00</DateTime><Text>text</Text></Metadata>', result.custom_xml_part.data)

    #
    # Test for getting custom xml part by specified index online.
    #
    def test_get_custom_xml_part_online(self):
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0)

        result = self.words_api.get_custom_xml_part_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.custom_xml_part, 'Validate GetCustomXmlPartOnline response')
        self.assertEqual('aspose', result.custom_xml_part.id)
        self.assertEqual('<Metadata><Author>author1</Author><Initial>initial</Initial><DateTime>2015-01-22T00:00:00</DateTime><Text>text</Text></Metadata>', result.custom_xml_part.data)

    #
    # Test for getting all custom xml parts from document.
    #
    def test_get_custom_xml_parts(self):
        remote_data_folder = self.remote_test_folder + '/CustomXmlParts'
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'
        remote_file_name = 'TestGetCustomXmlParts.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetCustomXmlPartsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_custom_xml_parts(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.custom_xml_parts, 'Validate GetCustomXmlParts response')
        self.assertIsNotNone(result.custom_xml_parts.custom_xml_parts_list, 'Validate GetCustomXmlParts response')
        self.assertEqual(2, len(result.custom_xml_parts.custom_xml_parts_list))
        self.assertEqual('aspose', result.custom_xml_parts.custom_xml_parts_list[0].id)
        self.assertEqual('<Metadata><Author>author1</Author><Initial>initial</Initial><DateTime>2015-01-22T00:00:00</DateTime><Text>text</Text></Metadata>', result.custom_xml_parts.custom_xml_parts_list[0].data)

    #
    # Test for getting all custom xml parts from document online.
    #
    def test_get_custom_xml_parts_online(self):
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetCustomXmlPartsOnlineRequest(document=request_document)

        result = self.words_api.get_custom_xml_parts_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.custom_xml_parts, 'Validate GetCustomXmlPartsOnline response')
        self.assertIsNotNone(result.custom_xml_parts.custom_xml_parts_list, 'Validate GetCustomXmlPartsOnline response')
        self.assertEqual(2, len(result.custom_xml_parts.custom_xml_parts_list))
        self.assertEqual('aspose', result.custom_xml_parts.custom_xml_parts_list[0].id)
        self.assertEqual('<Metadata><Author>author1</Author><Initial>initial</Initial><DateTime>2015-01-22T00:00:00</DateTime><Text>text</Text></Metadata>', result.custom_xml_parts.custom_xml_parts_list[0].data)

    #
    # Test for adding custom xml part.
    #
    def test_insert_custom_xml_part(self):
        remote_data_folder = self.remote_test_folder + '/CustomXmlParts'
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'
        remote_file_name = 'TestInsertCustomXmlPart.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_custom_xml_part = asposewordscloud.CustomXmlPartInsert(id='hello', data='<data>Hello world</data>')
        request = asposewordscloud.models.requests.InsertCustomXmlPartRequest(name=remote_file_name, custom_xml_part=request_custom_xml_part, folder=remote_data_folder)

        result = self.words_api.insert_custom_xml_part(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.custom_xml_part, 'Validate InsertCustomXmlPart response')
        self.assertEqual('hello', result.custom_xml_part.id)
        self.assertEqual('<data>Hello world</data>', result.custom_xml_part.data)

    #
    # Test for adding custom xml part online.
    #
    def test_insert_custom_xml_part_online(self):
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_custom_xml_part = asposewordscloud.CustomXmlPartInsert(id='hello', data='<data>Hello world</data>')
        request = asposewordscloud.models.requests.InsertCustomXmlPartOnlineRequest(document=request_document, custom_xml_part=request_custom_xml_part)

        result = self.words_api.insert_custom_xml_part_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.custom_xml_part, 'Validate InsertCustomXmlPartOnline response')
        self.assertEqual('hello', result.model.custom_xml_part.id)
        self.assertEqual('<data>Hello world</data>', result.model.custom_xml_part.data)

    #
    # Test for updating custom xml part.
    #
    def test_update_custom_xml_part(self):
        remote_data_folder = self.remote_test_folder + '/CustomXmlParts'
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'
        remote_file_name = 'TestUpdateCustomXmlPart.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_custom_xml_part = asposewordscloud.CustomXmlPartUpdate(data='<data>Hello world</data>')
        request = asposewordscloud.models.requests.UpdateCustomXmlPartRequest(name=remote_file_name, custom_xml_part_index=0, custom_xml_part=request_custom_xml_part, folder=remote_data_folder)

        result = self.words_api.update_custom_xml_part(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.custom_xml_part, 'Validate UpdateCustomXmlPart response')
        self.assertEqual('aspose', result.custom_xml_part.id)
        self.assertEqual('<data>Hello world</data>', result.custom_xml_part.data)

    #
    # Test for updating custom xml part online.
    #
    def test_update_custom_xml_part_online(self):
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_custom_xml_part = asposewordscloud.CustomXmlPartUpdate(data='<data>Hello world</data>')
        request = asposewordscloud.models.requests.UpdateCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0, custom_xml_part=request_custom_xml_part)

        result = self.words_api.update_custom_xml_part_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.model.custom_xml_part, 'Validate UpdateCustomXmlPartOnline response')
        self.assertEqual('aspose', result.model.custom_xml_part.id)
        self.assertEqual('<data>Hello world</data>', result.model.custom_xml_part.data)

    #
    # A test for DeleteCustomXmlPart.
    #
    def test_delete_custom_xml_part(self):
        remote_data_folder = self.remote_test_folder + '/CustomXmlParts'
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'
        remote_file_name = 'TestDeleteCustomXmlPart.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteCustomXmlPartRequest(name=remote_file_name, custom_xml_part_index=0, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        self.words_api.delete_custom_xml_part(request)


    #
    # A test for DeleteCustomXmlPart online.
    #
    def test_delete_custom_xml_part_online(self):
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteCustomXmlPartOnlineRequest(document=request_document, custom_xml_part_index=0)

        result = self.words_api.delete_custom_xml_part_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for DeleteCustomXmlParts.
    #
    def test_delete_custom_xml_parts(self):
        remote_data_folder = self.remote_test_folder + '/CustomXmlParts'
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'
        remote_file_name = 'TestDeleteCustomXmlPart.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteCustomXmlPartsRequest(name=remote_file_name, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        self.words_api.delete_custom_xml_parts(request)


    #
    # A test for DeleteCustomXmlParts online.
    #
    def test_delete_custom_xml_parts_online(self):
        local_file = 'DocumentElements/CustomXmlParts/MultipleCustomXmlParts.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteCustomXmlPartsOnlineRequest(document=request_document)

        result = self.words_api.delete_custom_xml_parts_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

