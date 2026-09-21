# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="downsample_options_data.py">
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

class DownsampleOptionsData(object):
    """Container class for Downsample options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'downsample_images': 'bool',
        'resolution': 'int',
        'resolution_threshold': 'int'
    }

    attribute_map = {
        'downsample_images': 'DownsampleImages',
        'resolution': 'Resolution',
        'resolution_threshold': 'ResolutionThreshold'
    }

    def __init__(self, downsample_images=None, resolution=None, resolution_threshold=None):  # noqa: E501
        """DownsampleOptionsData - a model defined in Swagger"""  # noqa: E501

        self._downsample_images = None
        self._resolution = None
        self._resolution_threshold = None
        self.discriminator = None

        if downsample_images is not None:
            self.downsample_images = downsample_images
        if resolution is not None:
            self.resolution = resolution
        if resolution_threshold is not None:
            self.resolution_threshold = resolution_threshold

    @property
    def downsample_images(self):
        """Gets the downsample_images of this DownsampleOptionsData.  # noqa: E501

        Gets or sets a value indicating whether images should be downsampled. The default value is true.  # noqa: E501

        :return: The downsample_images of this DownsampleOptionsData.  # noqa: E501
        :rtype: bool
        """
        return self._downsample_images

    @downsample_images.setter
    def downsample_images(self, downsample_images):
        """Sets the downsample_images of this DownsampleOptionsData.

        Gets or sets a value indicating whether images should be downsampled. The default value is true.  # noqa: E501

        :param downsample_images: The downsample_images of this DownsampleOptionsData.  # noqa: E501
        :type: bool
        """
        self._downsample_images = downsample_images

    @property
    def resolution(self):
        """Gets the resolution of this DownsampleOptionsData.  # noqa: E501

        Gets or sets the resolution in pixels per inch which the images should be downsampled to. The default value is 220 ppi.  # noqa: E501

        :return: The resolution of this DownsampleOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this DownsampleOptionsData.

        Gets or sets the resolution in pixels per inch which the images should be downsampled to. The default value is 220 ppi.  # noqa: E501

        :param resolution: The resolution of this DownsampleOptionsData.  # noqa: E501
        :type: int
        """
        self._resolution = resolution

    @property
    def resolution_threshold(self):
        """Gets the resolution_threshold of this DownsampleOptionsData.  # noqa: E501

        Gets or sets the threshold resolution in pixels per inch. If resolution of an image in the document is less than threshold value, the downsampling algorithm will not be applied. A value of 0 means the threshold check is not used and all images that can be reduced in size are downsampled. The default value is 0.  # noqa: E501

        :return: The resolution_threshold of this DownsampleOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._resolution_threshold

    @resolution_threshold.setter
    def resolution_threshold(self, resolution_threshold):
        """Sets the resolution_threshold of this DownsampleOptionsData.

        Gets or sets the threshold resolution in pixels per inch. If resolution of an image in the document is less than threshold value, the downsampling algorithm will not be applied. A value of 0 means the threshold check is not used and all images that can be reduced in size are downsampled. The default value is 0.  # noqa: E501

        :param resolution_threshold: The resolution_threshold of this DownsampleOptionsData.  # noqa: E501
        :type: int
        """
        self._resolution_threshold = resolution_threshold


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
        if not isinstance(other, DownsampleOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other