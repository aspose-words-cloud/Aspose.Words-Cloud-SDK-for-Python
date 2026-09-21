# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="list_info.py">
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

class ListInfo(object):
    """DTO container with a single document list.
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
        'list_id': 'int',
        'is_multi_level': 'bool',
        'is_restart_at_each_section': 'bool',
        'is_list_style_definition': 'bool',
        'is_list_style_reference': 'bool',
        'style': 'Style',
        'list_levels': 'ListLevels'
    }

    attribute_map = {
        'link': 'Link',
        'list_id': 'ListId',
        'is_multi_level': 'IsMultiLevel',
        'is_restart_at_each_section': 'IsRestartAtEachSection',
        'is_list_style_definition': 'IsListStyleDefinition',
        'is_list_style_reference': 'IsListStyleReference',
        'style': 'Style',
        'list_levels': 'ListLevels'
    }

    def __init__(self, link=None, list_id=None, is_multi_level=None, is_restart_at_each_section=None, is_list_style_definition=None, is_list_style_reference=None, style=None, list_levels=None):  # noqa: E501
        """ListInfo - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._list_id = None
        self._is_multi_level = None
        self._is_restart_at_each_section = None
        self._is_list_style_definition = None
        self._is_list_style_reference = None
        self._style = None
        self._list_levels = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if list_id is not None:
            self.list_id = list_id
        if is_multi_level is not None:
            self.is_multi_level = is_multi_level
        if is_restart_at_each_section is not None:
            self.is_restart_at_each_section = is_restart_at_each_section
        if is_list_style_definition is not None:
            self.is_list_style_definition = is_list_style_definition
        if is_list_style_reference is not None:
            self.is_list_style_reference = is_list_style_reference
        if style is not None:
            self.style = style
        if list_levels is not None:
            self.list_levels = list_levels

    @property
    def link(self):
        """Gets the link of this ListInfo.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this ListInfo.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ListInfo.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this ListInfo.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def list_id(self):
        """Gets the list_id of this ListInfo.  # noqa: E501

        Gets or sets the unique identifier of the list. You do not normally need to use this property. But if you use it, you normally do so in conjunction with the Aspose.Words.Lists.ListCollection.GetListByListId(System.Int32) method to find a list by its identifier.  # noqa: E501

        :return: The list_id of this ListInfo.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this ListInfo.

        Gets or sets the unique identifier of the list. You do not normally need to use this property. But if you use it, you normally do so in conjunction with the Aspose.Words.Lists.ListCollection.GetListByListId(System.Int32) method to find a list by its identifier.  # noqa: E501

        :param list_id: The list_id of this ListInfo.  # noqa: E501
        :type: int
        """
        self._list_id = list_id

    @property
    def is_multi_level(self):
        """Gets the is_multi_level of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether the list contains 9 levels; false when 1 level. The lists that you create with Aspose.Words are always multi-level lists and contain 9 levels. Microsoft Word 2003 and later always create multi-level lists with 9 levels. But in some documents, created with earlier versions of Microsoft Word you might encounter lists that have 1 level only.  # noqa: E501

        :return: The is_multi_level of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_multi_level

    @is_multi_level.setter
    def is_multi_level(self, is_multi_level):
        """Sets the is_multi_level of this ListInfo.

        Gets or sets a value indicating whether the list contains 9 levels; false when 1 level. The lists that you create with Aspose.Words are always multi-level lists and contain 9 levels. Microsoft Word 2003 and later always create multi-level lists with 9 levels. But in some documents, created with earlier versions of Microsoft Word you might encounter lists that have 1 level only.  # noqa: E501

        :param is_multi_level: The is_multi_level of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_multi_level = is_multi_level

    @property
    def is_restart_at_each_section(self):
        """Gets the is_restart_at_each_section of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether list should be restarted at each section. The default value is false. This option is supported only in RTF, DOC and DOCX document formats. This option will be written to DOCX only if Aspose.Words.Saving.OoxmlCompliance is higher then Aspose.Words.Saving.OoxmlCompliance.Ecma376_2006.  # noqa: E501

        :return: The is_restart_at_each_section of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_restart_at_each_section

    @is_restart_at_each_section.setter
    def is_restart_at_each_section(self, is_restart_at_each_section):
        """Sets the is_restart_at_each_section of this ListInfo.

        Gets or sets a value indicating whether list should be restarted at each section. The default value is false. This option is supported only in RTF, DOC and DOCX document formats. This option will be written to DOCX only if Aspose.Words.Saving.OoxmlCompliance is higher then Aspose.Words.Saving.OoxmlCompliance.Ecma376_2006.  # noqa: E501

        :param is_restart_at_each_section: The is_restart_at_each_section of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_restart_at_each_section = is_restart_at_each_section

    @property
    def is_list_style_definition(self):
        """Gets the is_list_style_definition of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether this list is a definition of a list style. When this property is true, the Aspose.Words.Lists.List.Style property returns the list style that this list defines. By modifying properties of a list that defines a list style, you modify The properties of the list style. A list that is a definition of a list style cannot be applied directly to paragraphs to make them numbered. Aspose.Words.Lists.List.Style Aspose.Words.Lists.List.IsListStyleReference.  # noqa: E501

        :return: The is_list_style_definition of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_list_style_definition

    @is_list_style_definition.setter
    def is_list_style_definition(self, is_list_style_definition):
        """Sets the is_list_style_definition of this ListInfo.

        Gets or sets a value indicating whether this list is a definition of a list style. When this property is true, the Aspose.Words.Lists.List.Style property returns the list style that this list defines. By modifying properties of a list that defines a list style, you modify The properties of the list style. A list that is a definition of a list style cannot be applied directly to paragraphs to make them numbered. Aspose.Words.Lists.List.Style Aspose.Words.Lists.List.IsListStyleReference.  # noqa: E501

        :param is_list_style_definition: The is_list_style_definition of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_list_style_definition = is_list_style_definition

    @property
    def is_list_style_reference(self):
        """Gets the is_list_style_reference of this ListInfo.  # noqa: E501

        Gets or sets a value indicating whether this list is a reference to a list style. Note, modifying properties of a list that is a reference to list style has no effect. The list formatting specified in the list style itself always takes precedence. Aspose.Words.Lists.List.Style Aspose.Words.Lists.List.IsListStyleDefinition.  # noqa: E501

        :return: The is_list_style_reference of this ListInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_list_style_reference

    @is_list_style_reference.setter
    def is_list_style_reference(self, is_list_style_reference):
        """Sets the is_list_style_reference of this ListInfo.

        Gets or sets a value indicating whether this list is a reference to a list style. Note, modifying properties of a list that is a reference to list style has no effect. The list formatting specified in the list style itself always takes precedence. Aspose.Words.Lists.List.Style Aspose.Words.Lists.List.IsListStyleDefinition.  # noqa: E501

        :param is_list_style_reference: The is_list_style_reference of this ListInfo.  # noqa: E501
        :type: bool
        """
        self._is_list_style_reference = is_list_style_reference

    @property
    def style(self):
        """Gets the style of this ListInfo.  # noqa: E501

        Gets or sets the list style that this list references or defines. If this list is not associated with a list style, the property will return null. A list could be a reference to a list style, in this case Aspose.Words.Lists.List.IsListStyleReference will be true. A list could be a definition of a list style, in this case Aspose.Words.Lists.List.IsListStyleDefinition will be true. Such a list cannot be applied to paragraphs in the document directly.  # noqa: E501

        :return: The style of this ListInfo.  # noqa: E501
        :rtype: Style
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this ListInfo.

        Gets or sets the list style that this list references or defines. If this list is not associated with a list style, the property will return null. A list could be a reference to a list style, in this case Aspose.Words.Lists.List.IsListStyleReference will be true. A list could be a definition of a list style, in this case Aspose.Words.Lists.List.IsListStyleDefinition will be true. Such a list cannot be applied to paragraphs in the document directly.  # noqa: E501

        :param style: The style of this ListInfo.  # noqa: E501
        :type: Style
        """
        self._style = style

    @property
    def list_levels(self):
        """Gets the list_levels of this ListInfo.  # noqa: E501

        Gets or sets the collection of list levels for this list. Use this property to access and modify formatting individual to each level of the list.  # noqa: E501

        :return: The list_levels of this ListInfo.  # noqa: E501
        :rtype: ListLevels
        """
        return self._list_levels

    @list_levels.setter
    def list_levels(self, list_levels):
        """Sets the list_levels of this ListInfo.

        Gets or sets the collection of list levels for this list. Use this property to access and modify formatting individual to each level of the list.  # noqa: E501

        :param list_levels: The list_levels of this ListInfo.  # noqa: E501
        :type: ListLevels
        """
        self._list_levels = list_levels


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._list_id is None:
            raise ValueError("Property ListId in ListInfo is required.")  # noqa: E501
        if self._is_multi_level is None:
            raise ValueError("Property IsMultiLevel in ListInfo is required.")  # noqa: E501
        if self._is_restart_at_each_section is None:
            raise ValueError("Property IsRestartAtEachSection in ListInfo is required.")  # noqa: E501
        if self._is_list_style_definition is None:
            raise ValueError("Property IsListStyleDefinition in ListInfo is required.")  # noqa: E501
        if self._is_list_style_reference is None:
            raise ValueError("Property IsListStyleReference in ListInfo is required.")  # noqa: E501

        if self._link is not None:
            self._link.validate()








        if self._style is not None:
            self._style.validate()



        if self._list_levels is not None:
            self._list_levels.validate()


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
        if not isinstance(other, ListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other