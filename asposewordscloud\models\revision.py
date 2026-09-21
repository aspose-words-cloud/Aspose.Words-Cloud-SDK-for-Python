# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="revision.py">
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

class Revision(object):
    """Revision Dto.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'revision_author': 'str',
        'revision_date_time': 'datetime',
        'revision_text': 'str',
        'revision_type': 'str'
    }

    attribute_map = {
        'revision_author': 'RevisionAuthor',
        'revision_date_time': 'RevisionDateTime',
        'revision_text': 'RevisionText',
        'revision_type': 'RevisionType'
    }

    def __init__(self, revision_author=None, revision_date_time=None, revision_text=None, revision_type=None):  # noqa: E501
        """Revision - a model defined in Swagger"""  # noqa: E501

        self._revision_author = None
        self._revision_date_time = None
        self._revision_text = None
        self._revision_type = None
        self.discriminator = None

        if revision_author is not None:
            self.revision_author = revision_author
        if revision_date_time is not None:
            self.revision_date_time = revision_date_time
        if revision_text is not None:
            self.revision_text = revision_text
        if revision_type is not None:
            self.revision_type = revision_type

    @property
    def revision_author(self):
        """Gets the revision_author of this Revision.  # noqa: E501

        Gets or sets the revision author.  # noqa: E501

        :return: The revision_author of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._revision_author

    @revision_author.setter
    def revision_author(self, revision_author):
        """Sets the revision_author of this Revision.

        Gets or sets the revision author.  # noqa: E501

        :param revision_author: The revision_author of this Revision.  # noqa: E501
        :type: str
        """
        self._revision_author = revision_author

    @property
    def revision_date_time(self):
        """Gets the revision_date_time of this Revision.  # noqa: E501

        Gets or sets the revision date time.  # noqa: E501

        :return: The revision_date_time of this Revision.  # noqa: E501
        :rtype: datetime
        """
        return self._revision_date_time

    @revision_date_time.setter
    def revision_date_time(self, revision_date_time):
        """Sets the revision_date_time of this Revision.

        Gets or sets the revision date time.  # noqa: E501

        :param revision_date_time: The revision_date_time of this Revision.  # noqa: E501
        :type: datetime
        """
        self._revision_date_time = revision_date_time

    @property
    def revision_text(self):
        """Gets the revision_text of this Revision.  # noqa: E501

        Gets or sets the revision text.  # noqa: E501

        :return: The revision_text of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._revision_text

    @revision_text.setter
    def revision_text(self, revision_text):
        """Sets the revision_text of this Revision.

        Gets or sets the revision text.  # noqa: E501

        :param revision_text: The revision_text of this Revision.  # noqa: E501
        :type: str
        """
        self._revision_text = revision_text

    @property
    def revision_type(self):
        """Gets the revision_type of this Revision.  # noqa: E501

        Gets or sets the revision type.  # noqa: E501

        :return: The revision_type of this Revision.  # noqa: E501
        :rtype: str
        """
        return self._revision_type

    @revision_type.setter
    def revision_type(self, revision_type):
        """Sets the revision_type of this Revision.

        Gets or sets the revision type.  # noqa: E501

        :param revision_type: The revision_type of this Revision.  # noqa: E501
        :type: str
        """
        self._revision_type = revision_type


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._revision_date_time is None:
            raise ValueError("Property RevisionDateTime in Revision is required.")  # noqa: E501

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
        if not isinstance(other, Revision):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other