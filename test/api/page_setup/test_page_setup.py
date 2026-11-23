# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_page_setup.py">
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
class TestPageSetup(BaseTestContext):
    #
    # Test for getting page settings.
    #
    def test_get_section_page_setup(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/PageSetup'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetSectionPageSetup.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetSectionPageSetupRequest(name=remote_file_name, section_index=0, folder=remote_data_folder)

        result = self.words_api.get_section_page_setup(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.page_setup, 'Validate GetSectionPageSetup response')
        self.assertEqual(1, result.page_setup.line_starting_number)

    #
    # Test for getting page settings online.
    #
    def test_get_section_page_setup_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetSectionPageSetupOnlineRequest(document=request_document, section_index=0)

        result = self.words_api.get_section_page_setup_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating page settings.
    #
    def test_update_section_page_setup(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/PageSetup'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestUpdateSectionPageSetup.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_page_setup = asposewordscloud.PageSetup(rtl_gutter=True, left_margin=10.0, orientation='Landscape', paper_size='A5')
        request = asposewordscloud.models.requests.UpdateSectionPageSetupRequest(name=remote_file_name, section_index=0, page_setup=request_page_setup, folder=remote_data_folder)

        result = self.words_api.update_section_page_setup(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.page_setup, 'Validate UpdateSectionPageSetup response')
        self.assertTrue(result.page_setup.rtl_gutter, 'Validate UpdateSectionPageSetup response')



    #
    # Test for updating page settings online.
    #
    def test_update_section_page_setup_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_page_setup = asposewordscloud.PageSetup(rtl_gutter=True, left_margin=10, orientation='Landscape', paper_size='A5')
        request = asposewordscloud.models.requests.UpdateSectionPageSetupOnlineRequest(document=request_document, section_index=0, page_setup=request_page_setup)

        result = self.words_api.update_section_page_setup_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for page rendering.
    #
    def test_get_render_page(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/PageSetup'
        local_text_file = 'DocumentElements/Text/SampleWordDocument.docx'
        remote_file_name = 'TestGetRenderPage.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_text_file), 'rb'))

        request = asposewordscloud.models.requests.RenderPageRequest(name=remote_file_name, page_index=1, format='jpg', folder=remote_data_folder)

        result = self.words_api.render_page(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for page rendering.
    #
    def test_get_render_page_online(self):
        local_text_file = 'DocumentElements/Text/SampleWordDocument.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_text_file), 'rb')
        request = asposewordscloud.models.requests.RenderPageOnlineRequest(document=request_document, page_index=1, format='jpg')

        result = self.words_api.render_page_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

