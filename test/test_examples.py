# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="TestExamples.py">
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
import asposewordscloud
import asposewordscloud.models.requests
from asposewordscloud.rest import ApiException
from shutil import copyfile
from test.base_test_context import BaseTestContext

class TestExamples(BaseTestContext):
    def setUp(self):
        super().setUp()
        self.words_api.upload_file(asposewordscloud.models.requests.UploadFileRequest(
            self.open_file(os.path.join('ExamplesData', 'test_doc.docx')),
            'test_doc.docx'
        ))


    def test_accept_all_revisions(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        file_name= 'test_doc.docx'

        # Upload original document to cloud storage.
        my_var1 = self.open_file(os.path.join(documents_dir, file_name), 'rb')
        my_var2 = file_name
        upload_file_request = asposewordscloud.models.requests.UploadFileRequest(file_content=my_var1, path=my_var2)
        words_api.upload_file(upload_file_request)

        # Calls AcceptAllRevisions method for document in cloud.
        my_var3 = file_name
        request = asposewordscloud.models.requests.AcceptAllRevisionsRequest(name=my_var3)
        words_api.accept_all_revisions(request)

    def test_accept_all_revisions_online(self):
        documents_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/../ExamplesData")
        words_api = self.words_api
        file_name= 'test_doc.docx'

        # Calls AcceptAllRevisionsOnline method for document in cloud.
        request_document = self.open_file(os.path.join(documents_dir, file_name), 'rb')
        request = asposewordscloud.models.requests.AcceptAllRevisionsOnlineRequest(document=request_document)
        accept_all_revisions_online_result = words_api.accept_all_revisions_online(request)
        open('test_result.docx','wb').write(list(accept_all_revisions_online_result.document.values())[0])