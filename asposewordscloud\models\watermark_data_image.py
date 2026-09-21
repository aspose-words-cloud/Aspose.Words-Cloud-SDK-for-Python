# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="watermark_data_image.py">
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

class WatermarkDataImage(object):
    """Class for insert watermark image request building.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image': 'FileReference',
        'is_washout': 'bool',
        'scale': 'float'
    }

    attribute_map = {
        'image': 'Image',
        'is_washout': 'IsWashout',
        'scale': 'Scale'
    }

    def __init__(self, image=None, is_washout=None, scale=None):  # noqa: E501
        """WatermarkDataImage - a model defined in Swagger"""  # noqa: E501

        self._image = None
        self._is_washout = None
        self._scale = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if is_washout is not None:
            self.is_washout = is_washout
        if scale is not None:
            self.scale = scale

    @property
    def image(self):
        """Gets the image of this WatermarkDataImage.  # noqa: E501

        Gets or sets the watermark image.  # noqa: E501

        :return: The image of this WatermarkDataImage.  # noqa: E501
        :rtype: FileReference
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this WatermarkDataImage.

        Gets or sets the watermark image.  # noqa: E501

        :param image: The image of this WatermarkDataImage.  # noqa: E501
        :type: FileReference
        """
        self._image = image

    @property
    def is_washout(self):
        """Gets the is_washout of this WatermarkDataImage.  # noqa: E501

        Gets or sets a boolean value which is responsible for washout effect of the watermark. The default value is true.  # noqa: E501

        :return: The is_washout of this WatermarkDataImage.  # noqa: E501
        :rtype: bool
        """
        return self._is_washout

    @is_washout.setter
    def is_washout(self, is_washout):
        """Sets the is_washout of this WatermarkDataImage.

        Gets or sets a boolean value which is responsible for washout effect of the watermark. The default value is true.  # noqa: E501

        :param is_washout: The is_washout of this WatermarkDataImage.  # noqa: E501
        :type: bool
        """
        self._is_washout = is_washout

    @property
    def scale(self):
        """Gets the scale of this WatermarkDataImage.  # noqa: E501

        Gets or sets the scale factor expressed as a fraction of the image. The default value is 0 - auto. Valid values range from 0 to 65.5 inclusive. Auto scale means that the watermark will be scaled to its max width and max height relative to the page margins.  # noqa: E501

        :return: The scale of this WatermarkDataImage.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this WatermarkDataImage.

        Gets or sets the scale factor expressed as a fraction of the image. The default value is 0 - auto. Valid values range from 0 to 65.5 inclusive. Auto scale means that the watermark will be scaled to its max width and max height relative to the page margins.  # noqa: E501

        :param scale: The scale of this WatermarkDataImage.  # noqa: E501
        :type: float
        """
        self._scale = scale


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""
        if self._image is not None:
            self._image.extract_files_content(filesContentResult)




    def validate(self):
        """Validate all required properties in model"""
        if self._image is None:
            raise ValueError("Property Image in WatermarkDataImage is required.")  # noqa: E501

        if self._image is not None:
            self._image.validate()




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
        if not isinstance(other, WatermarkDataImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other