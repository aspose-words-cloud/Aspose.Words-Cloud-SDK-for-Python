# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_run.py">
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
# Example of how to work with runs.
#
class TestRun(BaseTestContext):
    #
    # Test for updating run.
    #
    def test_update_run(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Runs'
        local_file = 'DocumentElements/Runs/Run.doc'
        remote_file_name = 'TestUpdateRun.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_run = asposewordscloud.RunUpdate(text='run with text')
        request = asposewordscloud.models.requests.UpdateRunRequest(name=remote_file_name, run=request_run, paragraph_path='paragraphs/1', index=0, folder=remote_data_folder)

        result = self.words_api.update_run(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.run, 'Validate UpdateRun response')
        self.assertEqual('run with text', result.run.text)

    #
    # Test for updating run online.
    #
    def test_update_run_online(self):
        local_file = 'DocumentElements/Runs/Run.doc'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_run = asposewordscloud.RunUpdate(text='run with text')
        request = asposewordscloud.models.requests.UpdateRunOnlineRequest(document=request_document, run=request_run, paragraph_path='paragraphs/1', index=0)

        result = self.words_api.update_run_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding run.
    #
    def test_insert_run(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Runs'
        local_file = 'DocumentElements/Runs/Run.doc'
        remote_file_name = 'TestInsertRun.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_run = asposewordscloud.RunInsert(text='run with text')
        request = asposewordscloud.models.requests.InsertRunRequest(name=remote_file_name, paragraph_path='paragraphs/1', run=request_run, folder=remote_data_folder)

        result = self.words_api.insert_run(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.run, 'Validate InsertRun response')
        self.assertEqual('run with text', result.run.text)
        self.assertEqual('0.0.1.3', result.run.node_id)

    #
    # Test for adding run online.
    #
    def test_insert_run_online(self):
        local_file = 'DocumentElements/Runs/Run.doc'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_run = asposewordscloud.RunInsert(text='run with text')
        request = asposewordscloud.models.requests.InsertRunOnlineRequest(document=request_document, paragraph_path='paragraphs/1', run=request_run)

        result = self.words_api.insert_run_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting run.
    #
    def test_delete_run(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Runs'
        local_file = 'DocumentElements/Runs/Run.doc'
        remote_file_name = 'TestDeleteRun.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteRunRequest(name=remote_file_name, paragraph_path='paragraphs/1', index=0, folder=remote_data_folder)

        self.words_api.delete_run(request)


    #
    # Test for deleting run online.
    #
    def test_delete_run_online(self):
        local_file = 'DocumentElements/Runs/Run.doc'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteRunOnlineRequest(document=request_document, paragraph_path='paragraphs/1', index=0)

        result = self.words_api.delete_run_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

