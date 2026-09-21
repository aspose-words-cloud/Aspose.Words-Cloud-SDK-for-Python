# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="report_engine_settings.py">
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

class ReportEngineSettings(object):
    """Report engine settings.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'csv_data_load_options': 'CsvDataLoadOptions',
        'data_source_name': 'str',
        'data_source_type': 'str',
        'json_data_load_options': 'JsonDataLoadOptions',
        'report_build_options': 'list[str]',
        'xml_data_load_options': 'XmlDataLoadOptions'
    }

    attribute_map = {
        'csv_data_load_options': 'CsvDataLoadOptions',
        'data_source_name': 'DataSourceName',
        'data_source_type': 'DataSourceType',
        'json_data_load_options': 'JsonDataLoadOptions',
        'report_build_options': 'ReportBuildOptions',
        'xml_data_load_options': 'XmlDataLoadOptions'
    }

    def __init__(self, csv_data_load_options=None, data_source_name=None, data_source_type=None, json_data_load_options=None, report_build_options=None, xml_data_load_options=None):  # noqa: E501
        """ReportEngineSettings - a model defined in Swagger"""  # noqa: E501

        self._csv_data_load_options = None
        self._data_source_name = None
        self._data_source_type = None
        self._json_data_load_options = None
        self._report_build_options = None
        self._xml_data_load_options = None
        self.discriminator = None

        if csv_data_load_options is not None:
            self.csv_data_load_options = csv_data_load_options
        if data_source_name is not None:
            self.data_source_name = data_source_name
        if data_source_type is not None:
            self.data_source_type = data_source_type
        if json_data_load_options is not None:
            self.json_data_load_options = json_data_load_options
        if report_build_options is not None:
            self.report_build_options = report_build_options
        if xml_data_load_options is not None:
            self.xml_data_load_options = xml_data_load_options

    @property
    def csv_data_load_options(self):
        """Gets the csv_data_load_options of this ReportEngineSettings.  # noqa: E501

        Gets or sets the options for parsing CSV data.  # noqa: E501

        :return: The csv_data_load_options of this ReportEngineSettings.  # noqa: E501
        :rtype: CsvDataLoadOptions
        """
        return self._csv_data_load_options

    @csv_data_load_options.setter
    def csv_data_load_options(self, csv_data_load_options):
        """Sets the csv_data_load_options of this ReportEngineSettings.

        Gets or sets the options for parsing CSV data.  # noqa: E501

        :param csv_data_load_options: The csv_data_load_options of this ReportEngineSettings.  # noqa: E501
        :type: CsvDataLoadOptions
        """
        self._csv_data_load_options = csv_data_load_options

    @property
    def data_source_name(self):
        """Gets the data_source_name of this ReportEngineSettings.  # noqa: E501

        Gets or sets the name to reference the data source object in the template.  # noqa: E501

        :return: The data_source_name of this ReportEngineSettings.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this ReportEngineSettings.

        Gets or sets the name to reference the data source object in the template.  # noqa: E501

        :param data_source_name: The data_source_name of this ReportEngineSettings.  # noqa: E501
        :type: str
        """
        self._data_source_name = data_source_name

    @property
    def data_source_type(self):
        """Gets the data_source_type of this ReportEngineSettings.  # noqa: E501

        Gets or sets type of datasource.  # noqa: E501

        :return: The data_source_type of this ReportEngineSettings.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this ReportEngineSettings.

        Gets or sets type of datasource.  # noqa: E501

        :param data_source_type: The data_source_type of this ReportEngineSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["Xml", "Json", "Csv"]  # noqa: E501
        if not data_source_type.isdigit():
            if data_source_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `data_source_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(data_source_type, allowed_values))
            self._data_source_type = data_source_type
        else:
            self._data_source_type = allowed_values[int(data_source_type) if six.PY3 else long(data_source_type)]

    @property
    def json_data_load_options(self):
        """Gets the json_data_load_options of this ReportEngineSettings.  # noqa: E501

        Gets or sets the options for parsing JSON data.  # noqa: E501

        :return: The json_data_load_options of this ReportEngineSettings.  # noqa: E501
        :rtype: JsonDataLoadOptions
        """
        return self._json_data_load_options

    @json_data_load_options.setter
    def json_data_load_options(self, json_data_load_options):
        """Sets the json_data_load_options of this ReportEngineSettings.

        Gets or sets the options for parsing JSON data.  # noqa: E501

        :param json_data_load_options: The json_data_load_options of this ReportEngineSettings.  # noqa: E501
        :type: JsonDataLoadOptions
        """
        self._json_data_load_options = json_data_load_options

    @property
    def report_build_options(self):
        """Gets the report_build_options of this ReportEngineSettings.  # noqa: E501

        Gets or sets type of options to build report.  # noqa: E501

        :return: The report_build_options of this ReportEngineSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_build_options

    @report_build_options.setter
    def report_build_options(self, report_build_options):
        """Sets the report_build_options of this ReportEngineSettings.

        Gets or sets type of options to build report.  # noqa: E501

        :param report_build_options: The report_build_options of this ReportEngineSettings.  # noqa: E501
        :type: list[str]
        """
        self._report_build_options = report_build_options

    @property
    def xml_data_load_options(self):
        """Gets the xml_data_load_options of this ReportEngineSettings.  # noqa: E501

        Gets or sets the options for parsing XML data.  # noqa: E501

        :return: The xml_data_load_options of this ReportEngineSettings.  # noqa: E501
        :rtype: XmlDataLoadOptions
        """
        return self._xml_data_load_options

    @xml_data_load_options.setter
    def xml_data_load_options(self, xml_data_load_options):
        """Sets the xml_data_load_options of this ReportEngineSettings.

        Gets or sets the options for parsing XML data.  # noqa: E501

        :param xml_data_load_options: The xml_data_load_options of this ReportEngineSettings.  # noqa: E501
        :type: XmlDataLoadOptions
        """
        self._xml_data_load_options = xml_data_load_options


    def extract_files_content(self, filesContentResult):
        """Append the file content result list"""

    def validate(self):
        """Validate all required properties in model"""
        if self._data_source_type is None:
            raise ValueError("Property DataSourceType in ReportEngineSettings is required.")  # noqa: E501

        if self._csv_data_load_options is not None:
            self._csv_data_load_options.validate()





        if self._json_data_load_options is not None:
            self._json_data_load_options.validate()




        if self._xml_data_load_options is not None:
            self._xml_data_load_options.validate()


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
        if not isinstance(other, ReportEngineSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other