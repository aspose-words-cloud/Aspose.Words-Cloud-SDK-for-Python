# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_styles.py">
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
# Example of how to work with styles.
#
class TestStyles(BaseTestContext):
    #
    # Test for getting styles from document.
    #
    def test_get_styles(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestGetStyles.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetStylesRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_styles(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.styles, 'Validate GetStyles response')
        self.assertEqual(22, len(result.styles))
        self.assertEqual('Default Paragraph Font', result.styles[0].name)

    #
    # Test for getting styles from document online.
    #
    def test_get_styles_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetStylesOnlineRequest(document=request_document)

        result = self.words_api.get_styles_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting style from document.
    #
    def test_get_style(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestGetStyle.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetStyleRequest(name=remote_file_name, style_name='Heading 1', folder=remote_data_folder)

        result = self.words_api.get_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.style, 'Validate GetStyle response')
        self.assertEqual('Heading 1', result.style.name)

    #
    # Test for getting style from document online.
    #
    def test_get_style_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetStyleOnlineRequest(document=request_document, style_name='Heading 1')

        result = self.words_api.get_style_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating style from document.
    #
    def test_update_style(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestUpdateStyle.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_style_update = asposewordscloud.StyleUpdate(name='My Style')
        request = asposewordscloud.models.requests.UpdateStyleRequest(name=remote_file_name, style_update=request_style_update, style_name='Heading 1', folder=remote_data_folder)

        result = self.words_api.update_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.style, 'Validate UpdateStyle response')
        self.assertEqual('My Style', result.style.name)

    #
    # Test for updating style from document online.
    #
    def test_update_style_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_style_update = asposewordscloud.StyleUpdate(name='My Style')
        request = asposewordscloud.models.requests.UpdateStyleOnlineRequest(document=request_document, style_update=request_style_update, style_name='Heading 1')

        result = self.words_api.update_style_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for inserting style from document.
    #
    def test_insert_style(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestInsertStyle.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_style_insert = asposewordscloud.StyleInsert(style_name='My Style', style_type='Paragraph')
        request = asposewordscloud.models.requests.InsertStyleRequest(name=remote_file_name, style_insert=request_style_insert, folder=remote_data_folder)

        result = self.words_api.insert_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.style, 'Validate InsertStyle response')
        self.assertEqual('My Style', result.style.name)

    #
    # Test for inserting style from document online.
    #
    def test_insert_style_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_style_insert = asposewordscloud.StyleInsert(style_name='My Style', style_type='Paragraph')
        request = asposewordscloud.models.requests.InsertStyleOnlineRequest(document=request_document, style_insert=request_style_insert)

        result = self.words_api.insert_style_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for coping style from document.
    #
    def test_copy_style(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestCopyStyle.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_style_copy = asposewordscloud.StyleCopy(style_name='Heading 1')
        request = asposewordscloud.models.requests.CopyStyleRequest(name=remote_file_name, style_copy=request_style_copy, folder=remote_data_folder)

        result = self.words_api.copy_style(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.style, 'Validate CopyStyle response')
        self.assertEqual('Heading 1_0', result.style.name)

    #
    # Test for coping style from document online.
    #
    def test_copy_style_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_style_copy = asposewordscloud.StyleCopy(style_name='Heading 1')
        request = asposewordscloud.models.requests.CopyStyleOnlineRequest(document=request_document, style_copy=request_style_copy)

        result = self.words_api.copy_style_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting style from document element.
    #
    def test_get_style_from_document_element(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestGetStyleFromDocumentElement.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetStyleFromDocumentElementRequest(name=remote_file_name, styled_node_path='paragraphs/1/paragraphFormat', folder=remote_data_folder)

        result = self.words_api.get_style_from_document_element(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.style, 'Validate GetStyleFromDocumentElement response')
        self.assertEqual('TOC 1', result.style.name)

    #
    # Test for getting style from document element online.
    #
    def test_get_style_from_document_element_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetStyleFromDocumentElementOnlineRequest(document=request_document, styled_node_path='paragraphs/1/paragraphFormat')

        result = self.words_api.get_style_from_document_element_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for applying style to document element.
    #
    def test_apply_style_to_document_element(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestApplyStyleToDocumentElement.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_style_apply = asposewordscloud.StyleApply(style_name='Heading 1')
        request = asposewordscloud.models.requests.ApplyStyleToDocumentElementRequest(name=remote_file_name, style_apply=request_style_apply, styled_node_path='paragraphs/1/paragraphFormat', folder=remote_data_folder)

        result = self.words_api.apply_style_to_document_element(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for applying style to document element online.
    #
    def test_apply_style_to_document_element_online(self):
        local_file = 'DocumentElements/Styles/GetStyles.docx'

        request_document = self.open_file(os.path.join(self.local_test_folder, local_file), 'rb')
        request_style_apply = asposewordscloud.StyleApply(style_name='Heading 1')
        request = asposewordscloud.models.requests.ApplyStyleToDocumentElementOnlineRequest(document=request_document, style_apply=request_style_apply, styled_node_path='paragraphs/1/paragraphFormat')

        result = self.words_api.apply_style_to_document_element_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for copying styles from a template.
    #
    def test_copy_styles_from_template(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Styles'
        local_file = 'DocumentElements/Styles/GetStyles.docx'
        remote_file_name = 'TestCopyStylesFromTemplate.docx'
        template_folder = 'DocumentElements/Styles'
        template_name = 'StyleTemplate.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, self.open_file(os.path.join(self.local_test_folder, local_file), 'rb'))
        self.upload_file(remote_data_folder + '/' + template_name, self.open_file(os.path.join(self.local_test_folder, template_folder + '/' + template_name), 'rb'))

        request = asposewordscloud.models.requests.CopyStylesFromTemplateRequest(name=remote_file_name, template_name=template_name, folder=remote_data_folder)

        result = self.words_api.copy_styles_from_template(request)
        self.assertIsNotNone(result, 'Error has occurred.')

