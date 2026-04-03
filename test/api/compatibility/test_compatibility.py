# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_compatibility.py">
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
# Example of how to work with compatibility options.
#
class TestCompatibility(BaseTestContext):
    #
    # Test for optimize document to specific MS Word version.
    #
    def test_optimize_document(self):
        remote_data_folder = self.remote_test_folder + '/Compatibility'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestOptimizeDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_options = asposewordscloud.OptimizationOptions(ms_word_version='Word2002')
        request = asposewordscloud.models.requests.OptimizeDocumentRequest(name=remote_file_name, options=request_options, folder=remote_data_folder)

        self.words_api.optimize_document(request)


    #
    # Test for optimize document to specific MS Word version.
    #
    def test_optimize_document_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_options = asposewordscloud.OptimizationOptions(ms_word_version='Word2002')
        request = asposewordscloud.models.requests.OptimizeDocumentOnlineRequest(document=request_document, options=request_options)

        result = self.words_api.optimize_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

