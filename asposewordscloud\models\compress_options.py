# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="compress_options.py">
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

class CompressOptions(object):
    """Options of document compress.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'images_quality': 'int',
        'images_reduce_size_factor': 'int'
    }

    attribute_map = {
        'images_quality': 'ImagesQuality',
        'images_reduce_size_factor': 'ImagesReduceSizeFactor'
    }

    def __init__(self, images_quality=None, images_reduce_size_factor=None):  # noqa: E501
        """CompressOptions - a model defined in Swagger"""  # noqa: E501

        self._images_quality = None
        self._images_reduce_size_factor = None
        self.discriminator = None

        if images_quality is not None:
            self.images_quality = images_quality
        if images_reduce_size_factor is not None:
            self.images_reduce_size_factor = images_reduce_size_factor

    @property
    def images_quality(self):
        """Gets the images_quality of this CompressOptions.  # noqa: E501

        Gets or sets the quality level of images from 0 to 100. The default value is 75.  # noqa: E501

        :return: The images_quality of this CompressOptions.  # noqa: E501
        :rtype: int
        """
        return self._images_quality

    @images_quality.setter
    def images_quality(self, images_quality):
        """Sets the images_quality of this CompressOptions.

        Gets or sets the quality level of images from 0 to 100. The default value is 75.  # noqa: E501

        :param images_quality: The images_quality of this CompressOptions.  # noqa: E501
        :type: int
        """
        self._images_quality = images_quality

    @property
    def images_reduce_size_factor(self):
        """Gets the images_reduce_size_factor of this CompressOptions.  # noqa: E501

        Gets or sets the resize factor of images. This value determines how many times the size of the images in the document will be reduced. The parameter value must be greater than 1 for resizing. The default value is 1 and has no effect on images size.  # noqa: E501

        :return: The images_reduce_size_factor of this CompressOptions.  # noqa: E501
        :rtype: int
        """
        return self._images_reduce_size_factor

    @images_reduce_size_factor.setter
    def images_reduce_size_factor(self, images_reduce_size_factor):
        """Sets the images_reduce_size_factor of this CompressOptions.

        Gets or sets the resize factor of images. This value determines how many times the size of the images in the document will be reduced. The parameter value must be greater than 1 for resizing. The default value is 1 and has no effect on images size.  # noqa: E501

        :param images_reduce_size_factor: The images_reduce_size_factor of this CompressOptions.  # noqa: E501
        :type: int
        """
        self._images_reduce_size_factor = images_reduce_size_factor


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

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
        if not isinstance(other, CompressOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other