# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="compare_options.py">
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

class CompareOptions(object):
    """DTO container with compare documents options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accept_all_revisions_before_comparison': 'bool',
        'granularity': 'str',
        'ignore_case_changes': 'bool',
        'ignore_comments': 'bool',
        'ignore_fields': 'bool',
        'ignore_footnotes': 'bool',
        'ignore_formatting': 'bool',
        'ignore_headers_and_footers': 'bool',
        'ignore_tables': 'bool',
        'ignore_textboxes': 'bool',
        'target': 'str'
    }

    attribute_map = {
        'accept_all_revisions_before_comparison': 'AcceptAllRevisionsBeforeComparison',
        'granularity': 'Granularity',
        'ignore_case_changes': 'IgnoreCaseChanges',
        'ignore_comments': 'IgnoreComments',
        'ignore_fields': 'IgnoreFields',
        'ignore_footnotes': 'IgnoreFootnotes',
        'ignore_formatting': 'IgnoreFormatting',
        'ignore_headers_and_footers': 'IgnoreHeadersAndFooters',
        'ignore_tables': 'IgnoreTables',
        'ignore_textboxes': 'IgnoreTextboxes',
        'target': 'Target'
    }

    def __init__(self, accept_all_revisions_before_comparison=None, granularity=None, ignore_case_changes=None, ignore_comments=None, ignore_fields=None, ignore_footnotes=None, ignore_formatting=None, ignore_headers_and_footers=None, ignore_tables=None, ignore_textboxes=None, target=None):  # noqa: E501
        """CompareOptions - a model defined in Swagger"""  # noqa: E501

        self._accept_all_revisions_before_comparison = None
        self._granularity = None
        self._ignore_case_changes = None
        self._ignore_comments = None
        self._ignore_fields = None
        self._ignore_footnotes = None
        self._ignore_formatting = None
        self._ignore_headers_and_footers = None
        self._ignore_tables = None
        self._ignore_textboxes = None
        self._target = None
        self.discriminator = None

        if accept_all_revisions_before_comparison is not None:
            self.accept_all_revisions_before_comparison = accept_all_revisions_before_comparison
        if granularity is not None:
            self.granularity = granularity
        if ignore_case_changes is not None:
            self.ignore_case_changes = ignore_case_changes
        if ignore_comments is not None:
            self.ignore_comments = ignore_comments
        if ignore_fields is not None:
            self.ignore_fields = ignore_fields
        if ignore_footnotes is not None:
            self.ignore_footnotes = ignore_footnotes
        if ignore_formatting is not None:
            self.ignore_formatting = ignore_formatting
        if ignore_headers_and_footers is not None:
            self.ignore_headers_and_footers = ignore_headers_and_footers
        if ignore_tables is not None:
            self.ignore_tables = ignore_tables
        if ignore_textboxes is not None:
            self.ignore_textboxes = ignore_textboxes
        if target is not None:
            self.target = target

    @property
    def accept_all_revisions_before_comparison(self):
        """Gets the accept_all_revisions_before_comparison of this CompareOptions.  # noqa: E501

        Gets or sets whether accept revisions before comparison or not.  # noqa: E501

        :return: The accept_all_revisions_before_comparison of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._accept_all_revisions_before_comparison

    @accept_all_revisions_before_comparison.setter
    def accept_all_revisions_before_comparison(self, accept_all_revisions_before_comparison):
        """Sets the accept_all_revisions_before_comparison of this CompareOptions.

        Gets or sets whether accept revisions before comparison or not.  # noqa: E501

        :param accept_all_revisions_before_comparison: The accept_all_revisions_before_comparison of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._accept_all_revisions_before_comparison = accept_all_revisions_before_comparison

    @property
    def granularity(self):
        """Gets the granularity of this CompareOptions.  # noqa: E501

        Gets or sets the option indicating whether changes are tracked by character or by word.  # noqa: E501

        :return: The granularity of this CompareOptions.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this CompareOptions.

        Gets or sets the option indicating whether changes are tracked by character or by word.  # noqa: E501

        :param granularity: The granularity of this CompareOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["CharLevel", "WordLevel"]  # noqa: E501
        if not granularity.isdigit():
            if granularity not in allowed_values:
                raise ValueError(
                    "Invalid value for `granularity` ({0}), must be one of {1}"  # noqa: E501
                    .format(granularity, allowed_values))
            self._granularity = granularity
        else:
            self._granularity = allowed_values[int(granularity) if six.PY3 else long(granularity)]

    @property
    def ignore_case_changes(self):
        """Gets the ignore_case_changes of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether documents comparison is case insensitive. By default comparison is case sensitive.  # noqa: E501

        :return: The ignore_case_changes of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_case_changes

    @ignore_case_changes.setter
    def ignore_case_changes(self, ignore_case_changes):
        """Sets the ignore_case_changes of this CompareOptions.

        Gets or sets a value indicating whether documents comparison is case insensitive. By default comparison is case sensitive.  # noqa: E501

        :param ignore_case_changes: The ignore_case_changes of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_case_changes = ignore_case_changes

    @property
    def ignore_comments(self):
        """Gets the ignore_comments of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether comments content is ignored. By default comments are not ignored.  # noqa: E501

        :return: The ignore_comments of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_comments

    @ignore_comments.setter
    def ignore_comments(self, ignore_comments):
        """Sets the ignore_comments of this CompareOptions.

        Gets or sets a value indicating whether comments content is ignored. By default comments are not ignored.  # noqa: E501

        :param ignore_comments: The ignore_comments of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_comments = ignore_comments

    @property
    def ignore_fields(self):
        """Gets the ignore_fields of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether fields content is ignored. By default fields are not ignored.  # noqa: E501

        :return: The ignore_fields of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_fields

    @ignore_fields.setter
    def ignore_fields(self, ignore_fields):
        """Sets the ignore_fields of this CompareOptions.

        Gets or sets a value indicating whether fields content is ignored. By default fields are not ignored.  # noqa: E501

        :param ignore_fields: The ignore_fields of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_fields = ignore_fields

    @property
    def ignore_footnotes(self):
        """Gets the ignore_footnotes of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether footnotes/endnotes content is ignored. By default footnotes/endnotes are not ignored.  # noqa: E501

        :return: The ignore_footnotes of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_footnotes

    @ignore_footnotes.setter
    def ignore_footnotes(self, ignore_footnotes):
        """Sets the ignore_footnotes of this CompareOptions.

        Gets or sets a value indicating whether footnotes/endnotes content is ignored. By default footnotes/endnotes are not ignored.  # noqa: E501

        :param ignore_footnotes: The ignore_footnotes of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_footnotes = ignore_footnotes

    @property
    def ignore_formatting(self):
        """Gets the ignore_formatting of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether formatting is ignored. By default document formatting is not ignored.  # noqa: E501

        :return: The ignore_formatting of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_formatting

    @ignore_formatting.setter
    def ignore_formatting(self, ignore_formatting):
        """Sets the ignore_formatting of this CompareOptions.

        Gets or sets a value indicating whether formatting is ignored. By default document formatting is not ignored.  # noqa: E501

        :param ignore_formatting: The ignore_formatting of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_formatting = ignore_formatting

    @property
    def ignore_headers_and_footers(self):
        """Gets the ignore_headers_and_footers of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether headers and footers content is ignored. By default headers and footers are not ignored.  # noqa: E501

        :return: The ignore_headers_and_footers of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_headers_and_footers

    @ignore_headers_and_footers.setter
    def ignore_headers_and_footers(self, ignore_headers_and_footers):
        """Sets the ignore_headers_and_footers of this CompareOptions.

        Gets or sets a value indicating whether headers and footers content is ignored. By default headers and footers are not ignored.  # noqa: E501

        :param ignore_headers_and_footers: The ignore_headers_and_footers of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_headers_and_footers = ignore_headers_and_footers

    @property
    def ignore_tables(self):
        """Gets the ignore_tables of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether tables content is ignored. By default tables are not ignored.  # noqa: E501

        :return: The ignore_tables of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_tables

    @ignore_tables.setter
    def ignore_tables(self, ignore_tables):
        """Sets the ignore_tables of this CompareOptions.

        Gets or sets a value indicating whether tables content is ignored. By default tables are not ignored.  # noqa: E501

        :param ignore_tables: The ignore_tables of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_tables = ignore_tables

    @property
    def ignore_textboxes(self):
        """Gets the ignore_textboxes of this CompareOptions.  # noqa: E501

        Gets or sets a value indicating whether textboxes content is ignored. By default textboxes are not ignored.  # noqa: E501

        :return: The ignore_textboxes of this CompareOptions.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_textboxes

    @ignore_textboxes.setter
    def ignore_textboxes(self, ignore_textboxes):
        """Sets the ignore_textboxes of this CompareOptions.

        Gets or sets a value indicating whether textboxes content is ignored. By default textboxes are not ignored.  # noqa: E501

        :param ignore_textboxes: The ignore_textboxes of this CompareOptions.  # noqa: E501
        :type: bool
        """
        self._ignore_textboxes = ignore_textboxes

    @property
    def target(self):
        """Gets the target of this CompareOptions.  # noqa: E501

        Gets or sets the option that controls which document shall be used as a target during comparison.  # noqa: E501

        :return: The target of this CompareOptions.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this CompareOptions.

        Gets or sets the option that controls which document shall be used as a target during comparison.  # noqa: E501

        :param target: The target of this CompareOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["Current", "New"]  # noqa: E501
        if not target.isdigit():
            if target not in allowed_values:
                raise ValueError(
                    "Invalid value for `target` ({0}), must be one of {1}"  # noqa: E501
                    .format(target, allowed_values))
            self._target = target
        else:
            self._target = allowed_values[int(target) if six.PY3 else long(target)]


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
        if not isinstance(other, CompareOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other