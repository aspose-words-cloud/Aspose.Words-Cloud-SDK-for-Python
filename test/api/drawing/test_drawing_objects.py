# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="test_drawing_objects.py">
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
# Example of how to get drawing objects.
#
class TestDrawingObjects(BaseTestContext):
    #
    # Test for getting drawing objects from document.
    #
    def test_get_document_drawing_objects(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjects.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(name=remote_file_name, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_document_drawing_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing objects from document online.
    #
    def test_get_document_drawing_objects_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsOnlineRequest(document=request_document, node_path='sections/0')

        result = self.words_api.get_document_drawing_objects_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing objects from document without node path.
    #
    def test_get_document_drawing_objects_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectsWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectsRequest(name=remote_file_name, folder=remote_data_folder)

        result = self.words_api.get_document_drawing_objects(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object by specified index.
    #
    def test_get_document_drawing_object_by_index(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectByIndex.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(name=remote_file_name, index=0, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_document_drawing_object_by_index(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object by specified index online.
    #
    def test_get_document_drawing_object_by_index_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexOnlineRequest(document=request_document, index=0, node_path='sections/0')

        result = self.words_api.get_document_drawing_object_by_index_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object by specified index without node path.
    #
    def test_get_document_drawing_object_by_index_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectByIndexWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectByIndexRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_document_drawing_object_by_index(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object by specified index and format.
    #
    def test_render_drawing_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectByIndexWithFormat.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderDrawingObjectRequest(name=remote_file_name, format='png', index=0, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.render_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object by specified index and format online.
    #
    def test_render_drawing_object_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.RenderDrawingObjectOnlineRequest(document=request_document, format='png', index=0, node_path='sections/0')

        result = self.words_api.render_drawing_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object by specified index and format without node path.
    #
    def test_render_drawing_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectByIndexWithFormatWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.RenderDrawingObjectRequest(name=remote_file_name, format='png', index=0, folder=remote_data_folder)

        result = self.words_api.render_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for reading drawing object's image data.
    #
    def test_get_document_drawing_object_image_data(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectImageData.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(name=remote_file_name, index=0, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_document_drawing_object_image_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for reading drawing object's image data online.
    #
    def test_get_document_drawing_object_image_data_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataOnlineRequest(document=request_document, index=0, node_path='sections/0')

        result = self.words_api.get_document_drawing_object_image_data_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for reading drawing object's image data without node path.
    #
    def test_get_document_drawing_object_image_data_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectImageDataWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectImageDataRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_document_drawing_object_image_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object OLE data.
    #
    def test_get_document_drawing_object_ole_data(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_drawing_file = 'DocumentElements/DrawingObjects/sample_EmbeddedOLE.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectOleData.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_drawing_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(name=remote_file_name, index=0, node_path='sections/0', folder=remote_data_folder)

        result = self.words_api.get_document_drawing_object_ole_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object OLE data online.
    #
    def test_get_document_drawing_object_ole_data_online(self):
        local_drawing_file = 'DocumentElements/DrawingObjects/sample_EmbeddedOLE.docx'

        request_document = open(os.path.join(self.local_test_folder, local_drawing_file), 'rb')
        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataOnlineRequest(document=request_document, index=0, node_path='sections/0')

        result = self.words_api.get_document_drawing_object_ole_data_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for getting drawing object OLE data without node path.
    #
    def test_get_document_drawing_object_ole_data_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_drawing_file = 'DocumentElements/DrawingObjects/sample_EmbeddedOLE.docx'
        remote_file_name = 'TestGetDocumentDrawingObjectOleDataWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_drawing_file), 'rb'))

        request = asposewordscloud.models.requests.GetDocumentDrawingObjectOleDataRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        result = self.words_api.get_document_drawing_object_ole_data(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding drawing object.
    #
    def test_insert_drawing_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsetDrawingObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_drawing_object = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request_image_file = open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.InsertDrawingObjectRequest(name=remote_file_name, drawing_object=request_drawing_object, image_file=request_image_file, node_path='', folder=remote_data_folder)

        result = self.words_api.insert_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding drawing object online.
    #
    def test_insert_drawing_object_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_drawing_object = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request_image_file = open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.InsertDrawingObjectOnlineRequest(document=request_document, drawing_object=request_drawing_object, image_file=request_image_file, node_path='')

        result = self.words_api.insert_drawing_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for adding drawing object without node path.
    #
    def test_insert_drawing_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestInsetDrawingObjectWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_drawing_object = asposewordscloud.DrawingObjectInsert(height=0, left=0, top=0, width=0, relative_horizontal_position='Margin', relative_vertical_position='Margin', wrap_type='Inline')
        request_image_file = open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.InsertDrawingObjectRequest(name=remote_file_name, drawing_object=request_drawing_object, image_file=request_image_file, folder=remote_data_folder)

        result = self.words_api.insert_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting drawing object.
    #
    def test_delete_drawing_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteDrawingObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(name=remote_file_name, index=0, node_path='', folder=remote_data_folder)

        self.words_api.delete_drawing_object(request)


    #
    # Test for deleting drawing object online.
    #
    def test_delete_drawing_object_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request = asposewordscloud.models.requests.DeleteDrawingObjectOnlineRequest(document=request_document, index=0, node_path='')

        result = self.words_api.delete_drawing_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for deleting drawing object without node path.
    #
    def test_delete_drawing_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestDeleteDrawingObjectWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request = asposewordscloud.models.requests.DeleteDrawingObjectRequest(name=remote_file_name, index=0, folder=remote_data_folder)

        self.words_api.delete_drawing_object(request)


    #
    # Test for updating drawing object.
    #
    def test_update_drawing_object(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestUpdateDrawingObject.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_drawing_object = asposewordscloud.DrawingObjectUpdate(left=0)
        request_image_file = open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.UpdateDrawingObjectRequest(name=remote_file_name, drawing_object=request_drawing_object, image_file=request_image_file, index=0, node_path='', folder=remote_data_folder)

        result = self.words_api.update_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating drawing object online.
    #
    def test_update_drawing_object_online(self):
        local_file = 'Common/test_multi_pages.docx'

        request_document = open(os.path.join(self.local_test_folder, local_file), 'rb')
        request_drawing_object = asposewordscloud.DrawingObjectUpdate(left=0)
        request_image_file = open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.UpdateDrawingObjectOnlineRequest(document=request_document, drawing_object=request_drawing_object, image_file=request_image_file, index=0, node_path='')

        result = self.words_api.update_drawing_object_online(request)
        self.assertIsNotNone(result, 'Error has occurred.')


    #
    # Test for updating drawing object without node path.
    #
    def test_update_drawing_object_without_node_path(self):
        remote_data_folder = self.remote_test_folder + '/DocumentElements/DrawingObjectss'
        local_file = 'Common/test_multi_pages.docx'
        remote_file_name = 'TestUpdateDrawingObjectWithoutNodePath.docx'

        self.upload_file(remote_data_folder + '/' + remote_file_name, open(os.path.join(self.local_test_folder, local_file), 'rb'))

        request_drawing_object = asposewordscloud.DrawingObjectUpdate(left=0)
        request_image_file = open(os.path.join(self.local_test_folder, 'Common/aspose-cloud.png'), 'rb')
        request = asposewordscloud.models.requests.UpdateDrawingObjectRequest(name=remote_file_name, drawing_object=request_drawing_object, image_file=request_image_file, index=0, folder=remote_data_folder)

        result = self.words_api.update_drawing_object(request)
        self.assertIsNotNone(result, 'Error has occurred.')

