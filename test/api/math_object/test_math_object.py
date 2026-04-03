# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_math_object.py">
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
# Example of how to work with MathObjects.
#
class TestMathObject(BaseTestContext):
    #
    # Test for getting mathObjects.
    #
    def test_get_office_math_objects(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestGetOfficeMathObjects.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(name=remote_file_name, node_path='', folder=remote_data_folder)

        result = self.words_api.get_office_math_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.office_math_objects, 'Validate GetOfficeMathObjects response')
        self.assertIsNotNone(result.office_math_objects.list, 'Validate GetOfficeMathObjects response')
        self.assertEqual(16, len(result.office_math_objects.list))
        self.assertEqual('0.0.0.0', result.office_math_objects.list[0].node_id)

    #
    # Test for getting mathObjects online.
    #
    def test_get_office_math_objects_online(self):
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetOfficeMathObjectsOnlineRequest(document=request_document, node_path='')

        result = self.words_api.get_office_math_objects_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting mathObjects without node path.
    #
    def test_get_office_math_objects_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestGetOfficeMathObjectsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_office_math_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.office_math_objects, 'Validate GetOfficeMathObjectsWithoutNodePath response')
        self.assertIsNotNone(result.office_math_objects.list, 'Validate GetOfficeMathObjectsWithoutNodePath response')
        self.assertEqual(16, len(result.office_math_objects.list))
        self.assertEqual('0.0.0.0', result.office_math_objects.list[0].node_id)

    #
    # Test for getting mathObject.
    #
    def test_get_office_math_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestGetOfficeMathObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.get_office_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.office_math_object, 'Validate GetOfficeMathObject response')
        self.assertEqual('0.0.0.0', result.office_math_object.node_id)

    #
    # Test for getting mathObject online.
    #
    def test_get_office_math_object_online(self):
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetOfficeMathObjectOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.get_office_math_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting mathObject without node path.
    #
    def test_get_office_math_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestGetOfficeMathObjectWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetOfficeMathObjectRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_office_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')
        self.assertIsNotNone(result.office_math_object, 'Validate GetOfficeMathObjectWithoutNodePath response')
        self.assertEqual('0.0.0.0', result.office_math_object.node_id)

    #
    # Test for rendering mathObject.
    #
    def test_render_math_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestRenderMathObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderMathObjectRequest(name=remote_file_name, format='png', index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.render_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for rendering mathObject.
    #
    def test_render_math_object_online(self):
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.RenderMathObjectOnlineRequest(document=request_document, format='png', index=0, node_path='')

        result = self.words_api.render_math_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for rendering mathObject without node path.
    #
    def test_render_math_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestRenderMathObjectWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderMathObjectRequest(name=remote_file_name, format='png', index=0, folder=remote_data_folder)

        result = self.words_api.render_math_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting mathObject.
    #
    def test_delete_office_math_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestDeleteOfficeMathObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        self.words_api.delete_office_math_object(request)


    #
    # Test for deleting mathObject online.
    #
    def test_delete_office_math_object_online(self):
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteOfficeMathObjectOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.delete_office_math_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting mathObject without node path.
    #
    def test_delete_office_math_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestDeleteOfficeMathObjectWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteOfficeMathObjectRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        self.words_api.delete_office_math_object(request)


    #
    # Test for deleting math objects.
    #
    def test_delete_office_math_objects(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/MathObjects'
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'
        remote_file_name = 'TestDeleteOfficeMathObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteOfficeMathObjectsRequest(name=remote_file_name, folder=remote_data_folder)

        self.words_api.delete_office_math_objects(request)


    #
    # Test for deleting math objects online.
    #
    def test_delete_office_math_objects_online(self):
        local_file = 'DocumentElements/MathObjects/MathObjects.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteOfficeMathObjectsOnlineRequest(document=request_document)

        result = self.words_api.delete_office_math_objects_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')

