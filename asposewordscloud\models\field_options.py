# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="field_options.py">
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

class FieldOptions(object):
    """DTO for field options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_user': 'UserInformation',
        'custom_toc_style_separator': 'str',
        'default_document_author': 'str',
        'field_index_format': 'str',
        'field_update_culture_name': 'str',
        'field_update_culture_source': 'str',
        'file_name': 'str',
        'is_bidi_text_supported_on_update': 'bool',
        'legacy_number_format': 'bool',
        'pre_process_culture_name': 'str',
        'template_name': 'str',
        'use_invariant_culture_number_format': 'bool',
        'built_in_templates_paths': 'list[str]'
    }

    attribute_map = {
        'current_user': 'CurrentUser',
        'custom_toc_style_separator': 'CustomTocStyleSeparator',
        'default_document_author': 'DefaultDocumentAuthor',
        'field_index_format': 'FieldIndexFormat',
        'field_update_culture_name': 'FieldUpdateCultureName',
        'field_update_culture_source': 'FieldUpdateCultureSource',
        'file_name': 'FileName',
        'is_bidi_text_supported_on_update': 'IsBidiTextSupportedOnUpdate',
        'legacy_number_format': 'LegacyNumberFormat',
        'pre_process_culture_name': 'PreProcessCultureName',
        'template_name': 'TemplateName',
        'use_invariant_culture_number_format': 'UseInvariantCultureNumberFormat',
        'built_in_templates_paths': 'BuiltInTemplatesPaths'
    }

    def __init__(self, current_user=None, custom_toc_style_separator=None, default_document_author=None, field_index_format=None, field_update_culture_name=None, field_update_culture_source=None, file_name=None, is_bidi_text_supported_on_update=None, legacy_number_format=None, pre_process_culture_name=None, template_name=None, use_invariant_culture_number_format=None, built_in_templates_paths=None):  # noqa: E501
        """FieldOptions - a model defined in Swagger"""  # noqa: E501

        self._current_user = None
        self._custom_toc_style_separator = None
        self._default_document_author = None
        self._field_index_format = None
        self._field_update_culture_name = None
        self._field_update_culture_source = None
        self._file_name = None
        self._is_bidi_text_supported_on_update = None
        self._legacy_number_format = None
        self._pre_process_culture_name = None
        self._template_name = None
        self._use_invariant_culture_number_format = None
        self._built_in_templates_paths = None
        self.discriminator = None

        if current_user is not None:
            self.current_user = current_user
        if custom_toc_style_separator is not None:
            self.custom_toc_style_separator = custom_toc_style_separator
        if default_document_author is not None:
            self.default_document_author = default_document_author
        if field_index_format is not None:
            self.field_index_format = field_index_format
        if field_update_culture_name is not None:
            self.field_update_culture_name = field_update_culture_name
        if field_update_culture_source is not None:
            self.field_update_culture_source = field_update_culture_source
        if file_name is not None:
            self.file_name = file_name
        if is_bidi_text_supported_on_update is not None:
            self.is_bidi_text_supported_on_update = is_bidi_text_supported_on_update
        if legacy_number_format is not None:
            self.legacy_number_format = legacy_number_format
        if pre_process_culture_name is not None:
            self.pre_process_culture_name = pre_process_culture_name
        if template_name is not None:
            self.template_name = template_name
        if use_invariant_culture_number_format is not None:
            self.use_invariant_culture_number_format = use_invariant_culture_number_format
        if built_in_templates_paths is not None:
            self.built_in_templates_paths = built_in_templates_paths

    @property
    def current_user(self):
        """Gets the current_user of this FieldOptions.  # noqa: E501

        Gets or sets Current User.  # noqa: E501

        :return: The current_user of this FieldOptions.  # noqa: E501
        :rtype: UserInformation
        """
        return self._current_user

    @current_user.setter
    def current_user(self, current_user):
        """Sets the current_user of this FieldOptions.

        Gets or sets Current User.  # noqa: E501

        :param current_user: The current_user of this FieldOptions.  # noqa: E501
        :type: UserInformation
        """
        self._current_user = current_user

    @property
    def custom_toc_style_separator(self):
        """Gets the custom_toc_style_separator of this FieldOptions.  # noqa: E501

        Gets or sets Custom Toc Style Separator.  # noqa: E501

        :return: The custom_toc_style_separator of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._custom_toc_style_separator

    @custom_toc_style_separator.setter
    def custom_toc_style_separator(self, custom_toc_style_separator):
        """Sets the custom_toc_style_separator of this FieldOptions.

        Gets or sets Custom Toc Style Separator.  # noqa: E501

        :param custom_toc_style_separator: The custom_toc_style_separator of this FieldOptions.  # noqa: E501
        :type: str
        """
        self._custom_toc_style_separator = custom_toc_style_separator

    @property
    def default_document_author(self):
        """Gets the default_document_author of this FieldOptions.  # noqa: E501

        Gets or sets Default Document Author.  # noqa: E501

        :return: The default_document_author of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._default_document_author

    @default_document_author.setter
    def default_document_author(self, default_document_author):
        """Sets the default_document_author of this FieldOptions.

        Gets or sets Default Document Author.  # noqa: E501

        :param default_document_author: The default_document_author of this FieldOptions.  # noqa: E501
        :type: str
        """
        self._default_document_author = default_document_author

    @property
    def field_index_format(self):
        """Gets the field_index_format of this FieldOptions.  # noqa: E501

        Gets or sets Field Index Format.  # noqa: E501

        :return: The field_index_format of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._field_index_format

    @field_index_format.setter
    def field_index_format(self, field_index_format):
        """Sets the field_index_format of this FieldOptions.

        Gets or sets Field Index Format.  # noqa: E501

        :param field_index_format: The field_index_format of this FieldOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["Template", "Classic", "Fancy", "Modern", "Bulleted", "Formal", "Simple"]  # noqa: E501
        if not field_index_format.isdigit():
            if field_index_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `field_index_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(field_index_format, allowed_values))
            self._field_index_format = field_index_format
        else:
            self._field_index_format = allowed_values[int(field_index_format) if six.PY3 else long(field_index_format)]

    @property
    def field_update_culture_name(self):
        """Gets the field_update_culture_name of this FieldOptions.  # noqa: E501

        Gets or sets Field Update Culture Name. It is used for all fields if FieldUpdateCultureSource is FieldCode.  # noqa: E501

        :return: The field_update_culture_name of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._field_update_culture_name

    @field_update_culture_name.setter
    def field_update_culture_name(self, field_update_culture_name):
        """Sets the field_update_culture_name of this FieldOptions.

        Gets or sets Field Update Culture Name. It is used for all fields if FieldUpdateCultureSource is FieldCode.  # noqa: E501

        :param field_update_culture_name: The field_update_culture_name of this FieldOptions.  # noqa: E501
        :type: str
        """
        self._field_update_culture_name = field_update_culture_name

    @property
    def field_update_culture_source(self):
        """Gets the field_update_culture_source of this FieldOptions.  # noqa: E501

        Gets or sets Field Update Culture Source.  # noqa: E501

        :return: The field_update_culture_source of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._field_update_culture_source

    @field_update_culture_source.setter
    def field_update_culture_source(self, field_update_culture_source):
        """Sets the field_update_culture_source of this FieldOptions.

        Gets or sets Field Update Culture Source.  # noqa: E501

        :param field_update_culture_source: The field_update_culture_source of this FieldOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["CurrentThread", "FieldCode"]  # noqa: E501
        if not field_update_culture_source.isdigit():
            if field_update_culture_source not in allowed_values:
                raise ValueError(
                    "Invalid value for `field_update_culture_source` ({0}), must be one of {1}"  # noqa: E501
                    .format(field_update_culture_source, allowed_values))
            self._field_update_culture_source = field_update_culture_source
        else:
            self._field_update_culture_source = allowed_values[int(field_update_culture_source) if six.PY3 else long(field_update_culture_source)]

    @property
    def file_name(self):
        """Gets the file_name of this FieldOptions.  # noqa: E501

        Gets or sets File Name.  # noqa: E501

        :return: The file_name of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FieldOptions.

        Gets or sets File Name.  # noqa: E501

        :param file_name: The file_name of this FieldOptions.  # noqa: E501
        :type: str
        """
        self._file_name = file_name

    @property
    def is_bidi_text_supported_on_update(self):
        """Gets the is_bidi_text_supported_on_update of this FieldOptions.  # noqa: E501

        Gets or sets if Bidi Text Supported OnUpdate.  # noqa: E501

        :return: The is_bidi_text_supported_on_update of this FieldOptions.  # noqa: E501
        :rtype: bool
        """
        return self._is_bidi_text_supported_on_update

    @is_bidi_text_supported_on_update.setter
    def is_bidi_text_supported_on_update(self, is_bidi_text_supported_on_update):
        """Sets the is_bidi_text_supported_on_update of this FieldOptions.

        Gets or sets if Bidi Text Supported OnUpdate.  # noqa: E501

        :param is_bidi_text_supported_on_update: The is_bidi_text_supported_on_update of this FieldOptions.  # noqa: E501
        :type: bool
        """
        self._is_bidi_text_supported_on_update = is_bidi_text_supported_on_update

    @property
    def legacy_number_format(self):
        """Gets the legacy_number_format of this FieldOptions.  # noqa: E501

        Gets or sets if Legacy Number Format.  # noqa: E501

        :return: The legacy_number_format of this FieldOptions.  # noqa: E501
        :rtype: bool
        """
        return self._legacy_number_format

    @legacy_number_format.setter
    def legacy_number_format(self, legacy_number_format):
        """Sets the legacy_number_format of this FieldOptions.

        Gets or sets if Legacy Number Format.  # noqa: E501

        :param legacy_number_format: The legacy_number_format of this FieldOptions.  # noqa: E501
        :type: bool
        """
        self._legacy_number_format = legacy_number_format

    @property
    def pre_process_culture_name(self):
        """Gets the pre_process_culture_name of this FieldOptions.  # noqa: E501

        Gets or sets PreProcess Culture Name. It is a culture code for DOC fields.  # noqa: E501

        :return: The pre_process_culture_name of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._pre_process_culture_name

    @pre_process_culture_name.setter
    def pre_process_culture_name(self, pre_process_culture_name):
        """Sets the pre_process_culture_name of this FieldOptions.

        Gets or sets PreProcess Culture Name. It is a culture code for DOC fields.  # noqa: E501

        :param pre_process_culture_name: The pre_process_culture_name of this FieldOptions.  # noqa: E501
        :type: str
        """
        self._pre_process_culture_name = pre_process_culture_name

    @property
    def template_name(self):
        """Gets the template_name of this FieldOptions.  # noqa: E501

        Gets or sets Template Name.  # noqa: E501

        :return: The template_name of this FieldOptions.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this FieldOptions.

        Gets or sets Template Name.  # noqa: E501

        :param template_name: The template_name of this FieldOptions.  # noqa: E501
        :type: str
        """
        self._template_name = template_name

    @property
    def use_invariant_culture_number_format(self):
        """Gets the use_invariant_culture_number_format of this FieldOptions.  # noqa: E501

        Gets or sets if Use Invariant Culture Number Format.  # noqa: E501

        :return: The use_invariant_culture_number_format of this FieldOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_invariant_culture_number_format

    @use_invariant_culture_number_format.setter
    def use_invariant_culture_number_format(self, use_invariant_culture_number_format):
        """Sets the use_invariant_culture_number_format of this FieldOptions.

        Gets or sets if Use Invariant Culture Number Format.  # noqa: E501

        :param use_invariant_culture_number_format: The use_invariant_culture_number_format of this FieldOptions.  # noqa: E501
        :type: bool
        """
        self._use_invariant_culture_number_format = use_invariant_culture_number_format

    @property
    def built_in_templates_paths(self):
        """Gets the built_in_templates_paths of this FieldOptions.  # noqa: E501

        Gets or sets BuiltIn Templates Paths.  # noqa: E501

        :return: The built_in_templates_paths of this FieldOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._built_in_templates_paths

    @built_in_templates_paths.setter
    def built_in_templates_paths(self, built_in_templates_paths):
        """Sets the built_in_templates_paths of this FieldOptions.

        Gets or sets BuiltIn Templates Paths.  # noqa: E501

        :param built_in_templates_paths: The built_in_templates_paths of this FieldOptions.  # noqa: E501
        :type: list[str]
        """
        self._built_in_templates_paths = built_in_templates_paths


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""

        if self._current_user is not None:
            self._current_user.validate()














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
        if not isinstance(other, FieldOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other