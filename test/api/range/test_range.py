# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_range.py">
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
# Example of how to work with ranges.
#
class TestRange(BaseTestContext):
    #
    # Test for getting the text from range.
    #
    def test_get_range_text(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Range'
        local_file = 'DocumentElements/Range/RangeGet.doc'
        remote_file_name = 'TestGetRangeText.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetRangeTextRequest(name=remote_file_name, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1', folder=remote_data_folder)

        result = self.words_api.get_range_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertEqual('This is HEADER ', result.text)

    #
    # Test for getting the text from range online.
    #
    def test_get_range_text_online(self):
        local_file = 'DocumentElements/Range/RangeGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetRangeTextOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')

        result = self.words_api.get_range_text_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for removing the text for range.
    #
    def test_remove_range(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Range'
        local_file = 'DocumentElements/Range/RangeGet.doc'
        remote_file_name = 'TestRemoveRange.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RemoveRangeRequest(name=remote_file_name, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1', folder=remote_data_folder)

        result = self.words_api.remove_range(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for removing the text for range online.
    #
    def test_remove_range_online(self):
        local_file = 'DocumentElements/Range/RangeGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.RemoveRangeOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_end_identifier='id0.0.1')

        result = self.words_api.remove_range_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for saving a range as a new document.
    #
    def test_save_as_range(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Range'
        local_file = 'DocumentElements/Range/RangeGet.doc'
        remote_file_name = 'TestSaveAsRange.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_document_parameters = asposewordscloud.RangeDocument(document_name=remote_data_folder + '/NewDoc.docx')
        request = asposewordscloud.models.requests.SaveAsRangeRequest(name=remote_file_name, range_start_identifier='id0.0.0', document_parameters=request_document_parameters, range_end_identifier='id0.0.1', folder=remote_data_folder)

        result = self.words_api.save_as_range(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate SaveAsRange response')
        self.assertEqual('NewDoc.docx', result.document.file_name)

    #
    # Test for saving a range as a new document online.
    #
    def test_save_as_range_online(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Range'
        local_file = 'DocumentElements/Range/RangeGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_document_parameters = asposewordscloud.RangeDocument(document_name=remote_data_folder + '/NewDoc.docx')
        request = asposewordscloud.models.requests.SaveAsRangeOnlineRequest(document=request_document, range_start_identifier='id0.0.0', document_parameters=request_document_parameters, range_end_identifier='id0.0.1')

        result = self.words_api.save_as_range_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for replacing text in range.
    #
    def test_replace_with_text(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Range'
        local_file = 'DocumentElements/Range/RangeGet.doc'
        remote_file_name = 'TestReplaceWithText.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_range_text = asposewordscloud.ReplaceRange(text='Replaced header')
        request = asposewordscloud.models.requests.ReplaceWithTextRequest(name=remote_file_name, range_start_identifier='id0.0.0', range_text=request_range_text, range_end_identifier='id0.0.1', folder=remote_data_folder)

        result = self.words_api.replace_with_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate ReplaceWithText response')
        self.assertEqual('TestReplaceWithText.docx', result.document.file_name)

    #
    # Test for replacing text in range online.
    #
    def test_replace_with_text_online(self):
        local_file = 'DocumentElements/Range/RangeGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_range_text = asposewordscloud.ReplaceRange(text='Replaced header')
        request = asposewordscloud.models.requests.ReplaceWithTextOnlineRequest(document=request_document, range_start_identifier='id0.0.0', range_text=request_range_text, range_end_identifier='id0.0.1')

        result = self.words_api.replace_with_text_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test to translate node id to node path.
    #
    def test_translate_node_id(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Range'
        local_file = 'DocumentElements/Range/RangeGet.doc'
        remote_file_name = 'TestTranslateNodeId.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.TranslateNodeIdRequest(name=remote_file_name, node_id='id0.0.0', folder=remote_data_folder)

        result = self.words_api.translate_node_id(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertEqual('sections/0/body/paragraphs/0', result.path)

    #
    # Test to translate node id to node path online.
    #
    def test_translate_node_id_online(self):
        local_file = 'DocumentElements/Range/RangeGet.doc'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.TranslateNodeIdOnlineRequest(document=request_document, node_id='id0.0.0')

        result = self.words_api.translate_node_id_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

