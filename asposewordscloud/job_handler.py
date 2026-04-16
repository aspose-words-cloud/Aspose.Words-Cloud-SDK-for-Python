# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="job_handler.py">
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

from __future__ import absolute_import

import time

from asposewordscloud.rest import ApiException


class JobHandler(object):
    def __init__(self, api, request, info):
        self._api = api
        self._request = request
        self._info = info
        self._result = None

    @property
    def status(self):
        return self._info.status if self._info.status is not None else ''

    @property
    def message(self):
        return self._info.message if self._info.message is not None else ''

    @property
    def result(self):
        return self._result

    def update(self):
        if self._info.job_id is None:
            raise ApiException(status=400, reason='Invalid job id.')

        parts = self._api.api_client.call_job_result(self._info.job_id)
        if len(parts.parts) >= 1:
            self._info = self._api.api_client.deserialize_job_info_part(parts.parts[0])
            if len(parts.parts) >= 2 and self._is_succeeded():
                self._result = self._api.api_client.deserialize_http_response_part(self._request, parts.parts[1])

        return self._result

    def wait_result(self, update_interval=3):
        while self._is_queued() or self._is_processing():
            time.sleep(update_interval)
            self.update()

        if self._is_succeeded() and self._result is None:
            self.update()

        if not self._is_succeeded():
            raise ApiException(status=400, reason='Job failed with status "{0}" - "{1}".'.format(self.status, self.message))

        return self._result

    def _is_queued(self):
        return self.status.lower() == 'queued'

    def _is_processing(self):
        return self.status.lower() == 'processing'

    def _is_succeeded(self):
        return self.status.lower() == 'succeded' or self.status.lower() == 'succeeded'