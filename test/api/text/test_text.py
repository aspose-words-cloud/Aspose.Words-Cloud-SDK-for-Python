# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_text.py">
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
# Example of how to work with macros.
#
class TestText(BaseTestContext):
    #
    # Test for replacing text.
    #
    def test_replace_text(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Text'
        remote_file_name = 'TestReplaceText.docx'
        local_file = 'Common/test_multi_pages.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_replace_text = asposewordscloud.ReplaceTextParameters(old_value='Testing', new_value='Aspose testing', is_match_case=True, is_match_whole_word=False, is_old_value_regex=False)
        request = asposewordscloud.models.requests.ReplaceTextRequest(name=remote_file_name, replace_text=request_replace_text, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.replace_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertEqual(3, result.matches)

    #
    # Test for replacing text online.
    #
    def test_replace_text_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_replace_text = asposewordscloud.ReplaceTextParameters(old_value='aspose', new_value='aspose new', is_match_case=True, is_match_whole_word=False, is_old_value_regex=False)
        request = asposewordscloud.models.requests.ReplaceTextOnlineRequest(document=request_document, replace_text=request_replace_text)

        result = self.words_api.replace_text_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for searching.
    #
    def test_search(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Text'
        remote_file_name = 'TestSearch.docx'
        local_file = 'DocumentElements/Text/SampleWordDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.SearchRequest(name=remote_file_name, pattern='aspose', folder=remote_data_folder)

        result = self.words_api.search(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.search_results, 'Validate Search response')
        self.assertIsNotNone(result.search_results.results_list, 'Validate Search response')
        self.assertEqual(23, len(result.search_results.results_list))
        self.assertIsNotNone(result.search_results.results_list[0].range_start, 'Validate Search response')
        self.assertEqual(65, result.search_results.results_list[0].range_start.offset)

    #
    # Test for searching online.
    #
    def test_search_online(self):
        local_file = 'DocumentElements/Text/SampleWordDocument.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.SearchOnlineRequest(document=request_document, pattern='aspose')

        result = self.words_api.search_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

