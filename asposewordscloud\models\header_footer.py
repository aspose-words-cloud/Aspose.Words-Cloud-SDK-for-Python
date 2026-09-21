# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="header_footer.py">
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

class HeaderFooter(object):
    """DTO container with a section element.
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
        'type': 'str',
        'child_nodes': 'list[NodeLink]',
        'paragraphs': 'LinkElement',
        'drawing_objects': 'LinkElement'
    }

    attribute_map = {
        'link': 'Link',
        'type': 'Type',
        'child_nodes': 'ChildNodes',
        'paragraphs': 'Paragraphs',
        'drawing_objects': 'DrawingObjects'
    }

    def __init__(self, link=None, type=None, child_nodes=None, paragraphs=None, drawing_objects=None):  # noqa: E501
        """HeaderFooter - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._type = None
        self._child_nodes = None
        self._paragraphs = None
        self._drawing_objects = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if type is not None:
            self.type = type
        if child_nodes is not None:
            self.child_nodes = child_nodes
        if paragraphs is not None:
            self.paragraphs = paragraphs
        if drawing_objects is not None:
            self.drawing_objects = drawing_objects

    @property
    def link(self):
        """Gets the link of this HeaderFooter.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this HeaderFooter.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this HeaderFooter.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this HeaderFooter.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def type(self):
        """Gets the type of this HeaderFooter.  # noqa: E501

        Gets or sets the paragraph's text.  # noqa: E501

        :return: The type of this HeaderFooter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HeaderFooter.

        Gets or sets the paragraph's text.  # noqa: E501

        :param type: The type of this HeaderFooter.  # noqa: E501
        :type: str
        """
        allowed_values = ["HeaderEven", "HeaderPrimary", "FooterEven", "FooterPrimary", "HeaderFirst", "FooterFirst"]  # noqa: E501
        if not type.isdigit():
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values))
            self._type = type
        else:
            self._type = allowed_values[int(type) if six.PY3 else long(type)]

    @property
    def child_nodes(self):
        """Gets the child_nodes of this HeaderFooter.  # noqa: E501

        Gets or sets the child nodes.  # noqa: E501

        :return: The child_nodes of this HeaderFooter.  # noqa: E501
        :rtype: list[NodeLink]
        """
        return self._child_nodes

    @child_nodes.setter
    def child_nodes(self, child_nodes):
        """Sets the child_nodes of this HeaderFooter.

        Gets or sets the child nodes.  # noqa: E501

        :param child_nodes: The child_nodes of this HeaderFooter.  # noqa: E501
        :type: list[NodeLink]
        """
        self._child_nodes = child_nodes

    @property
    def paragraphs(self):
        """Gets the paragraphs of this HeaderFooter.  # noqa: E501

        Gets or sets the link to Paragraphs resource.  # noqa: E501

        :return: The paragraphs of this HeaderFooter.  # noqa: E501
        :rtype: LinkElement
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this HeaderFooter.

        Gets or sets the link to Paragraphs resource.  # noqa: E501

        :param paragraphs: The paragraphs of this HeaderFooter.  # noqa: E501
        :type: LinkElement
        """
        self._paragraphs = paragraphs

    @property
    def drawing_objects(self):
        """Gets the drawing_objects of this HeaderFooter.  # noqa: E501

        Gets or sets the link to DrawingObjects resource.  # noqa: E501

        :return: The drawing_objects of this HeaderFooter.  # noqa: E501
        :rtype: LinkElement
        """
        return self._drawing_objects

    @drawing_objects.setter
    def drawing_objects(self, drawing_objects):
        """Sets the drawing_objects of this HeaderFooter.

        Gets or sets the link to DrawingObjects resource.  # noqa: E501

        :param drawing_objects: The drawing_objects of this HeaderFooter.  # noqa: E501
        :type: LinkElement
        """
        self._drawing_objects = drawing_objects


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._type is None:
            raise ValueError("Property Type in HeaderFooter is required.")  # noqa: E501

        if self._link is not None:
            self._link.validate()




        if self._child_nodes is not None:
            for elementChildNodes in self._child_nodes:
                if elementChildNodes is not None:
                    elementChildNodes.validate()



        if self._paragraphs is not None:
            self._paragraphs.validate()



        if self._drawing_objects is not None:
            self._drawing_objects.validate()


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
        if not isinstance(other, HeaderFooter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other