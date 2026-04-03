# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_section.py">
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
# Example of how to work with sections.
#
class TestSection(BaseTestContext):
    #
    # Test for getting section by index.
    #
    def test_get_section(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Section'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetSection.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetSectionRequest(name=remote_file_name, section_index=0, folder=remote_data_folder)

        result = self.words_api.get_section(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.section, 'Validate GetSection response')
        self.assertIsNotNone(result.section.child_nodes, 'Validate GetSection response')
        self.assertEqual(13, len(result.section.child_nodes))
        self.assertEqual('0.3.0', result.section.child_nodes[0].node_id)

    #
    # Test for getting section by index online.
    #
    def test_get_section_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetSectionOnlineRequest(document=request_document, section_index=0)

        result = self.words_api.get_section_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting sections.
    #
    def test_get_sections(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Section'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetSections.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetSectionsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_sections(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.sections, 'Validate GetSections response')
        self.assertIsNotNone(result.sections.section_link_list, 'Validate GetSections response')
        self.assertEqual(1, len(result.sections.section_link_list))
        self.assertEqual('0', result.sections.section_link_list[0].node_id)

    #
    # Test for getting sections online.
    #
    def test_get_sections_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetSectionsOnlineRequest(document=request_document)

        result = self.words_api.get_sections_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for delete a section.
    #
    def test_delete_section(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Section'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteSection.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteSectionRequest(name=remote_file_name, section_index=0, folder=remote_data_folder)

        self.words_api.delete_section(request)


    #
    # Test for delete a section online.
    #
    def test_delete_section_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteSectionOnlineRequest(document=request_document, section_index=0)

        result = self.words_api.delete_section_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for merge a section with the next one.
    #
    def test_merge_with_next(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Section'
        remote_file_name = 'TestMergeWithNext.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'DocumentElements/Sections/Source.docx'), 'rb'))

        request = asposewordscloud.models.requests.MergeWithNextRequest(name=remote_file_name, section_index=0, folder=remote_data_folder)

        self.words_api.merge_with_next(request)


    #
    # Test for merge a section with the next one online.
    #
    def test_merge_with_next_online(self):
        request_document = open(os.path.join(self.local_test_folder, 'DocumentElements/Sections/Source.docx'), 'rb')
        request = asposewordscloud.models.requests.MergeWithNextOnlineRequest(document=request_document, section_index=0)

        result = self.words_api.merge_with_next_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for insertion a section.
    #
    def test_insert_section(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Section'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsertSection.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.InsertSectionRequest(name=remote_file_name, section_index=0, folder=remote_data_folder)

        self.words_api.insert_section(request)


    #
    # Test for insertion a section online.
    #
    def test_insert_section_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.InsertSectionOnlineRequest(document=request_document, section_index=0)

        result = self.words_api.insert_section_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for linking headers and footers to previous section.
    #
    def test_link_header_footers_to_previous(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/Section'
        remote_file_name = 'TestLinkHeaderFootersToPrevious.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, 'DocumentElements/Sections/Source.docx'), 'rb'))

        request = asposewordscloud.models.requests.LinkHeaderFootersToPreviousRequest(name=remote_file_name, section_index=1, folder=remote_data_folder)

        self.words_api.link_header_footers_to_previous(request)

