# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_paragraph.py">
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
# Example of how to work with paragraph.
#
class TestParagraph(BaseTestContext):
    #
    # Test for getting paragraph.
    #
    def test_get_document_paragraph_by_index(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphByIndex.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphRequest(name=remote_file_name, index=0, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate GetDocumentParagraphByIndex response')
        self.assertEqual('0.0.0', result.paragraph.node_id)

    #
    # Test for getting paragraph online.
    #
    def test_get_document_paragraph_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetParagraphOnlineRequest(document=request_document, index=0, node_path='sections/0')

        result = self.words_api.get_paragraph_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph without node path.
    #
    def test_get_document_paragraph_by_index_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphByIndexWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate GetDocumentParagraphByIndexWithoutNodePath response')
        self.assertEqual('0.0.0', result.paragraph.node_id)

    #
    # Test for getting all paragraphs.
    #
    def test_get_document_paragraphs(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphsRequest(name=remote_file_name, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_paragraphs(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraphs, 'Validate GetDocumentParagraphs response')
        self.assertIsNotNone(result.paragraphs.paragraph_link_list, 'Validate GetDocumentParagraphs response')
        self.assertEqual(15, len(result.paragraphs.paragraph_link_list))
        self.assertEqual('Page 1 of 3', result.paragraphs.paragraph_link_list[0].text)

    #
    # Test for getting all paragraphs online.
    #
    def test_get_document_paragraphs_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetParagraphsOnlineRequest(document=request_document, node_path='sections/0')

        result = self.words_api.get_paragraphs_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting all paragraphs without node path.
    #
    def test_get_document_paragraphs_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_paragraphs(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraphs, 'Validate GetDocumentParagraphsWithoutNodePath response')
        self.assertIsNotNone(result.paragraphs.paragraph_link_list, 'Validate GetDocumentParagraphsWithoutNodePath response')
        self.assertEqual(15, len(result.paragraphs.paragraph_link_list))
        self.assertEqual('Page 1 of 3', result.paragraphs.paragraph_link_list[0].text)

    #
    # Test for getting paragraph run.
    #
    def test_get_document_paragraph_run(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphRun.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetRunRequest(name=remote_file_name, paragraph_path='paragraphs/0', index=0, folder=remote_data_folder)

        result = self.words_api.get_run(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.run, 'Validate GetDocumentParagraphRun response')
        self.assertEqual('Page ', result.run.text)

    #
    # Test for getting paragraph run online.
    #
    def test_get_document_paragraph_run_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetRunOnlineRequest(document=request_document, paragraph_path='paragraphs/0', index=0)

        result = self.words_api.get_run_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph run font.
    #
    def test_get_document_paragraph_run_font(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphRunFont.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetRunFontRequest(name=remote_file_name, paragraph_path='paragraphs/0', index=0, folder=remote_data_folder)

        result = self.words_api.get_run_font(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.font, 'Validate GetDocumentParagraphRunFont response')
        self.assertEqual('Times New Roman', result.font.name)

    #
    # Test for getting paragraph run font online.
    #
    def test_get_document_paragraph_run_font_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetRunFontOnlineRequest(document=request_document, paragraph_path='paragraphs/0', index=0)

        result = self.words_api.get_run_font_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph runs.
    #
    def test_get_paragraph_runs(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetParagraphRuns.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetRunsRequest(name=remote_file_name, paragraph_path='sections/0/paragraphs/0', folder=remote_data_folder)

        result = self.words_api.get_runs(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.runs, 'Validate GetParagraphRuns response')
        self.assertIsNotNone(result.runs.list, 'Validate GetParagraphRuns response')
        self.assertEqual(6, len(result.runs.list))
        self.assertEqual('Page ', result.runs.list[0].text)

    #
    # Test for getting paragraph runs online.
    #
    def test_get_paragraph_runs_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetRunsOnlineRequest(document=request_document, paragraph_path='sections/0/paragraphs/0')

        result = self.words_api.get_runs_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating paragraph run font.
    #
    def test_update_run_font(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestUpdateRunFont.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_font_dto = asposewordscloud.Font(bold=True)
        request = asposewordscloud.models.requests.UpdateRunFontRequest(name=remote_file_name, font_dto=request_font_dto, paragraph_path='paragraphs/0', index=0, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.update_run_font(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.font, 'Validate UpdateRunFont response')
        self.assertTrue(result.font.bold, 'Validate UpdateRunFont response')

    #
    # Test for updating paragraph run font online.
    #
    def test_update_run_font_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_font_dto = asposewordscloud.Font(bold=True)
        request = asposewordscloud.models.requests.UpdateRunFontOnlineRequest(document=request_document, font_dto=request_font_dto, paragraph_path='paragraphs/0', index=0)

        result = self.words_api.update_run_font_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding paragraph.
    #
    def test_insert_paragraph(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertParagraph.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_paragraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        request = asposewordscloud.models.requests.InsertParagraphRequest(name=remote_file_name, paragraph=request_paragraph, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.insert_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate InsertParagraph response')
        self.assertEqual('0.3.8', result.paragraph.node_id)

    #
    # Test for adding paragraph online.
    #
    def test_insert_paragraph_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_paragraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        request = asposewordscloud.models.requests.InsertParagraphOnlineRequest(document=request_document, paragraph=request_paragraph, node_path='sections/0')

        result = self.words_api.insert_paragraph_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding paragraph without node path.
    #
    def test_insert_paragraph_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertParagraphWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_paragraph = asposewordscloud.ParagraphInsert(text='This is a new paragraph for your document')
        request = asposewordscloud.models.requests.InsertParagraphRequest(name=remote_file_name, paragraph=request_paragraph, folder=remote_data_folder)

        result = self.words_api.insert_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph, 'Validate InsertParagraphWithoutNodePath response')
        self.assertEqual('0.3.8', result.paragraph.node_id)

    #
    # Test for paragraph rendering.
    #
    def test_render_paragraph(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestRenderParagraph.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderParagraphRequest(name=remote_file_name, format='png', index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.render_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for paragraph rendering.
    #
    def test_render_paragraph_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.RenderParagraphOnlineRequest(document=request_document, format='png', index=0, node_path='')

        result = self.words_api.render_paragraph_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for paragraph rendering without node path.
    #
    def test_render_paragraph_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestRenderParagraphWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderParagraphRequest(name=remote_file_name, format='png', index=0, folder=remote_data_folder)

        result = self.words_api.render_paragraph(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph format settings.
    #
    def test_get_paragraph_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphFormatRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.get_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph_format, 'Validate GetParagraphFormat response')
        self.assertEqual('Normal', result.paragraph_format.style_name)

    #
    # Test for getting paragraph format settings online.
    #
    def test_get_paragraph_format_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetParagraphFormatOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.get_paragraph_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph format settings without node path.
    #
    def test_get_paragraph_format_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphFormatRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph_format, 'Validate GetParagraphFormatWithoutNodePath response')
        self.assertEqual('Normal', result.paragraph_format.style_name)

    #
    # Test for updating  paragraph format settings.
    #
    def test_update_paragraph_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentParagraphs.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_paragraph_format_dto = asposewordscloud.ParagraphFormatUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateParagraphFormatRequest(name=remote_file_name, index=0, paragraph_format_dto=request_paragraph_format_dto, node_path='', folder=remote_data_folder)

        result = self.words_api.update_paragraph_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.paragraph_format, 'Validate UpdateParagraphFormat response')


    #
    # Test for updating  paragraph format settings online.
    #
    def test_update_paragraph_format_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_paragraph_format_dto = asposewordscloud.ParagraphFormatUpdate(alignment='Right')
        request = asposewordscloud.models.requests.UpdateParagraphFormatOnlineRequest(document=request_document, index=0, paragraph_format_dto=request_paragraph_format_dto, node_path='')

        result = self.words_api.update_paragraph_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting  a paragraph.
    #
    def test_delete_paragraph(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteParagraph.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        self.words_api.delete_paragraph(request)


    #
    # Test for deleting  a paragraph online.
    #
    def test_delete_paragraph_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteParagraphOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.delete_paragraph_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting  a paragraph without node path.
    #
    def test_delete_paragraph_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteParagraphWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        self.words_api.delete_paragraph(request)


    #
    # Test for getting paragraph list format.
    #
    def test_get_paragraph_list_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        list_folder = 'DocumentElements/ParagraphListFormat'
        remote_file_name = 'TestParagraphGetListFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, list_folder + '/ParagraphGetListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.get_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate GetParagraphListFormat response')
        self.assertEqual(1, result.list_format.list_id)

    #
    # Test for getting paragraph list format online.
    #
    def test_get_paragraph_list_format_online(self):
        list_folder = 'DocumentElements/ParagraphListFormat'

        request_document = open(os.path.join(self.local_test_folder, list_folder + '/ParagraphGetListFormat.doc'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphListFormatOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.get_paragraph_list_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph list format without node path.
    #
    def test_get_paragraph_list_format_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        list_folder = 'DocumentElements/ParagraphListFormat'
        remote_file_name = 'TestParagraphGetListFormatWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, list_folder + '/ParagraphGetListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphListFormatRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate GetParagraphListFormatWithoutNodePath response')
        self.assertEqual(1, result.list_format.list_id)

    #
    # Test for updating paragraph list format.
    #
    def test_update_paragraph_list_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        list_folder = 'DocumentElements/ParagraphListFormat'
        remote_file_name = 'TestUpdateParagraphListFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, list_folder + '/ParagraphUpdateListFormat.doc'), 'rb'))

        request_list_format_dto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name=remote_file_name, index=0, list_format_dto=request_list_format_dto, node_path='', folder=remote_data_folder)

        result = self.words_api.update_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate UpdateParagraphListFormat response')
        self.assertEqual(2, result.list_format.list_id)

    #
    # Test for updating paragraph list format online.
    #
    def test_update_paragraph_list_format_online(self):
        list_folder = 'DocumentElements/ParagraphListFormat'

        request_document = open(os.path.join(self.local_test_folder, list_folder + '/ParagraphUpdateListFormat.doc'), 'rb')
        request_list_format_dto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatOnlineRequest(document=request_document, list_format_dto=request_list_format_dto, index=0, node_path='')

        result = self.words_api.update_paragraph_list_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating paragraph list format without node path.
    #
    def test_update_paragraph_list_format_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        list_folder = 'DocumentElements/ParagraphListFormat'
        remote_file_name = 'TestUpdateParagraphListFormatWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, list_folder + '/ParagraphUpdateListFormat.doc'), 'rb'))

        request_list_format_dto = asposewordscloud.ListFormatUpdate(list_id=2)
        request = asposewordscloud.models.requests.UpdateParagraphListFormatRequest(name=remote_file_name, index=0, list_format_dto=request_list_format_dto, folder=remote_data_folder)

        result = self.words_api.update_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.list_format, 'Validate UpdateParagraphListFormatWithoutNodePath response')
        self.assertEqual(2, result.list_format.list_id)

    #
    # Test for deleting paragraph list format.
    #
    def test_delete_paragraph_list_format(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        list_folder = 'DocumentElements/ParagraphListFormat'
        remote_file_name = 'TestDeleteParagraphListFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, list_folder + '/ParagraphDeleteListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.delete_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting paragraph list format online.
    #
    def test_delete_paragraph_list_format_online(self):
        list_folder = 'DocumentElements/ParagraphListFormat'

        request_document = open(os.path.join(self.local_test_folder, list_folder + '/ParagraphDeleteListFormat.doc'), 'rb')
        request = asposewordscloud.models.requests.DeleteParagraphListFormatOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.delete_paragraph_list_format_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting paragraph list format without node path.
    #
    def test_delete_paragraph_list_format_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        list_folder = 'DocumentElements/ParagraphListFormat'
        remote_file_name = 'TestDeleteParagraphListFormatWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, list_folder + '/ParagraphDeleteListFormat.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphListFormatRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.delete_paragraph_list_format(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph tab stops.
    #
    def test_get_paragraph_tab_stops(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestGetParagraphTabStops.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.get_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate GetParagraphTabStops response')
        self.assertEqual(2, len(result.tab_stops))
        self.assertEqual(72.0, result.tab_stops[0].position)

    #
    # Test for getting paragraph tab stops online.
    #
    def test_get_paragraph_tab_stops_online(self):
        tab_stop_folder = 'DocumentElements/Paragraphs'

        request_document = open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb')
        request = asposewordscloud.models.requests.GetParagraphTabStopsOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.get_paragraph_tab_stops_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting paragraph tab stops without node path.
    #
    def test_get_paragraph_tab_stops_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestGetParagraphTabStopsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.GetParagraphTabStopsRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate GetParagraphTabStopsWithoutNodePath response')
        self.assertEqual(2, len(result.tab_stops))
        self.assertEqual(72.0, result.tab_stops[0].position)

    #
    # Test for inserting paragraph tab stop.
    #
    def test_insert_paragraph_tab_stops(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestInsertOrUpdateParagraphTabStop.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request_tab_stop_insert_dto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=100.0)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name=remote_file_name, index=0, tab_stop_insert_dto=request_tab_stop_insert_dto, node_path='', folder=remote_data_folder)

        result = self.words_api.insert_or_update_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate InsertParagraphTabStops response')
        self.assertEqual(3, len(result.tab_stops))
        self.assertEqual(100.0, result.tab_stops[1].position)



    #
    # Test for inserting paragraph tab stop online.
    #
    def test_insert_paragraph_tab_stops_online(self):
        tab_stop_folder = 'DocumentElements/Paragraphs'

        request_document = open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb')
        request_tab_stop_insert_dto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=72)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopOnlineRequest(document=request_document, tab_stop_insert_dto=request_tab_stop_insert_dto, index=0, node_path='')

        result = self.words_api.insert_or_update_paragraph_tab_stop_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting paragraph tab stop without node path.
    #
    def test_insert_paragraph_tab_stops_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestInsertOrUpdateParagraphTabStopWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request_tab_stop_insert_dto = asposewordscloud.TabStopInsert(alignment='Left', leader='None', position=100.0)
        request = asposewordscloud.models.requests.InsertOrUpdateParagraphTabStopRequest(name=remote_file_name, index=0, tab_stop_insert_dto=request_tab_stop_insert_dto, folder=remote_data_folder)

        result = self.words_api.insert_or_update_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate InsertParagraphTabStopsWithoutNodePath response')
        self.assertEqual(3, len(result.tab_stops))
        self.assertEqual(100.0, result.tab_stops[1].position)



    #
    # Test for deleting all paragraph tab stops.
    #
    def test_delete_all_paragraph_tab_stops(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestDeleteAllParagraphTabStops.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.delete_all_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteAllParagraphTabStops response')
        self.assertEqual(0, len(result.tab_stops))

    #
    # Test for deleting all paragraph tab stops online.
    #
    def test_delete_all_paragraph_tab_stops_online(self):
        tab_stop_folder = 'DocumentElements/Paragraphs'

        request_document = open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb')
        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.delete_all_paragraph_tab_stops_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting all paragraph tab stops without node path.
    #
    def test_delete_all_paragraph_tab_stops_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestDeleteAllParagraphTabStopsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteAllParagraphTabStopsRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.delete_all_paragraph_tab_stops(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteAllParagraphTabStopsWithoutNodePath response')
        self.assertEqual(0, len(result.tab_stops))

    #
    # Test for deleting a tab stops.
    #
    def test_delete_paragraph_tab_stop(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestDeleteParagraphTabStop.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name=remote_file_name, position=72.0, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.delete_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteParagraphTabStop response')
        self.assertEqual(1, len(result.tab_stops))

    #
    # Test for deleting a tab stops online.
    #
    def test_delete_paragraph_tab_stop_online(self):
        tab_stop_folder = 'DocumentElements/Paragraphs'

        request_document = open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb')
        request = asposewordscloud.models.requests.DeleteParagraphTabStopOnlineRequest(document=request_document, position=72.0, index=0, node_path='')

        result = self.words_api.delete_paragraph_tab_stop_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting a tab stops without node path.
    #
    def test_delete_paragraph_tab_stop_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Paragraphs'
        tab_stop_folder = 'DocumentElements/Paragraphs'
        remote_file_name = 'TestDeleteParagraphTabStopWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, tab_stop_folder + '/ParagraphTabStops.docx'), 'rb'))

        request = asposewordscloud.models.requests.DeleteParagraphTabStopRequest(name=remote_file_name, position=72.0, index=0, folder=remote_data_folder)

        result = self.words_api.delete_paragraph_tab_stop(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.tab_stops, 'Validate DeleteParagraphTabStopWithoutNodePath response')
        self.assertEqual(1, len(result.tab_stops))
