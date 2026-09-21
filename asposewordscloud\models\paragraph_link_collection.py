# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="paragraph_link_collection.py">
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

class ParagraphLinkCollection(object):
    """The collection of paragraph's links.
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
        'paragraph_link_list': 'list[ParagraphLink]'
    }

    attribute_map = {
        'link': 'Link',
        'paragraph_link_list': 'ParagraphLinkList'
    }

    def __init__(self, link=None, paragraph_link_list=None):  # noqa: E501
        """ParagraphLinkCollection - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._paragraph_link_list = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if paragraph_link_list is not None:
            self.paragraph_link_list = paragraph_link_list

    @property
    def link(self):
        """Gets the link of this ParagraphLinkCollection.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this ParagraphLinkCollection.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ParagraphLinkCollection.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this ParagraphLinkCollection.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def paragraph_link_list(self):
        """Gets the paragraph_link_list of this ParagraphLinkCollection.  # noqa: E501

        Gets or sets the collection of paragraph's links.  # noqa: E501

        :return: The paragraph_link_list of this ParagraphLinkCollection.  # noqa: E501
        :rtype: list[ParagraphLink]
        """
        return self._paragraph_link_list

    @paragraph_link_list.setter
    def paragraph_link_list(self, paragraph_link_list):
        """Sets the paragraph_link_list of this ParagraphLinkCollection.

        Gets or sets the collection of paragraph's links.  # noqa: E501

        :param paragraph_link_list: The paragraph_link_list of this ParagraphLinkCollection.  # noqa: E501
        :type: list[ParagraphLink]
        """
        self._paragraph_link_list = paragraph_link_list


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()



        if self._paragraph_link_list is not None:
            for elementParagraphLinkList in self._paragraph_link_list:
                if elementParagraphLinkList is not None:
                    elementParagraphLinkList.validate()


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
        if not isinstance(other, ParagraphLinkCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other