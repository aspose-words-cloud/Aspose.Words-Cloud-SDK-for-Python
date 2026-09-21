# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="advanced_compare_options.py">
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

class AdvancedCompareOptions(object):
    """Allows to set advanced compare options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compare_list_definitions': 'bool',
        'ignore_dml_unique_id': 'bool',
        'ignore_store_item_id': 'bool'
    }

    attribute_map = {
        'compare_list_definitions': 'CompareListDefinitions',
        'ignore_dml_unique_id': 'IgnoreDmlUniqueId',
        'ignore_store_item_id': 'IgnoreStoreItemId'
    }

    def __init__(self, compare_list_definitions=None, ignore_dml_unique_id=None, ignore_store_item_id=None):  # noqa: E501
        """AdvancedCompareOptions - a model defined in Swagger"""  # noqa: E501

        self._compare_list_definitions = None
        self._ignore_dml_unique_id = None
        self._ignore_store_item_id = None
        self.discriminator = None

        if compare_list_definitions is not None:
            self.compare_list_definitions = compare_list_definitions
        if ignore_dml_unique_id is not None:
            self.ignore_dml_unique_id = ignore_dml_unique_id
        if ignore_store_item_id is not None:
            self.ignore_store_item_id = ignore_store_item_id

    @property
    def compare_list_definitions(self):
        """Gets the compare_list_definitions of this AdvancedCompareOptions.  # noqa: E501

        Gets or sets the value indicating whether list definition contents are compared instead of list definition Ids. Default value is false.  # noqa: E501

        :return: The compare_list_definitions of this AdvancedCompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._compare_list_definitions

    @compare_list_definitions.setter
    def compare_list_definitions(self, compare_list_definitions):
        """Sets the compare_list_definitions of this AdvancedCompareOptions.

        Gets or sets the value indicating whether list definition contents are compared instead of list definition Ids. Default value is false.  # noqa: E501

        :param compare_list_definitions: The compare_list_definitions of this AdvancedCompareOptions.  # noqa: E501
        :type: bool
        """
        self._compare_list_definitions = compare_list_definitions

    @property
    def ignore_dml_unique_id(self):
        """Gets the ignore_dml_unique_id of this AdvancedCompareOptions.  # noqa: E501

        Gets or sets the value indicating whether to ignore difference in DrawingML unique Id. Default value is false.  # noqa: E501

        :return: The ignore_dml_unique_id of this AdvancedCompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_dml_unique_id

    @ignore_dml_unique_id.setter
    def ignore_dml_unique_id(self, ignore_dml_unique_id):
        """Sets the ignore_dml_unique_id of this AdvancedCompareOptions.

        Gets or sets the value indicating whether to ignore difference in DrawingML unique Id. Default value is false.  # noqa: E501

        :param ignore_dml_unique_id: The ignore_dml_unique_id of this AdvancedCompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_dml_unique_id = ignore_dml_unique_id

    @property
    def ignore_store_item_id(self):
        """Gets the ignore_store_item_id of this AdvancedCompareOptions.  # noqa: E501

        Gets or sets the value indicating whether to ignore difference in StructuredDocumentTag store item Id. Default value is false.  # noqa: E501

        :return: The ignore_store_item_id of this AdvancedCompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_store_item_id

    @ignore_store_item_id.setter
    def ignore_store_item_id(self, ignore_store_item_id):
        """Sets the ignore_store_item_id of this AdvancedCompareOptions.

        Gets or sets the value indicating whether to ignore difference in StructuredDocumentTag store item Id. Default value is false.  # noqa: E501

        :param ignore_store_item_id: The ignore_store_item_id of this AdvancedCompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_store_item_id = ignore_store_item_id


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
        if not isinstance(other, AdvancedCompareOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other