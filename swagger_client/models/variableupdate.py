# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Variableupdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, is_enabled=None, is_json=None, name=None, value=None):
        """
        Variableupdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'is_json': 'bool',
            'name': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'is_enabled': 'is_enabled',
            'is_json': 'is_json',
            'name': 'name',
            'value': 'value'
        }

        self._is_enabled = is_enabled
        self._is_json = is_json
        self._name = name
        self._value = value

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this Variableupdate.

        :return: The is_enabled of this Variableupdate.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Variableupdate.

        :param is_enabled: The is_enabled of this Variableupdate.
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")

        self._is_enabled = is_enabled

    @property
    def is_json(self):
        """
        Gets the is_json of this Variableupdate.

        :return: The is_json of this Variableupdate.
        :rtype: bool
        """
        return self._is_json

    @is_json.setter
    def is_json(self, is_json):
        """
        Sets the is_json of this Variableupdate.

        :param is_json: The is_json of this Variableupdate.
        :type: bool
        """
        if is_json is None:
            raise ValueError("Invalid value for `is_json`, must not be `None`")

        self._is_json = is_json

    @property
    def name(self):
        """
        Gets the name of this Variableupdate.

        :return: The name of this Variableupdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Variableupdate.

        :param name: The name of this Variableupdate.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this Variableupdate.

        :return: The value of this Variableupdate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Variableupdate.

        :param value: The value of this Variableupdate.
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Variableupdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
