# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_table_border.py">
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
# Example of how to work with table borders.
#
class TestTableBorder(BaseTestContext):
    #
    # Test for getting borders.
    #
    def test_get_borders(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetBorders.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetBordersRequest(name=remote_file_name, node_path='tables/1/rows/0/cells/0', folder=remote_data_folder)

        result = self.words_api.get_borders(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.borders, 'Validate GetBorders response')
        self.assertIsNotNone(result.borders.list, 'Validate GetBorders response')
        self.assertEqual(6, len(result.borders.list))
        self.assertIsNotNone(result.borders.list[0].color, 'Validate GetBorders response')
        self.assertEqual('#000000', result.borders.list[0].color.web)

    #
    # Test for getting borders online.
    #
    def test_get_borders_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetBordersOnlineRequest(document=request_document, node_path='tables/1/rows/0/cells/0')

        result = self.words_api.get_borders_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting border.
    #
    def test_get_border(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetBorder.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetBorderRequest(name=remote_file_name, border_type='left', node_path='tables/1/rows/0/cells/0', folder=remote_data_folder)

        result = self.words_api.get_border(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.border, 'Validate GetBorder response')
        self.assertIsNotNone(result.border.color, 'Validate GetBorder response')
        self.assertEqual('#000000', result.border.color.web)

    #
    # Test for getting border online.
    #
    def test_get_border_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetBorderOnlineRequest(document=request_document, border_type='left', node_path='tables/1/rows/0/cells/0')

        result = self.words_api.get_border_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting borders.
    #
    def test_delete_borders(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestDeleteBorders.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteBordersRequest(name=remote_file_name, node_path='tables/1/rows/0/cells/0', folder=remote_data_folder)

        result = self.words_api.delete_borders(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting borders online.
    #
    def test_delete_borders_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteBordersOnlineRequest(document=request_document, node_path='tables/1/rows/0/cells/0')

        result = self.words_api.delete_borders_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting border.
    #
    def test_delete_border(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestDeleteBorder.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteBorderRequest(name=remote_file_name, border_type='left', node_path='tables/1/rows/0/cells/0', folder=remote_data_folder)

        result = self.words_api.delete_border(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting border online.
    #
    def test_delete_border_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteBorderOnlineRequest(document=request_document, border_type='left', node_path='tables/1/rows/0/cells/0')

        result = self.words_api.delete_border_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating border.
    #
    def test_update_border(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestUpdateBorder.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_border_properties_color = asposewordscloud.XmlColor(web='#AABBCC')
        request_border_properties = asposewordscloud.Border(border_type='Left', color=request_border_properties_color, distance_from_text=6.0, line_style='DashDotStroker', line_width=2.0, shadow=True)
        request = asposewordscloud.models.requests.UpdateBorderRequest(name=remote_file_name, border_type='left', border_properties=request_border_properties, node_path='tables/1/rows/0/cells/0', folder=remote_data_folder)

        result = self.words_api.update_border(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.border, 'Validate UpdateBorder response')
        self.assertIsNotNone(result.border.color, 'Validate UpdateBorder response')
        self.assertEqual('#AABBCC', result.border.color.web)
        self.assertEqual(6.0, result.border.distance_from_text)
        self.assertEqual(2.0, result.border.line_width)
        self.assertTrue(result.border.shadow, 'Validate UpdateBorder response')

    #
    # Test for updating border online.
    #
    def test_update_border_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_border_properties_color = asposewordscloud.XmlColor(web='#AABBCC')
        request_border_properties = asposewordscloud.Border(border_type='Left', color=request_border_properties_color, distance_from_text=6, line_style='DashDotStroker', line_width=2, shadow=True)
        request = asposewordscloud.models.requests.UpdateBorderOnlineRequest(document=request_document, border_properties=request_border_properties, border_type='left', node_path='tables/1/rows/0/cells/0')

        result = self.words_api.update_border_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

