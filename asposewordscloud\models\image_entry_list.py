# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="image_entry_list.py">
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

class ImageEntryList(object):
    """Represents a list of images which will be appended to the original resource document or image.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'append_each_image_on_new_page': 'bool',
        'image_entries': 'list[ImageEntry]'
    }

    attribute_map = {
        'append_each_image_on_new_page': 'AppendEachImageOnNewPage',
        'image_entries': 'ImageEntries'
    }

    def __init__(self, append_each_image_on_new_page=None, image_entries=None):  # noqa: E501
        """ImageEntryList - a model defined in Swagger"""  # noqa: E501

        self._append_each_image_on_new_page = None
        self._image_entries = None
        self.discriminator = None

        if append_each_image_on_new_page is not None:
            self.append_each_image_on_new_page = append_each_image_on_new_page
        if image_entries is not None:
            self.image_entries = image_entries

    @property
    def append_each_image_on_new_page(self):
        """Gets the append_each_image_on_new_page of this ImageEntryList.  # noqa: E501

        Gets or sets a value indicating whether each image should be added to a new page in the document. This value only has an effect when adding images to a document that supports pagination.  # noqa: E501

        :return: The append_each_image_on_new_page of this ImageEntryList.  # noqa: E501
        :rtype: bool
        """
        return self._append_each_image_on_new_page

    @append_each_image_on_new_page.setter
    def append_each_image_on_new_page(self, append_each_image_on_new_page):
        """Sets the append_each_image_on_new_page of this ImageEntryList.

        Gets or sets a value indicating whether each image should be added to a new page in the document. This value only has an effect when adding images to a document that supports pagination.  # noqa: E501

        :param append_each_image_on_new_page: The append_each_image_on_new_page of this ImageEntryList.  # noqa: E501
        :type: bool
        """
        self._append_each_image_on_new_page = append_each_image_on_new_page

    @property
    def image_entries(self):
        """Gets the image_entries of this ImageEntryList.  # noqa: E501

        Gets or sets the list of images.  # noqa: E501

        :return: The image_entries of this ImageEntryList.  # noqa: E501
        :rtype: list[ImageEntry]
        """
        return self._image_entries

    @image_entries.setter
    def image_entries(self, image_entries):
        """Sets the image_entries of this ImageEntryList.

        Gets or sets the list of images.  # noqa: E501

        :param image_entries: The image_entries of this ImageEntryList.  # noqa: E501
        :type: list[ImageEntry]
        """
        self._image_entries = image_entries


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""
        if self._image_entries is not None:
            for element in self._image_entries:
                element.extract_files_content(filesContentResult)


    def validate(self):
        """Validate all required properties in model"""
        if self._image_entries is None:
            raise ValueError("Property ImageEntries in ImageEntryList is required.")  # noqa: E501

        if self._image_entries is not None:
            for elementImageEntries in self._image_entries:
                if elementImageEntries is not None:
                    elementImageEntries.validate()


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
        if not isinstance(other, ImageEntryList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other