# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HttpAccessupdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, is_enabled=None, addresses=None, basic_auth=None):
        """
        HttpAccessupdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'addresses': 'list[HttpAddressGrantupdate]',
            'basic_auth': 'HttpBasicAuthGrantupdate'
        }

        self.attribute_map = {
            'is_enabled': 'is_enabled',
            'addresses': 'addresses',
            'basic_auth': 'basic_auth'
        }

        self._is_enabled = is_enabled
        self._addresses = addresses
        self._basic_auth = basic_auth

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this HttpAccessupdate.

        :return: The is_enabled of this HttpAccessupdate.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this HttpAccessupdate.

        :param is_enabled: The is_enabled of this HttpAccessupdate.
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")

        self._is_enabled = is_enabled

    @property
    def addresses(self):
        """
        Gets the addresses of this HttpAccessupdate.

        :return: The addresses of this HttpAccessupdate.
        :rtype: list[HttpAddressGrantupdate]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this HttpAccessupdate.

        :param addresses: The addresses of this HttpAccessupdate.
        :type: list[HttpAddressGrantupdate]
        """
        if addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")

        self._addresses = addresses

    @property
    def basic_auth(self):
        """
        Gets the basic_auth of this HttpAccessupdate.

        :return: The basic_auth of this HttpAccessupdate.
        :rtype: HttpBasicAuthGrantupdate
        """
        return self._basic_auth

    @basic_auth.setter
    def basic_auth(self, basic_auth):
        """
        Sets the basic_auth of this HttpAccessupdate.

        :param basic_auth: The basic_auth of this HttpAccessupdate.
        :type: HttpBasicAuthGrantupdate
        """
        if basic_auth is None:
            raise ValueError("Invalid value for `basic_auth`, must not be `None`")

        self._basic_auth = basic_auth

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
        if not isinstance(other, HttpAccessupdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
