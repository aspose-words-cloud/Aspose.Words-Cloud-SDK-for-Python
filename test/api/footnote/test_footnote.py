# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_footnote.py">
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
# Example of how to work with footnotes.
#
class TestFootnote(BaseTestContext):
    #
    # Test for adding footnote.
    #
    def test_insert_footnote(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestInsertFootnote.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request_footnote_dto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        request = asposewordscloud.models.requests.InsertFootnoteRequest(name=remote_file_name, footnote_dto=request_footnote_dto, node_path='', folder=remote_data_folder)

        result = self.words_api.insert_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnote, 'Validate InsertFootnote response')
        self.assertEqual('0.1.7.1', result.footnote.node_id)
        self.assertEqual(' test endnote' + '\r\n', result.footnote.text)

    #
    # Test for adding footnote online.
    #
    def test_insert_footnote_online(self):
        footnote_folder = 'DocumentElements/Footnotes'

        request_document = open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb')
        request_footnote_dto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        request = asposewordscloud.models.requests.InsertFootnoteOnlineRequest(document=request_document, footnote_dto=request_footnote_dto, node_path='')

        result = self.words_api.insert_footnote_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding footnote without node path.
    #
    def test_insert_footnote_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestInsertFootnoteWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request_footnote_dto = asposewordscloud.FootnoteInsert(footnote_type='Endnote', text='test endnote')
        request = asposewordscloud.models.requests.InsertFootnoteRequest(name=remote_file_name, footnote_dto=request_footnote_dto, folder=remote_data_folder)

        result = self.words_api.insert_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnote, 'Validate InsertFootnoteWithoutNodePath response')
        self.assertEqual('0.1.7.1', result.footnote.node_id)
        self.assertEqual(' test endnote' + '\r\n', result.footnote.text)

    #
    # Test for deleting footnote.
    #
    def test_delete_footnote(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestDeleteFootnote.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFootnoteRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        self.words_api.delete_footnote(request)


    #
    # Test for deleting footnote online.
    #
    def test_delete_footnote_online(self):
        footnote_folder = 'DocumentElements/Footnotes'

        request_document = open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb')
        request = asposewordscloud.models.requests.DeleteFootnoteOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.delete_footnote_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting footnote without node path.
    #
    def test_delete_footnote_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestDeleteFootnoteWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.DeleteFootnoteRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        self.words_api.delete_footnote(request)


    #
    # Test for getting footnotes.
    #
    def test_get_footnotes(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestGetFootnotes.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnotesRequest(name=remote_file_name, node_path='', folder=remote_data_folder)

        result = self.words_api.get_footnotes(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnotes, 'Validate GetFootnotes response')
        self.assertIsNotNone(result.footnotes.list, 'Validate GetFootnotes response')
        self.assertEqual(6, len(result.footnotes.list))
        self.assertEqual(' Footnote 1.' + '\r\n', result.footnotes.list[0].text)

    #
    # Test for getting footnotes online.
    #
    def test_get_footnotes_online(self):
        footnote_folder = 'DocumentElements/Footnotes'

        request_document = open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb')
        request = asposewordscloud.models.requests.GetFootnotesOnlineRequest(document=request_document, node_path='')

        result = self.words_api.get_footnotes_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting footnotes without node path.
    #
    def test_get_footnotes_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestGetFootnotesWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnotesRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_footnotes(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnotes, 'Validate GetFootnotesWithoutNodePath response')
        self.assertIsNotNone(result.footnotes.list, 'Validate GetFootnotesWithoutNodePath response')
        self.assertEqual(6, len(result.footnotes.list))
        self.assertEqual(' Footnote 1.' + '\r\n', result.footnotes.list[0].text)

    #
    # Test for getting footnote.
    #
    def test_get_footnote(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestGetFootnote.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnoteRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.get_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnote, 'Validate GetFootnote response')
        self.assertEqual(' Footnote 1.' + '\r\n', result.footnote.text)

    #
    # Test for getting footnote online.
    #
    def test_get_footnote_online(self):
        footnote_folder = 'DocumentElements/Footnotes'

        request_document = open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb')
        request = asposewordscloud.models.requests.GetFootnoteOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.get_footnote_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting footnote without node path.
    #
    def test_get_footnote_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestGetFootnoteWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request = asposewordscloud.models.requests.GetFootnoteRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnote, 'Validate GetFootnoteWithoutNodePath response')
        self.assertEqual(' Footnote 1.' + '\r\n', result.footnote.text)

    #
    # Test for updating footnote.
    #
    def test_update_footnote(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestUpdateFootnote.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request_footnote_dto = asposewordscloud.FootnoteUpdate(text='new text is here')
        request = asposewordscloud.models.requests.UpdateFootnoteRequest(name=remote_file_name, index=0, footnote_dto=request_footnote_dto, node_path='', folder=remote_data_folder)

        result = self.words_api.update_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnote, 'Validate UpdateFootnote response')
        self.assertEqual(' new text is here' + '\r\n', result.footnote.text)

    #
    # Test for updating footnote online.
    #
    def test_update_footnote_online(self):
        footnote_folder = 'DocumentElements/Footnotes'

        request_document = open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb')
        request_footnote_dto = asposewordscloud.FootnoteUpdate(text='new text is here')
        request = asposewordscloud.models.requests.UpdateFootnoteOnlineRequest(document=request_document, index=0, footnote_dto=request_footnote_dto, node_path='')

        result = self.words_api.update_footnote_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating footnote without node path.
    #
    def test_update_footnote_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Footnotes'
        footnote_folder = 'DocumentElements/Footnotes'
        remote_file_name = 'TestUpdateFootnoteWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, footnote_folder + '/Footnote.doc'), 'rb'))

        request_footnote_dto = asposewordscloud.FootnoteUpdate(text='new text is here')
        request = asposewordscloud.models.requests.UpdateFootnoteRequest(name=remote_file_name, index=0, footnote_dto=request_footnote_dto, folder=remote_data_folder)

        result = self.words_api.update_footnote(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.footnote, 'Validate UpdateFootnoteWithoutNodePath response')
        self.assertEqual(' new text is here' + '\r\n', result.footnote.text)
