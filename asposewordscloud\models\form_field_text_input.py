# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="form_field_text_input.py">
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

class FormFieldTextInput(object):
    """FormField text input element.
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
        'name': 'str',
        'enabled': 'bool',
        'status_text': 'str',
        'own_status': 'bool',
        'help_text': 'str',
        'own_help': 'bool',
        'calculate_on_exit': 'bool',
        'entry_macro': 'str',
        'exit_macro': 'str',
        'text_input_format': 'str',
        'text_input_type': 'str',
        'text_input_default': 'str',
        'max_length': 'int'
    }

    attribute_map = {
        'link': 'Link',
        'node_id': 'NodeId',
        'name': 'Name',
        'enabled': 'Enabled',
        'status_text': 'StatusText',
        'own_status': 'OwnStatus',
        'help_text': 'HelpText',
        'own_help': 'OwnHelp',
        'calculate_on_exit': 'CalculateOnExit',
        'entry_macro': 'EntryMacro',
        'exit_macro': 'ExitMacro',
        'text_input_format': 'TextInputFormat',
        'text_input_type': 'TextInputType',
        'text_input_default': 'TextInputDefault',
        'max_length': 'MaxLength'
    }

    def __init__(self, link=None, node_id=None, name=None, enabled=None, status_text=None, own_status=None, help_text=None, own_help=None, calculate_on_exit=None, entry_macro=None, exit_macro=None, text_input_format=None, text_input_type=None, text_input_default=None, max_length=None):  # noqa: E501
        """FormFieldTextInput - a model defined in Swagger"""  # noqa: E501

        self._link = None
        self._node_id = None
        self._name = None
        self._enabled = None
        self._status_text = None
        self._own_status = None
        self._help_text = None
        self._own_help = None
        self._calculate_on_exit = None
        self._entry_macro = None
        self._exit_macro = None
        self._text_input_format = None
        self._text_input_type = None
        self._text_input_default = None
        self._max_length = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if node_id is not None:
            self.node_id = node_id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if status_text is not None:
            self.status_text = status_text
        if own_status is not None:
            self.own_status = own_status
        if help_text is not None:
            self.help_text = help_text
        if own_help is not None:
            self.own_help = own_help
        if calculate_on_exit is not None:
            self.calculate_on_exit = calculate_on_exit
        if entry_macro is not None:
            self.entry_macro = entry_macro
        if exit_macro is not None:
            self.exit_macro = exit_macro
        if text_input_format is not None:
            self.text_input_format = text_input_format
        if text_input_type is not None:
            self.text_input_type = text_input_type
        if text_input_default is not None:
            self.text_input_default = text_input_default
        if max_length is not None:
            self.max_length = max_length

    @property
    def link(self):
        """Gets the link of this FormFieldTextInput.  # noqa: E501

        Gets or sets the link to the document.  # noqa: E501

        :return: The link of this FormFieldTextInput.  # noqa: E501
        :rtype: WordsApiLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this FormFieldTextInput.

        Gets or sets the link to the document.  # noqa: E501

        :param link: The link of this FormFieldTextInput.  # noqa: E501
        :type: WordsApiLink
        """
        self._link = link

    @property
    def node_id(self):
        """Gets the node_id of this FormFieldTextInput.  # noqa: E501

        Gets or sets the node id.  # noqa: E501

        :return: The node_id of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this FormFieldTextInput.

        Gets or sets the node id.  # noqa: E501

        :param node_id: The node_id of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._node_id = node_id

    @property
    def name(self):
        """Gets the name of this FormFieldTextInput.  # noqa: E501

        Gets or sets the form field name.  # noqa: E501

        :return: The name of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormFieldTextInput.

        Gets or sets the form field name.  # noqa: E501

        :param name: The name of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this FormFieldTextInput.  # noqa: E501

        Gets or sets a value indicating whether a form field is enabled. If a form field is enabled, its contents can be changed as the form is filled in.  # noqa: E501

        :return: The enabled of this FormFieldTextInput.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this FormFieldTextInput.

        Gets or sets a value indicating whether a form field is enabled. If a form field is enabled, its contents can be changed as the form is filled in.  # noqa: E501

        :param enabled: The enabled of this FormFieldTextInput.  # noqa: E501
        :type: bool
        """
        self._enabled = enabled

    @property
    def status_text(self):
        """Gets the status_text of this FormFieldTextInput.  # noqa: E501

        Gets or sets text, displayed in the status bar when a form field has the focus. If the OwnStatus property is set to true, the StatusText property specifies the status bar text. If the OwnStatus property is set to false, the StatusText property specifies the name of an AutoText entry that contains status bar text for the form field.  # noqa: E501

        :return: The status_text of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        """Sets the status_text of this FormFieldTextInput.

        Gets or sets text, displayed in the status bar when a form field has the focus. If the OwnStatus property is set to true, the StatusText property specifies the status bar text. If the OwnStatus property is set to false, the StatusText property specifies the name of an AutoText entry that contains status bar text for the form field.  # noqa: E501

        :param status_text: The status_text of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._status_text = status_text

    @property
    def own_status(self):
        """Gets the own_status of this FormFieldTextInput.  # noqa: E501

        Gets or sets a value indicating whether the source of the text that's displayed in the status bar when a form field has the focus. If true, the text specified by the StatusText property is displayed. If false, the text of the AutoText entry specified by the StatusText property is displayed.  # noqa: E501

        :return: The own_status of this FormFieldTextInput.  # noqa: E501
        :rtype: bool
        """
        return self._own_status

    @own_status.setter
    def own_status(self, own_status):
        """Sets the own_status of this FormFieldTextInput.

        Gets or sets a value indicating whether the source of the text that's displayed in the status bar when a form field has the focus. If true, the text specified by the StatusText property is displayed. If false, the text of the AutoText entry specified by the StatusText property is displayed.  # noqa: E501

        :param own_status: The own_status of this FormFieldTextInput.  # noqa: E501
        :type: bool
        """
        self._own_status = own_status

    @property
    def help_text(self):
        """Gets the help_text of this FormFieldTextInput.  # noqa: E501

        Gets or sets text, displayed in a message box when the form field has the focus and the user presses F1. If the OwnHelp property is set to True, HelpText specifies the text string value. If OwnHelp is set to False, HelpText specifies the name of an AutoText entry that contains help text for the form field.  # noqa: E501

        :return: The help_text of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """Sets the help_text of this FormFieldTextInput.

        Gets or sets text, displayed in a message box when the form field has the focus and the user presses F1. If the OwnHelp property is set to True, HelpText specifies the text string value. If OwnHelp is set to False, HelpText specifies the name of an AutoText entry that contains help text for the form field.  # noqa: E501

        :param help_text: The help_text of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._help_text = help_text

    @property
    def own_help(self):
        """Gets the own_help of this FormFieldTextInput.  # noqa: E501

        Gets or sets a value indicating whether the source of the text that's displayed in a message box when a form field has the focus and the user presses F1. If true, the text specified by the HelpText property is displayed. If False, the text in the AutoText entry specified by the HelpText property is displayed.  # noqa: E501

        :return: The own_help of this FormFieldTextInput.  # noqa: E501
        :rtype: bool
        """
        return self._own_help

    @own_help.setter
    def own_help(self, own_help):
        """Sets the own_help of this FormFieldTextInput.

        Gets or sets a value indicating whether the source of the text that's displayed in a message box when a form field has the focus and the user presses F1. If true, the text specified by the HelpText property is displayed. If False, the text in the AutoText entry specified by the HelpText property is displayed.  # noqa: E501

        :param own_help: The own_help of this FormFieldTextInput.  # noqa: E501
        :type: bool
        """
        self._own_help = own_help

    @property
    def calculate_on_exit(self):
        """Gets the calculate_on_exit of this FormFieldTextInput.  # noqa: E501

        Gets or sets a value indicating whether references to the specified form field are automatically updated whenever the field is exited. Setting CalculateOnExit only affects the behavior of the form field when the document is opened in Microsoft Word. Aspose.Words never updates references to the form field.  # noqa: E501

        :return: The calculate_on_exit of this FormFieldTextInput.  # noqa: E501
        :rtype: bool
        """
        return self._calculate_on_exit

    @calculate_on_exit.setter
    def calculate_on_exit(self, calculate_on_exit):
        """Sets the calculate_on_exit of this FormFieldTextInput.

        Gets or sets a value indicating whether references to the specified form field are automatically updated whenever the field is exited. Setting CalculateOnExit only affects the behavior of the form field when the document is opened in Microsoft Word. Aspose.Words never updates references to the form field.  # noqa: E501

        :param calculate_on_exit: The calculate_on_exit of this FormFieldTextInput.  # noqa: E501
        :type: bool
        """
        self._calculate_on_exit = calculate_on_exit

    @property
    def entry_macro(self):
        """Gets the entry_macro of this FormFieldTextInput.  # noqa: E501

        Gets or sets the entry macro name for the form field. The entry macro runs when the form field gets the focus in Microsoft Word.  # noqa: E501

        :return: The entry_macro of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._entry_macro

    @entry_macro.setter
    def entry_macro(self, entry_macro):
        """Sets the entry_macro of this FormFieldTextInput.

        Gets or sets the entry macro name for the form field. The entry macro runs when the form field gets the focus in Microsoft Word.  # noqa: E501

        :param entry_macro: The entry_macro of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._entry_macro = entry_macro

    @property
    def exit_macro(self):
        """Gets the exit_macro of this FormFieldTextInput.  # noqa: E501

        Gets or sets the exit macro name for the form field. The exit macro runs when the form field loses the focus in Microsoft Word.  # noqa: E501

        :return: The exit_macro of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._exit_macro

    @exit_macro.setter
    def exit_macro(self, exit_macro):
        """Sets the exit_macro of this FormFieldTextInput.

        Gets or sets the exit macro name for the form field. The exit macro runs when the form field loses the focus in Microsoft Word.  # noqa: E501

        :param exit_macro: The exit_macro of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._exit_macro = exit_macro

    @property
    def text_input_format(self):
        """Gets the text_input_format of this FormFieldTextInput.  # noqa: E501

        Gets or sets text formatting for the text form field. If the text form field contains regular text, then valid format strings are "", "UPPERCASE", "LOWERCASE", "FIRST CAPITAL" and "TITLE CASE". The strings are case-insensitive.If the text form field contains a number or a date/time value, then valid format strings are number or date and time format strings.  # noqa: E501

        :return: The text_input_format of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._text_input_format

    @text_input_format.setter
    def text_input_format(self, text_input_format):
        """Sets the text_input_format of this FormFieldTextInput.

        Gets or sets text formatting for the text form field. If the text form field contains regular text, then valid format strings are "", "UPPERCASE", "LOWERCASE", "FIRST CAPITAL" and "TITLE CASE". The strings are case-insensitive.If the text form field contains a number or a date/time value, then valid format strings are number or date and time format strings.  # noqa: E501

        :param text_input_format: The text_input_format of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._text_input_format = text_input_format

    @property
    def text_input_type(self):
        """Gets the text_input_type of this FormFieldTextInput.  # noqa: E501

        Gets or sets the type of the text form field.  # noqa: E501

        :return: The text_input_type of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._text_input_type

    @text_input_type.setter
    def text_input_type(self, text_input_type):
        """Sets the text_input_type of this FormFieldTextInput.

        Gets or sets the type of the text form field.  # noqa: E501

        :param text_input_type: The text_input_type of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Regular", "Number", "Date", "CurrentDate", "CurrentTime", "Calculated"]  # noqa: E501
        if not text_input_type.isdigit():
            if text_input_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `text_input_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(text_input_type, allowed_values))
            self._text_input_type = text_input_type
        else:
            self._text_input_type = allowed_values[int(text_input_type) if six.PY3 else long(text_input_type)]

    @property
    def text_input_default(self):
        """Gets the text_input_default of this FormFieldTextInput.  # noqa: E501

        Gets or sets the default string or a calculation expression of the text form field. The meaning of this property depends on the value of the TextInputType property.When TextInputType is Regular or Number, this string specifies the default string for the text form field. This string is the content that Microsoft Word will display in the document when the form field is empty.When TextInputType is Calculated, then this string holds the expression to be calculated. The expression needs to be a formula valid according to Microsoft Word formula field requirements. When you set a new expression using this property, Aspose.Words calculates the formula result automatically and inserts it into the form field.  # noqa: E501

        :return: The text_input_default of this FormFieldTextInput.  # noqa: E501
        :rtype: str
        """
        return self._text_input_default

    @text_input_default.setter
    def text_input_default(self, text_input_default):
        """Sets the text_input_default of this FormFieldTextInput.

        Gets or sets the default string or a calculation expression of the text form field. The meaning of this property depends on the value of the TextInputType property.When TextInputType is Regular or Number, this string specifies the default string for the text form field. This string is the content that Microsoft Word will display in the document when the form field is empty.When TextInputType is Calculated, then this string holds the expression to be calculated. The expression needs to be a formula valid according to Microsoft Word formula field requirements. When you set a new expression using this property, Aspose.Words calculates the formula result automatically and inserts it into the form field.  # noqa: E501

        :param text_input_default: The text_input_default of this FormFieldTextInput.  # noqa: E501
        :type: str
        """
        self._text_input_default = text_input_default

    @property
    def max_length(self):
        """Gets the max_length of this FormFieldTextInput.  # noqa: E501

        Gets or sets the maximum length for the text field. Zero when the length is not limited.  # noqa: E501

        :return: The max_length of this FormFieldTextInput.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this FormFieldTextInput.

        Gets or sets the maximum length for the text field. Zero when the length is not limited.  # noqa: E501

        :param max_length: The max_length of this FormFieldTextInput.  # noqa: E501
        :type: int
        """
        self._max_length = max_length


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._name is None:
            raise ValueError("Property Name in FormFieldTextInput is required.")  # noqa: E501
        if self._text_input_format is None:
            raise ValueError("Property TextInputFormat in FormFieldTextInput is required.")  # noqa: E501
        if self._text_input_default is None:
            raise ValueError("Property TextInputDefault in FormFieldTextInput is required.")  # noqa: E501

        if self._link is not None:
            self._link.validate()
















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
        if not isinstance(other, FormFieldTextInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other