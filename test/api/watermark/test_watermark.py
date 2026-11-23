# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_watermark.py">
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
# Example of how to work with watermarks.
#
class TestWatermark(BaseTestContext):
    #
    # Test for adding watermark text.
    #
    def test_insert_watermark_text(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Watermark'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertWatermarkText.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_watermark_data = asposewordscloud.WatermarkDataText(text='watermark text')
        request = asposewordscloud.models.requests.InsertWatermarkRequest(name=remote_file_name, watermark_data=request_watermark_data, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.insert_watermark(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate InsertWatermarkText response')

    #
    # Test for adding watermark text online.
    #
    def test_insert_watermark_text_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_watermark_data = asposewordscloud.WatermarkDataText(text='watermark text')
        request = asposewordscloud.models.requests.InsertWatermarkOnlineRequest(document=request_document, watermark_data=request_watermark_data)

        result = self.words_api.insert_watermark_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding watermark text.
    #
    def test_insert_watermark_image(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Watermark'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertWatermarkImage.docx'
        remote_image_path = remote_data_folder + '/TestInsertWatermarkImage.png'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))
        self.upload_file(remote_image_path, self.open_file(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'))

        request_watermark_data_image = asposewordscloud.FileReference.fromRemoteFilePath(remote_image_path)
        request_watermark_data = asposewordscloud.WatermarkDataImage(image=request_watermark_data_image)
        request = asposewordscloud.models.requests.InsertWatermarkRequest(name=remote_file_name, watermark_data=request_watermark_data, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.insert_watermark(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate InsertWatermarkImage response')

    #
    # Test for adding watermark text online.
    #
    def test_insert_watermark_image_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_watermark_data_image_stream = self.open_file(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request_watermark_data_image = asposewordscloud.FileReference.fromLocalFileContent(request_watermark_data_image_stream)
        request_watermark_data = asposewordscloud.WatermarkDataImage(image=request_watermark_data_image)
        request = asposewordscloud.models.requests.InsertWatermarkOnlineRequest(document=request_document, watermark_data=request_watermark_data)

        result = self.words_api.insert_watermark_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding watermark image.
    #
    def test_insert_watermark_image_deprecated(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Watermark'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertWatermarkImage.docx'
        remote_image_path = remote_data_folder + '/TestInsertWatermarkImage.png'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))
        self.upload_file(remote_image_path, self.open_file(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb'))

        request = asposewordscloud.models.requests.InsertWatermarkImageRequest(name=remote_file_name, image_file=None, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name, image=remote_image_path)

        result = self.words_api.insert_watermark_image(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate InsertWatermarkImageDeprecated response')
        self.assertEqual('TestInsertWatermarkImage.docx', result.document.file_name)

    #
    # Test for adding watermark image online.
    #
    def test_insert_watermark_image_deprecated_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_image_file = self.open_file(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.InsertWatermarkImageOnlineRequest(document=request_document, image_file=request_image_file)

        result = self.words_api.insert_watermark_image_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding watermark text.
    #
    def test_insert_watermark_text_deprecated(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Watermark'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertWatermarkText.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_watermark_text = asposewordscloud.WatermarkText(text='This is the text', rotation_angle=90.0)
        request = asposewordscloud.models.requests.InsertWatermarkTextRequest(name=remote_file_name, watermark_text=request_watermark_text, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.insert_watermark_text(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate InsertWatermarkTextDeprecated response')
        self.assertEqual('TestInsertWatermarkText.docx', result.document.file_name)

    #
    # Test for adding watermark text online.
    #
    def test_insert_watermark_text_deprecated_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_watermark_text = asposewordscloud.WatermarkText(text='This is the text', rotation_angle=90)
        request = asposewordscloud.models.requests.InsertWatermarkTextOnlineRequest(document=request_document, watermark_text=request_watermark_text)

        result = self.words_api.insert_watermark_text_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting watermark.
    #
    def test_delete_watermark(self):
        remote_data_folder = self.remote_test_folder + '/DocumentActions/Watermark'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteWatermark.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteWatermarkRequest(name=remote_file_name, folder=remote_data_folder, dest_file_name=self.remote_test_out + '/' + remote_file_name)

        result = self.words_api.delete_watermark(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.document, 'Validate DeleteWatermark response')
        self.assertEqual('TestDeleteWatermark.docx', result.document.file_name)

    #
    # Test for deleting watermark online.
    #
    def test_delete_watermark_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteWatermarkOnlineRequest(document=request_document)

        result = self.words_api.delete_watermark_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

