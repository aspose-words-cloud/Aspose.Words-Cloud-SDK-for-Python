# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_batch.py">
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

from urllib3 import request
import asposewordscloud.models
import os
import asposewordscloud.models.requests
from test.base_test_context import BaseTestContext


class TestBatch(BaseTestContext):

    test_folder = 'DocumentElements/Bookmarks'

    #
    # Test for batch request
    #
    def test_batch(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestBatchParagraphs.docx'
        file = self.open_file(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb')
        remote_path = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_folder = os.path.join(self.remote_test_folder, self.test_folder)
        paragraph = asposewordscloud.models.ParagraphInsert(text="This is a new paragraph for your document")
        request0 = asposewordscloud.models.requests.UploadFileRequest(file, remote_path)
        request1 = asposewordscloud.models.requests.GetParagraphsRequest(name=remote_name, node_path="sections/0", folder=remote_folder)
        request2 = asposewordscloud.models.requests.GetParagraphRequest(name=remote_name, index=0, node_path="sections/0", folder=remote_folder)
        request3 = asposewordscloud.models.requests.InsertParagraphRequest(name=remote_name, paragraph=paragraph, node_path="sections/0", folder=remote_folder)
        request4 = asposewordscloud.models.requests.DeleteParagraphRequest(name=remote_name, index=0, node_path="", folder=remote_folder)

        reportingFolder = 'DocumentActions/Reporting'
        localDocumentFile = 'ReportTemplate.docx'
        localDataFile = self.open_file(os.path.join(self.local_test_folder, reportingFolder + '/ReportData.json'), 'r').read()
        requestReportEngineSettings = asposewordscloud.ReportEngineSettings(data_source_type='Json', data_source_name='persons')
        request5 = asposewordscloud.models.requests.BuildReportOnlineRequest(
            template=self.open_file(os.path.join(self.local_test_folder, reportingFolder + '/' + localDocumentFile), 'rb'),
            data=localDataFile, report_engine_settings=requestReportEngineSettings)

        self.words_api.upload_file(request0)

        batch_request1 = asposewordscloud.models.requests.BatchRequest(request = request1)
        batch_request2 = asposewordscloud.models.requests.BatchRequest(request = request2)
        batch_request3 = asposewordscloud.models.requests.BatchRequest(request = request3)
        batch_request4 = asposewordscloud.models.requests.BatchRequest(request = request4)
        batch_request5 = asposewordscloud.models.requests.BatchRequest(request = request5)

        result = self.words_api.batch(batch_request1, batch_request2, batch_request3, batch_request4, batch_request5)
        self.assertEqual(len(result), 5)
        self.assertIsInstance(result[0], asposewordscloud.ParagraphLinkCollectionResponse)
        self.assertIsInstance(result[1], asposewordscloud.ParagraphResponse)
        self.assertIsInstance(result[2], asposewordscloud.ParagraphResponse)
        self.assertIsNone(result[3])
        self.assertIsInstance(result[4], bytes)

    #
    # Test for batch request without returning of intermediate results
    #
    def test_batch_without_intermidiate_results(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'TestBatchParagraphs.docx'
        file = self.open_file(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb')
        remote_path = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_folder = os.path.join(self.remote_test_folder, self.test_folder)
        paragraph = asposewordscloud.models.ParagraphInsert(text="This is a new paragraph for your document")
        request0 = asposewordscloud.models.requests.UploadFileRequest(file, remote_path)
        request1 = asposewordscloud.models.requests.GetParagraphsRequest(name=remote_name, node_path="sections/0", folder=remote_folder)
        request2 = asposewordscloud.models.requests.GetParagraphRequest(name=remote_name, index=0, node_path="sections/0", folder=remote_folder)
        request3 = asposewordscloud.models.requests.InsertParagraphRequest(name=remote_name, paragraph=paragraph, node_path="sections/0", folder=remote_folder)
        request4 = asposewordscloud.models.requests.DeleteParagraphRequest(name=remote_name, index=0, node_path="", folder=remote_folder)

        reportingFolder = 'DocumentActions/Reporting'
        localDocumentFile = 'ReportTemplate.docx'
        localDataFile = self.open_file(os.path.join(self.local_test_folder, reportingFolder + '/ReportData.json'), 'r').read()
        requestReportEngineSettings = asposewordscloud.ReportEngineSettings(data_source_type='Json', data_source_name='persons')
        request5 = asposewordscloud.models.requests.BuildReportOnlineRequest(
            template=self.open_file(os.path.join(self.local_test_folder, reportingFolder + '/' + localDocumentFile), 'rb'),
            data=localDataFile, report_engine_settings=requestReportEngineSettings)

        self.words_api.upload_file(request0)

        batch_request1 = asposewordscloud.models.requests.BatchRequest(request = request1)
        batch_request2 = asposewordscloud.models.requests.BatchRequest(request = request2)
        batch_request3 = asposewordscloud.models.requests.BatchRequest(request = request3)
        batch_request4 = asposewordscloud.models.requests.BatchRequest(request = request4)
        batch_request5 = asposewordscloud.models.requests.BatchRequest(request = request5)

        result = self.words_api.batch_with_options(True, batch_request1, batch_request2, batch_request3, batch_request4, batch_request5)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], bytes)

    #
    # Test for a batch with depend on feature
    #
    def test_batch_with_reversed_order(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'test_batch_with_reversed_order.docx'
        file = self.open_file(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb')
        remote_path = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_folder = os.path.join(self.remote_test_folder, self.test_folder)

        self.upload_file(remote_folder + '/' + remote_name, file)

        request1 =  asposewordscloud.models.requests.GetParagraphsRequest(name=remote_name, node_path="sections/0", folder=remote_folder)
        request2 = asposewordscloud.models.requests.GetParagraphRequest(name=remote_name, index=0, node_path="sections/0", folder=remote_folder)

        batch_request1 = asposewordscloud.models.requests.BatchRequest(request=request1)
        batch_request2 = asposewordscloud.models.requests.BatchRequest(request=request2)
        batch_request1.depends_on(batch_request2)

        result = self.words_api.batch(batch_request1, batch_request2)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], asposewordscloud.models.ParagraphResponse)
        self.assertIsInstance(result[1], asposewordscloud.models.ParagraphLinkCollectionResponse)


    #
    # Test for a batch with resultOf feature
    #
    def test_batch_with_result_of(self):
        filename = 'test_multi_pages.docx'
        remote_name = 'test_batch_with_result_of.docx'
        file = self.open_file(os.path.join(self.local_test_folder, self.local_common_folder, filename), 'rb')
        remote_path = os.path.join(self.remote_test_folder, self.test_folder, remote_name)
        remote_folder = os.path.join(self.remote_test_folder, self.test_folder)

        self.upload_file(remote_folder + '/' + remote_name, file)

        request1 =  asposewordscloud.models.requests.GetDocumentWithFormatRequest(name=remote_name, format='docx', folder=remote_folder)
        batch_request1 = asposewordscloud.models.requests.BatchRequest(request=request1)

        request2 = asposewordscloud.models.requests.DeleteCommentsOnlineRequest(document=batch_request1.use_as_source())
        batch_request2 = asposewordscloud.models.requests.BatchRequest(request=request2)

        batch_request2.depends_on(batch_request1)

        result = self.words_api.batch(batch_request1, batch_request2)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[1], dict)