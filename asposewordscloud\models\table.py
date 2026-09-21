# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="table.py">
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

class Table(object):
    """DTO container with a table element.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'WordsApiLink',
        'node_id': 'str',
        'table_row_list': 'list[TableRow]',
        'table_properties': 'TableProperties'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'table_row_list': 'TableRowList',
        'table_properties': 'TableProperties'
    }

    def __init__(self, link=None, node_id=None, table_row_list=None, table_properties=None):  # noqa: E501
        """Table - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._table_row_list = None
        self._table_properties = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if table_row_list is not None:
            self.table_row_list = table_row_list
        if table_properties is not None:
            self.table_properties = table_properties

    @property
    def link(self):
        """Gets the link of this Table.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this Table.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Table.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this Table.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this Table.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this Table.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this Table.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this Table.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def table_row_list(self):
        """Gets the table_row_list of this Table.  # noqa: E501

        Gets or sets the collection of table's rows.  # noqa: E501

        :return: The table_row_list of this Table.  # noqa: E501
        :rtype: list[TableRow]
        """
        return self._table_row_list

    @table_row_list.setter
    def table_row_list(self, table_row_list):
        """Sets the table_row_list of this Table.

        Gets or sets the collection of table's rows.  # noqa: E501

        :param table_row_list: The table_row_list of this Table.  # noqa: E501
        :type: list[TableRow]
        """
        self._table_row_list = table_row_list

    @property
    def table_properties(self):
        """Gets the table_properties of this Table.  # noqa: E501

        Gets or sets table properties.  # noqa: E501

        :return: The table_properties of this Table.  # noqa: E501
        :rtype: TableProperties
        """
        return self._table_properties

    @table_properties.setter
    def table_properties(self, table_properties):
        """Sets the table_properties of this Table.

        Gets or sets table properties.  # noqa: E501

        :param table_properties: The table_properties of this Table.  # noqa: E501
        :type: TableProperties
        """
        self._table_properties = table_properties


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()




        if self._table_row_list is not None:
            for elementTableRowList in self._table_row_list:
                if elementTableRowList is not None:
                    elementTableRowList.validate()



        if self._table_properties is not None:
            self._table_properties.validate()


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
        if not isinstance(other, Table):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other