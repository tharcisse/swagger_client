# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Domainupdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ssl=None, wildcard=None):
        """
        Domainupdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ssl': 'DomainSSLupdate',
            'wildcard': 'bool'
        }

        self.attribute_map = {
            'ssl': 'ssl',
            'wildcard': 'wildcard'
        }

        self._ssl = ssl
        self._wildcard = wildcard

    @property
    def ssl(self):
        """
        Gets the ssl of this Domainupdate.

        :return: The ssl of this Domainupdate.
        :rtype: DomainSSLupdate
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """
        Sets the ssl of this Domainupdate.

        :param ssl: The ssl of this Domainupdate.
        :type: DomainSSLupdate
        """
        if ssl is None:
            raise ValueError("Invalid value for `ssl`, must not be `None`")

        self._ssl = ssl

    @property
    def wildcard(self):
        """
        Gets the wildcard of this Domainupdate.

        :return: The wildcard of this Domainupdate.
        :rtype: bool
        """
        return self._wildcard

    @wildcard.setter
    def wildcard(self, wildcard):
        """
        Sets the wildcard of this Domainupdate.

        :param wildcard: The wildcard of this Domainupdate.
        :type: bool
        """
        if wildcard is None:
            raise ValueError("Invalid value for `wildcard`, must not be `None`")

        self._wildcard = wildcard

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
        if not isinstance(other, Domainupdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other