# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="office_math_object.py">
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

class OfficeMathObject(object):
    """DTO container with an OfficeMath object.
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
        'content': 'StoryChildNodes',
        'display_type': 'str',
        'justification': 'str',
        'math_object_type': 'str'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'content': 'Content',
        'display_type': 'DisplayType',
        'justification': 'Justification',
        'math_object_type': 'MathObjectType'
    }

    def __init__(self, link=None, node_id=None, content=None, display_type=None, justification=None, math_object_type=None):  # noqa: E501
        """OfficeMathObject - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._content = None
        self._display_type = None
        self._justification = None
        self._math_object_type = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if content is not None:
            self.content = content
        if display_type is not None:
            self.display_type = display_type
        if justification is not None:
            self.justification = justification
        if math_object_type is not None:
            self.math_object_type = math_object_type

    @property
    def link(self):
        """Gets the link of this OfficeMathObject.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this OfficeMathObject.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this OfficeMathObject.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this OfficeMathObject.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this OfficeMathObject.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this OfficeMathObject.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this OfficeMathObject.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this OfficeMathObject.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def content(self):
        """Gets the content of this OfficeMathObject.  # noqa: E501

        Gets or sets the content of a footnote.  # noqa: E501

        :return: The content of this OfficeMathObject.  # noqa: E501
        :rtype: StoryChildNodes
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this OfficeMathObject.

        Gets or sets the content of a footnote.  # noqa: E501

        :param content: The content of this OfficeMathObject.  # noqa: E501
        :type: StoryChildNodes
        """
        self._content = content

    @property
    def display_type(self):
        """Gets the display_type of this OfficeMathObject.  # noqa: E501

        Gets or sets the display format type of the OfficeMath object. This display format defines whether an equation is displayed inline with the text or displayed on its own line. Display format type has effect for top level Office Math only.Returned display format type is always Inline for nested Office Math.  # noqa: E501

        :return: The display_type of this OfficeMathObject.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this OfficeMathObject.

        Gets or sets the display format type of the OfficeMath object. This display format defines whether an equation is displayed inline with the text or displayed on its own line. Display format type has effect for top level Office Math only.Returned display format type is always Inline for nested Office Math.  # noqa: E501

        :param display_type: The display_type of this OfficeMathObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["Display", "Inline"]  # noqa: E501
        if not display_type.isdigit():
            if display_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `display_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(display_type, allowed_values))
            self._display_type = display_type
        else:
            self._display_type = allowed_values[int(display_type) if six.PY3 else long(display_type)]

    @property
    def justification(self):
        """Gets the justification of this OfficeMathObject.  # noqa: E501

        Gets or sets the justification of the OfficeMath object. Justification cannot be set to the Office Math with display format type Inline.Inline justification cannot be set to the Office Math with display format type Display.Corresponding DisplayType has to be set before setting Office Math justification.  # noqa: E501

        :return: The justification of this OfficeMathObject.  # noqa: E501
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """Sets the justification of this OfficeMathObject.

        Gets or sets the justification of the OfficeMath object. Justification cannot be set to the Office Math with display format type Inline.Inline justification cannot be set to the Office Math with display format type Display.Corresponding DisplayType has to be set before setting Office Math justification.  # noqa: E501

        :param justification: The justification of this OfficeMathObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["CenterGroup", "Default", "Center", "Left", "Right", "Inline"]  # noqa: E501
        if not justification.isdigit():
            if justification not in allowed_values:
                raise ValueError(
                    "Invalid value for `justification` ({0}), must be one of {1}"  # noqa: E501
                    .format(justification, allowed_values))
            self._justification = justification
        else:
            self._justification = allowed_values[int(justification) if six.PY3 else long(justification)]

    @property
    def math_object_type(self):
        """Gets the math_object_type of this OfficeMathObject.  # noqa: E501

        Gets or sets the type of the OfficeMath object.  # noqa: E501

        :return: The math_object_type of this OfficeMathObject.  # noqa: E501
        :rtype: str
        """
        return self._math_object_type

    @math_object_type.setter
    def math_object_type(self, math_object_type):
        """Sets the math_object_type of this OfficeMathObject.

        Gets or sets the type of the OfficeMath object.  # noqa: E501

        :param math_object_type: The math_object_type of this OfficeMathObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["OMath", "OMathPara", "Accent", "Bar", "BorderBox", "Box", "Delimiter", "Degree", "Argument", "Array", "Fraction", "Denominator", "Numerator", "Function", "FunctionName", "GroupCharacter", "Limit", "LowerLimit", "UpperLimit", "Matrix", "MatrixRow", "NAry", "Phantom", "Radical", "SubscriptPart", "SuperscriptPart", "PreSubSuperscript", "Subscript", "SubSuperscript", "Superscript", "None"]  # noqa: E501
        if not math_object_type.isdigit():
            if math_object_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `math_object_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(math_object_type, allowed_values))
            self._math_object_type = math_object_type
        else:
            self._math_object_type = allowed_values[int(math_object_type) if six.PY3 else long(math_object_type)]


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._link is not None:
            self._link.validate()




        if self._content is not None:
            self._content.validate()





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
        if not isinstance(other, OfficeMathObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other