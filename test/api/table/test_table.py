# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_table.py">
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
# Example of how to work wtih table.
#
class TestTable(BaseTestContext):
    #
    # Test for getting tables.
    #
    def test_get_tables(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTables.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTablesRequest(name=remote_file_name, node_path='', folder=remote_data_folder)

        result = self.words_api.get_tables(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tables, 'Validate GetTables response')
        self.assertIsNotNone(result.tables.table_link_list, 'Validate GetTables response')
        self.assertEqual(5, len(result.tables.table_link_list))
        self.assertEqual('0.0.1', result.tables.table_link_list[0].node_id)

    #
    # Test for getting tables online.
    #
    def test_get_tables_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTablesOnlineRequest(document=request_document, node_path='')

        result = self.words_api.get_tables_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting tables without node path.
    #
    def test_get_tables_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTablesWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTablesRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_tables(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tables, 'Validate GetTablesWithoutNodePath response')
        self.assertIsNotNone(result.tables.table_link_list, 'Validate GetTablesWithoutNodePath response')
        self.assertEqual(5, len(result.tables.table_link_list))
        self.assertEqual('0.0.1', result.tables.table_link_list[0].node_id)

    #
    # Test for getting table.
    #
    def test_get_table(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTable.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTableRequest(name=remote_file_name, index=1, node_path='', folder=remote_data_folder)

        result = self.words_api.get_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.table, 'Validate GetTable response')
        self.assertIsNotNone(result.table.table_row_list, 'Validate GetTable response')
        self.assertEqual(1, len(result.table.table_row_list))
        self.assertIsNotNone(result.table.table_row_list[0].table_cell_list, 'Validate GetTable response')
        self.assertEqual(2, len(result.table.table_row_list[0].table_cell_list))

    #
    # Test for getting table online.
    #
    def test_get_table_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTableOnlineRequest(document=request_document, index=1, node_path='')

        result = self.words_api.get_table_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting table without node path.
    #
    def test_get_table_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTableWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTableRequest(name=remote_file_name, index=1, folder=remote_data_folder)

        result = self.words_api.get_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.table, 'Validate GetTableWithoutNodePath response')
        self.assertIsNotNone(result.table.table_row_list, 'Validate GetTableWithoutNodePath response')
        self.assertEqual(1, len(result.table.table_row_list))
        self.assertIsNotNone(result.table.table_row_list[0].table_cell_list, 'Validate GetTableWithoutNodePath response')
        self.assertEqual(2, len(result.table.table_row_list[0].table_cell_list))

    #
    # Test for deleting table.
    #
    def test_delete_table(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestDeleteTable.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableRequest(name=remote_file_name, index=1, node_path='', folder=remote_data_folder)

        self.words_api.delete_table(request)


    #
    # Test for deleting table online.
    #
    def test_delete_table_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteTableOnlineRequest(document=request_document, index=1, node_path='')

        result = self.words_api.delete_table_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting table without node path.
    #
    def test_delete_table_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestDeleteTableWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableRequest(name=remote_file_name, index=1, folder=remote_data_folder)

        self.words_api.delete_table(request)


    #
    # Test for adding table.
    #
    def test_insert_table(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestInsertTable.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_table = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        request = asposewordscloud.models.requests.InsertTableRequest(name=remote_file_name, table=request_table, node_path='', folder=remote_data_folder)

        result = self.words_api.insert_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.table, 'Validate InsertTable response')
        self.assertIsNotNone(result.table.table_row_list, 'Validate InsertTable response')
        self.assertEqual(4, len(result.table.table_row_list))
        self.assertIsNotNone(result.table.table_row_list[0].table_cell_list, 'Validate InsertTable response')
        self.assertEqual(5, len(result.table.table_row_list[0].table_cell_list))

    #
    # Test for adding table online.
    #
    def test_insert_table_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_table = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        request = asposewordscloud.models.requests.InsertTableOnlineRequest(document=request_document, table=request_table, node_path='')

        result = self.words_api.insert_table_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding table without node path.
    #
    def test_insert_table_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestInsertTableWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_table = asposewordscloud.TableInsert(columns_count=5, rows_count=4)
        request = asposewordscloud.models.requests.InsertTableRequest(name=remote_file_name, table=request_table, folder=remote_data_folder)

        result = self.words_api.insert_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.table, 'Validate InsertTableWithoutNodePath response')
        self.assertIsNotNone(result.table.table_row_list, 'Validate InsertTableWithoutNodePath response')
        self.assertEqual(4, len(result.table.table_row_list))
        self.assertIsNotNone(result.table.table_row_list[0].table_cell_list, 'Validate InsertTableWithoutNodePath response')
        self.assertEqual(5, len(result.table.table_row_list[0].table_cell_list))

    #
    # Test for getting document properties.
    #
    def test_get_table_properties(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTableProperties.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTablePropertiesRequest(name=remote_file_name, index=1, node_path='', folder=remote_data_folder)

        result = self.words_api.get_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.properties, 'Validate GetTableProperties response')
        self.assertEqual('Table Grid', result.properties.style_name)

    #
    # Test for getting document properties online.
    #
    def test_get_table_properties_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTablePropertiesOnlineRequest(document=request_document, index=1, node_path='')

        result = self.words_api.get_table_properties_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting document properties without node path.
    #
    def test_get_table_properties_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTablePropertiesWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTablePropertiesRequest(name=remote_file_name, index=1, folder=remote_data_folder)

        result = self.words_api.get_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.properties, 'Validate GetTablePropertiesWithoutNodePath response')
        self.assertEqual('Table Grid', result.properties.style_name)

    #
    # Test for updating table properties.
    #
    def test_update_table_properties(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestUpdateTableProperties.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_properties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1, cell_spacing=2.0, style_options='ColumnBands')
        request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name=remote_file_name, properties=request_properties, index=1, node_path='', folder=remote_data_folder)

        result = self.words_api.update_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.properties, 'Validate UpdateTableProperties response')
        self.assertFalse(result.properties.allow_auto_fit, 'Validate UpdateTableProperties response')
        self.assertTrue(result.properties.bidi, 'Validate UpdateTableProperties response')
        self.assertEqual(1.0, result.properties.bottom_padding)
        self.assertEqual(2.0, result.properties.cell_spacing)

    #
    # Test for updating table properties online.
    #
    def test_update_table_properties_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_properties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1, cell_spacing=2, style_options='ColumnBands')
        request = asposewordscloud.models.requests.UpdateTablePropertiesOnlineRequest(document=request_document, properties=request_properties, index=1, node_path='')

        result = self.words_api.update_table_properties_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating table properties without node path.
    #
    def test_update_table_properties_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestUpdateTablePropertiesWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_properties = asposewordscloud.TableProperties(alignment='Right', allow_auto_fit=False, bidi=True, bottom_padding=1.0, cell_spacing=2.0, style_options='ColumnBands')
        request = asposewordscloud.models.requests.UpdateTablePropertiesRequest(name=remote_file_name, properties=request_properties, index=1, folder=remote_data_folder)

        result = self.words_api.update_table_properties(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.properties, 'Validate UpdateTablePropertiesWithoutNodePath response')
        self.assertFalse(result.properties.allow_auto_fit, 'Validate UpdateTablePropertiesWithoutNodePath response')
        self.assertTrue(result.properties.bidi, 'Validate UpdateTablePropertiesWithoutNodePath response')
        self.assertEqual(1.0, result.properties.bottom_padding)
        self.assertEqual(2.0, result.properties.cell_spacing)

    #
    # Test for getting table row.
    #
    def test_get_table_row(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTableRow.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTableRowRequest(name=remote_file_name, table_path='tables/1', index=0, folder=remote_data_folder)

        result = self.words_api.get_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.row, 'Validate GetTableRow response')
        self.assertIsNotNone(result.row.table_cell_list, 'Validate GetTableRow response')
        self.assertEqual(2, len(result.row.table_cell_list))

    #
    # Test for getting table row online.
    #
    def test_get_table_row_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTableRowOnlineRequest(document=request_document, table_path='tables/1', index=0)

        result = self.words_api.get_table_row_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting table row.
    #
    def test_delete_table_row(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestDeleteTableRow.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableRowRequest(name=remote_file_name, table_path='tables/1', index=0, folder=remote_data_folder)

        self.words_api.delete_table_row(request)


    #
    # Test for deleting table row online.
    #
    def test_delete_table_row_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteTableRowOnlineRequest(document=request_document, table_path='tables/1', index=0)

        result = self.words_api.delete_table_row_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding row.
    #
    def test_insert_table_row(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestInsertTableRow.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_row = asposewordscloud.TableRowInsert(columns_count=5)
        request = asposewordscloud.models.requests.InsertTableRowRequest(name=remote_file_name, row=request_row, node_path='sections/0/tables/2', folder=remote_data_folder)

        result = self.words_api.insert_table_row(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.row, 'Validate InsertTableRow response')
        self.assertIsNotNone(result.row.table_cell_list, 'Validate InsertTableRow response')
        self.assertEqual(5, len(result.row.table_cell_list))

    #
    # Test for adding row online.
    #
    def test_insert_table_row_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_row = asposewordscloud.TableRowInsert(columns_count=5)
        request = asposewordscloud.models.requests.InsertTableRowOnlineRequest(document=request_document, row=request_row, node_path='sections/0/tables/2')

        result = self.words_api.insert_table_row_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting row format.
    #
    def test_get_table_row_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTableRowFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTableRowFormatRequest(name=remote_file_name, table_path='sections/0/tables/2', index=0, folder=remote_data_folder)

        result = self.words_api.get_table_row_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.row_format, 'Validate GetTableRowFormat response')
        self.assertTrue(result.row_format.allow_break_across_pages, 'Validate GetTableRowFormat response')

    #
    # Test for getting row format online.
    #
    def test_get_table_row_format_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTableRowFormatOnlineRequest(document=request_document, table_path='sections/0/tables/2', index=0)

        result = self.words_api.get_table_row_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test updating row format.
    #
    def test_update_table_row_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestUpdateTableRowFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_format = asposewordscloud.TableRowFormat(allow_break_across_pages=True, heading_format=True, height=10.0, height_rule='Exactly')
        request = asposewordscloud.models.requests.UpdateTableRowFormatRequest(name=remote_file_name, format=request_format, table_path='sections/0/tables/2', index=0, folder=remote_data_folder)

        result = self.words_api.update_table_row_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.row_format, 'Validate UpdateTableRowFormat response')
        self.assertTrue(result.row_format.allow_break_across_pages, 'Validate UpdateTableRowFormat response')
        self.assertTrue(result.row_format.heading_format, 'Validate UpdateTableRowFormat response')
        self.assertEqual(10.0, result.row_format.height)

    #
    # Test updating row format online.
    #
    def test_update_table_row_format_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_format = asposewordscloud.TableRowFormat(allow_break_across_pages=True, heading_format=True, height=10, height_rule='Auto')
        request = asposewordscloud.models.requests.UpdateTableRowFormatOnlineRequest(document=request_document, format=request_format, table_path='sections/0/tables/2', index=0)

        result = self.words_api.update_table_row_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting table cell.
    #
    def test_get_table_cell(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTableCell.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTableCellRequest(name=remote_file_name, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remote_data_folder)

        result = self.words_api.get_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.cell, 'Validate GetTableCell response')
        self.assertEqual('0.0.5.0.0', result.cell.node_id)

    #
    # Test for getting table cell online.
    #
    def test_get_table_cell_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTableCellOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)

        result = self.words_api.get_table_cell_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting cell.
    #
    def test_delete_table_cell(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestDeleteTableCell.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteTableCellRequest(name=remote_file_name, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remote_data_folder)

        self.words_api.delete_table_cell(request)


    #
    # Test for deleting cell online.
    #
    def test_delete_table_cell_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteTableCellOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)

        result = self.words_api.delete_table_cell_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding cell.
    #
    def test_insert_table_cell(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestInsertTableCell.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_cell = asposewordscloud.TableCellInsert()
        request = asposewordscloud.models.requests.InsertTableCellRequest(name=remote_file_name, cell=request_cell, table_row_path='sections/0/tables/2/rows/0', folder=remote_data_folder)

        result = self.words_api.insert_table_cell(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.cell, 'Validate InsertTableCell response')
        self.assertEqual('0.0.5.0.3', result.cell.node_id)

    #
    # Test for adding cell online.
    #
    def test_insert_table_cell_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_cell = asposewordscloud.TableCellInsert()
        request = asposewordscloud.models.requests.InsertTableCellOnlineRequest(document=request_document, cell=request_cell, table_row_path='sections/0/tables/2/rows/0')

        result = self.words_api.insert_table_cell_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting cell format.
    #
    def test_get_table_cell_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestGetTableCellFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetTableCellFormatRequest(name=remote_file_name, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remote_data_folder)

        result = self.words_api.get_table_cell_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.cell_format, 'Validate GetTableCellFormat response')
        self.assertTrue(result.cell_format.wrap_text, 'Validate GetTableCellFormat response')

    #
    # Test for getting cell format online.
    #
    def test_get_table_cell_format_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetTableCellFormatOnlineRequest(document=request_document, table_row_path='sections/0/tables/2/rows/0', index=0)

        result = self.words_api.get_table_cell_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating cell format.
    #
    def test_update_table_cell_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestUpdateTableCellFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_format = asposewordscloud.TableCellFormat(bottom_padding=5.0, fit_text=True, horizontal_merge='First', wrap_text=True)
        request = asposewordscloud.models.requests.UpdateTableCellFormatRequest(name=remote_file_name, format=request_format, table_row_path='sections/0/tables/2/rows/0', index=0, folder=remote_data_folder)

        result = self.words_api.update_table_cell_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.cell_format, 'Validate UpdateTableCellFormat response')
        self.assertEqual(5.0, result.cell_format.bottom_padding)
        self.assertTrue(result.cell_format.fit_text, 'Validate UpdateTableCellFormat response')
        self.assertTrue(result.cell_format.wrap_text, 'Validate UpdateTableCellFormat response')

    #
    # Test for updating cell format online.
    #
    def test_update_table_cell_format_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_format = asposewordscloud.TableCellFormat(bottom_padding=5, fit_text=True, horizontal_merge='First', wrap_text=True)
        request = asposewordscloud.models.requests.UpdateTableCellFormatOnlineRequest(document=request_document, format=request_format, table_row_path='sections/0/tables/2/rows/0', index=0)

        result = self.words_api.update_table_cell_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for table rendering.
    #
    def test_render_table(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestRenderTable.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderTableRequest(name=remote_file_name, format='png', index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.render_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for table rendering.
    #
    def test_render_table_online(self):
        local_file = 'DocumentElements/Tables/TablesGet.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.RenderTableOnlineRequest(document=request_document, format='png', index=0, node_path='')

        result = self.words_api.render_table_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for table rendering without node path.
    #
    def test_render_table_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Tables'
        local_file = 'DocumentElements/Tables/TablesGet.docx'
        remote_file_name = 'TestRenderTableWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderTableRequest(name=remote_file_name, format='png', index=0, folder=remote_data_folder)

        result = self.words_api.render_table(request)
        self.assertIsNotNone(result, 'Error has occurred.')

