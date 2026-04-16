# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_convert_document.py">
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
# Example of how to convert document to one of the available formats.
#
class TestConvertDocument(BaseTestContext):
    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/ConvertDocument'
        local_name = 'test_multi_pages.docx'
        remote_name = 'TestSaveAs.docx'

        self.upload_file(remote_folder + '/' + remote_name, open(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb'))

        request_save_options_data = asposewordscloud.PdfSaveOptionsData(file_name=self.remote_test_out + '/TestSaveAs.pdf')
        request = asposewordscloud.models.requests.SaveAsRequest(name=remote_name, save_options_data=request_save_options_data, folder=remote_folder)

        result = self.words_api.save_as(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.save_result, 'Validate SaveAs response')
        self.assertIsNotNone(result.save_result.dest_document, 'Validate SaveAs response')

    #
    # Test for converting document online to one of the available formats.
    #
    def test_save_as_online(self):
        local_name = 'test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb')
        request_save_options_data = asposewordscloud.PdfSaveOptionsData(file_name=self.remote_test_out + '/TestSaveAs.pdf')
        request = asposewordscloud.models.requests.SaveAsOnlineRequest(document=request_document, save_options_data=request_save_options_data)

        result = self.words_api.save_as_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for converting document online to html with additional files like css and images.
    #
    def test_save_as_online_html_multifile(self):
        local_name = 'test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb')
        request_save_options_data = asposewordscloud.HtmlSaveOptionsData(file_name=self.remote_test_out + '/TestSaveAsHtml.html', css_style_sheet_type='External', css_style_sheet_file_name=self.remote_test_out + '/TestSaveAsHtml.css')
        request = asposewordscloud.models.requests.SaveAsOnlineRequest(document=request_document, save_options_data=request_save_options_data)

        result = self.words_api.save_as_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as_docx(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/ConvertDocument'
        local_folder = 'DocumentActions/ConvertDocument'
        local_name = '45.pdf'
        remote_name = 'TestSaveAsFromPdfToDoc.pdf'

        self.upload_file(remote_folder + '/' + remote_name, open(os.path.join(self.local_test_folder, local_folder + '/' + local_name), 'rb'))

        request_save_options_data = asposewordscloud.DocxSaveOptionsData(file_name=self.remote_test_out + '/TestSaveAsFromPdfToDoc.docx')
        request = asposewordscloud.models.requests.SaveAsRequest(name=remote_name, save_options_data=request_save_options_data, folder=remote_folder)

        result = self.words_api.save_as(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.save_result, 'Validate SaveAsDocx response')
        self.assertIsNotNone(result.save_result.dest_document, 'Validate SaveAsDocx response')

    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as_tiff(self):
        remote_folder = self.remote_test_folder + '/DocumentActions/ConvertDocument'
        local_name = 'test_multi_pages.docx'
        remote_name = 'TestSaveAsTiff.pdf'

        self.upload_file(remote_folder + '/' + remote_name, open(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb'))

        request_save_options = asposewordscloud.TiffSaveOptionsData(file_name=self.remote_test_out + '/abc.tiff')
        request = asposewordscloud.models.requests.SaveAsTiffRequest(name=remote_name, save_options=request_save_options, folder=remote_folder)

        result = self.words_api.save_as_tiff(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.save_result, 'Validate SaveAsTiff response')
        self.assertIsNotNone(result.save_result.dest_document, 'Validate SaveAsTiff response')

    #
    # Test for converting document to one of the available formats.
    #
    def test_save_as_tiff_online(self):
        local_name = 'test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, 'Common/' + local_name), 'rb')
        request_save_options = asposewordscloud.TiffSaveOptionsData(file_name=self.remote_test_out + '/abc.tiff')
        request = asposewordscloud.models.requests.SaveAsTiffOnlineRequest(document=request_document, save_options=request_save_options)

        result = self.words_api.save_as_tiff_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for ConvertDocument.
    #
    def test_convert_document(self):
        local_folder = 'DocumentActions/ConvertDocument'

        request_document = open(os.path.join(self.local_test_folder, local_folder + '/test_uploadfile.docx'), 'rb')
        request = asposewordscloud.models.requests.ConvertDocumentRequest(document=request_document, format='pdf')

        result = self.words_api.convert_document(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # A test for ConvertDocument as a job.
    #
    def test_convert_document_job(self):
        local_folder = 'DocumentActions/ConvertDocument'

        request_document = open(os.path.join(self.local_test_folder, local_folder + '/test_uploadfile.docx'), 'rb')
        request = asposewordscloud.models.requests.ConvertDocumentJobRequest(document=request_document, format='pdf')

        job_handler = self.words_api.convert_document_job(request)
        self.assertIsNotNone(job_handler, 'Error has occurred.')

