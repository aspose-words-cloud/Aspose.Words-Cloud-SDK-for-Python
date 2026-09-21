import uuid
import io

class BatchRequest(object):
    """
    Request wrapper for batch operation.
    Initializes a new instance.
    :param request The request to wrap.
    """
    def __init__(self, request):
        self.request = request
        self.id = str(uuid.uuid4())
        self.parent_id = None 

    def depends_on(self, parent_request):
        self.parent_id = parent_request.id

    def create_http_request(self, api_client, encryptor):
        http_request = self.request.create_http_request(api_client, encryptor)
        http_request["header_params"]["RequestId"] = self.id

        if self.parent_id is not None:
            http_request["header_params"]["DependsOn"] = self.parent_id

        return http_request

    def get_response_type(self):
        return self.request.get_response_type()

    def deserialize_response(self, api_client, response):
        return self.request.deserialize_response(api_client, response)

    def use_as_source(self):
        data = io.StringIO()
        data.write('resultOf(' + self.id + ')')
        return data
