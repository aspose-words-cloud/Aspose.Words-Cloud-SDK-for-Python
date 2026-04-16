# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="job_info.py">
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
import pprint
import re  # noqa: F401

import typing_extensions
import datetime
import six
import json

class JobInfo(object):
    """The REST response with a job result.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'job_id': 'str',
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'job_id': 'JobId',
        'message': 'Message',
        'status': 'Status'
    }

    def __init__(self, job_id=None, message=None, status=None):  # noqa: E501
        """JobInfo - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._message = None
        self._status = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def job_id(self):
        """Gets the job_id of this JobInfo.  # noqa: E501

        Gets or sets the job id.  # noqa: E501

        :return: The job_id of this JobInfo.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobInfo.

        Gets or sets the job id.  # noqa: E501

        :param job_id: The job_id of this JobInfo.  # noqa: E501
        :type: str
        """
        self._job_id = job_id

    @property
    def message(self):
        """Gets the message of this JobInfo.  # noqa: E501

        Gets or sets the job message.  # noqa: E501

        :return: The message of this JobInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobInfo.

        Gets or sets the job message.  # noqa: E501

        :param message: The message of this JobInfo.  # noqa: E501
        :type: str
        """
        self._message = message

    @property
    def status(self):
        """Gets the status of this JobInfo.  # noqa: E501

        Gets or sets the job status.  # noqa: E501

        :return: The status of this JobInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobInfo.

        Gets or sets the job status.  # noqa: E501

        :param status: The status of this JobInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Queued", "Processing", "Succeded", "Failed"]  # noqa: E501
        if not status.isdigit():
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                    .format(status, allowed_values))
            self._status = status
        else:
            self._status = allowed_values[int(status) if six.PY3 else long(status)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._status is None:
            raise ValueError("Property Status in JobInfo is required.")  # noqa: E501

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return result

    def to_json(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map[attr]] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map[attr]] = value.to_dict()
            elif isinstance(value, dict):
                result[self.attribute_map[attr]] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, (datetime.datetime, datetime.date)):
                result[self.attribute_map[attr]] = value.isoformat()
            else:
                result[self.attribute_map[attr]] = value

        return json.dumps(result)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other