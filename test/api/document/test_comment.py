# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_comment.py">
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
# Example of how to get comments from document.
#
class TestComment(BaseTestContext):
    #
    # Test for getting comment by specified comment's index.
    #
    def test_get_comment(self):
        remote_data_folder = self.remote_test_folder + '/Comments'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetComment.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetCommentRequest(name=remote_file_name, comment_index=0, folder=remote_data_folder)

        result = self.words_api.get_comment(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.comment, 'Validate GetComment response')
        self.assertEqual('Comment 1' + '\r\n\r\n', result.comment.text)

    #
    # Test for getting comment by specified comment's index online.
    #
    def test_get_comment_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetCommentOnlineRequest(document=request_document, comment_index=0)

        result = self.words_api.get_comment_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting all comments from document.
    #
    def test_get_comments(self):
        remote_data_folder = self.remote_test_folder + '/Comments'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetComments.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetCommentsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_comments(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.comments, 'Validate GetComments response')
        self.assertIsNotNone(result.comments.comment_list, 'Validate GetComments response')
        self.assertEqual(1, len(result.comments.comment_list))
        self.assertEqual('Comment 1' + '\r\n\r\n', result.comments.comment_list[0].text)

    #
    # Test for getting all comments from document online.
    #
    def test_get_comments_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetCommentsOnlineRequest(document=request_document)

        result = self.words_api.get_comments_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding comment.
    #
    def test_insert_comment(self):
        remote_data_folder = self.remote_test_folder + '/Comments'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertComment.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_comment_range_start = asposewordscloud.PositionInsideNode(node_id='0.3.0.3', offset=0)
        request_comment_range_end = asposewordscloud.PositionInsideNode(node_id='0.3.0.3', offset=0)
        request_comment = asposewordscloud.CommentInsert(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        request = asposewordscloud.models.requests.InsertCommentRequest(name=remote_file_name, comment=request_comment, folder=remote_data_folder)

        result = self.words_api.insert_comment(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.comment, 'Validate InsertComment response')
        self.assertEqual('A new Comment' + '\r\n', result.comment.text)
        self.assertIsNotNone(result.comment.range_start, 'Validate InsertComment response')
        self.assertIsNotNone(result.comment.range_start.node, 'Validate InsertComment response')
        self.assertEqual('0.3.0.4', result.comment.range_start.node.node_id)

    #
    # Test for adding comment online.
    #
    def test_insert_comment_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_comment_range_start = asposewordscloud.PositionInsideNode(node_id='0.3.0.3', offset=0)
        request_comment_range_end = asposewordscloud.PositionInsideNode(node_id='0.3.0.3', offset=0)
        request_comment = asposewordscloud.CommentInsert(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        request = asposewordscloud.models.requests.InsertCommentOnlineRequest(document=request_document, comment=request_comment)

        result = self.words_api.insert_comment_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating comment.
    #
    def test_update_comment(self):
        remote_data_folder = self.remote_test_folder + '/Comments'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestUpdateComment.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_comment_range_start = asposewordscloud.PositionInsideNode(node_id='0.3.0', offset=0)
        request_comment_range_end = asposewordscloud.PositionInsideNode(node_id='0.3.0', offset=0)
        request_comment = asposewordscloud.CommentUpdate(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        request = asposewordscloud.models.requests.UpdateCommentRequest(name=remote_file_name, comment_index=0, comment=request_comment, folder=remote_data_folder)

        result = self.words_api.update_comment(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.comment, 'Validate UpdateComment response')
        self.assertEqual('A new Comment' + '\r\n', result.comment.text)
        self.assertIsNotNone(result.comment.range_start, 'Validate UpdateComment response')
        self.assertIsNotNone(result.comment.range_start.node, 'Validate UpdateComment response')
        self.assertEqual('0.3.0.1', result.comment.range_start.node.node_id)

    #
    # Test for updating comment online.
    #
    def test_update_comment_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_comment_range_start = asposewordscloud.PositionInsideNode(node_id='0.3.0', offset=0)
        request_comment_range_end = asposewordscloud.PositionInsideNode(node_id='0.3.0', offset=0)
        request_comment = asposewordscloud.CommentUpdate(range_start=request_comment_range_start, range_end=request_comment_range_end, initial='IA', author='Imran Anwar', text='A new Comment')
        request = asposewordscloud.models.requests.UpdateCommentOnlineRequest(document=request_document, comment_index=0, comment=request_comment)

        result = self.words_api.update_comment_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for DeleteComment.
    #
    def test_delete_comment(self):
        remote_data_folder = self.remote_test_folder + '/Comments'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteComment.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteCommentRequest(name=remote_file_name, comment_index=0, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        self.words_api.delete_comment(request)


    #
    # A test for DeleteComment online.
    #
    def test_delete_comment_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteCommentOnlineRequest(document=request_document, comment_index=0)

        result = self.words_api.delete_comment_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for DeleteComments.
    #
    def test_delete_comments(self):
        remote_data_folder = self.remote_test_folder + '/Comments'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteComment.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteCommentsRequest(name=remote_file_name, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        self.words_api.delete_comments(request)


    #
    # A test for DeleteComments online.
    #
    def test_delete_comments_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteCommentsOnlineRequest(document=request_document)

        result = self.words_api.delete_comments_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

