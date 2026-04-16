# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_append_document.py">
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
# Example of how to append document.
#
class TestAppendDocument(BaseTestContext):
    #
    # Test for appending document.
    #
    def test_append_document(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/AppendDocument'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestAppendDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_document_list_document_entries0_file_reference = asposewordscloud.FileReference.fromRemoteFilePath(remote_data_folder + '/' + remote_file_name)
        request_document_list_document_entries0 = asposewordscloud.DocumentEntry(file_reference=request_document_list_document_entries0_file_reference, import_format_mode='KeepSourceFormatting')
        request_document_list_document_entries = [request_document_list_document_entries0]
        request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
        request = asposewordscloud.models.requests.AppendDocumentRequest(name=remote_file_name, document_list=request_document_list, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.append_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate AppendDocument response')
        self.assertEqual('TestAppendDocument.docx', result.document.file_name)

    #
    # Test for appending document job.
    #
    def test_append_document_job(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/AppendDocument'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestAppendDocument.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_document_list_document_entries0_file_reference = asposewordscloud.FileReference.fromRemoteFilePath(remote_data_folder + '/' + remote_file_name)
        request_document_list_document_entries0 = asposewordscloud.DocumentEntry(file_reference=request_document_list_document_entries0_file_reference, import_format_mode='KeepSourceFormatting')
        request_document_list_document_entries = [request_document_list_document_entries0]
        request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
        request = asposewordscloud.models.requests.AppendDocumentJobRequest(name=remote_file_name, document_list=request_document_list, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        job_handler = self.words_api.append_document_job(request)
        self.assertIsNotNone(job_handler, 'Error has occurred.')
        result = job_handler.wait_result(3)
        self.assertIsNotNone(result.document, 'Validate AppendDocumentJob response')
        self.assertEqual('TestAppendDocument.docx', result.document.file_name)

    #
    # Test for appending document online.
    #
    def test_append_document_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_document_list_document_entries0_file_reference_stream = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_document_list_document_entries0_file_reference = asposewordscloud.FileReference.fromLocalFileContent(request_document_list_document_entries0_file_reference_stream)
        request_document_list_document_entries0 = asposewordscloud.DocumentEntry(file_reference=request_document_list_document_entries0_file_reference, import_format_mode='KeepSourceFormatting')
        request_document_list_document_entries = [request_document_list_document_entries0]
        request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
        request = asposewordscloud.models.requests.AppendDocumentOnlineRequest(document=request_document, document_list=request_document_list)

        result = self.words_api.append_document_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for appending document online job.
    #
    def test_append_document_online_job(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_document_list_document_entries0_file_reference_stream = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_document_list_document_entries0_file_reference = asposewordscloud.FileReference.fromLocalFileContent(request_document_list_document_entries0_file_reference_stream)
        request_document_list_document_entries0 = asposewordscloud.DocumentEntry(file_reference=request_document_list_document_entries0_file_reference, import_format_mode='KeepSourceFormatting')
        request_document_list_document_entries = [request_document_list_document_entries0]
        request_document_list = asposewordscloud.DocumentEntryList(document_entries=request_document_list_document_entries)
        request = asposewordscloud.models.requests.AppendDocumentOnlineJobRequest(document=request_document, document_list=request_document_list)

        job_handler = self.words_api.append_document_online_job(request)
        self.assertIsNotNone(job_handler, 'Error has occurred.')

