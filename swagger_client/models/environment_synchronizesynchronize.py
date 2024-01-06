# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EnvironmentSynchronizesynchronize(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, synchronize_data=None, synchronize_code=None):
        """
        EnvironmentSynchronizesynchronize - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'synchronize_data': 'bool',
            'synchronize_code': 'bool'
        }

        self.attribute_map = {
            'synchronize_data': 'synchronize_data',
            'synchronize_code': 'synchronize_code'
        }

        self._synchronize_data = synchronize_data
        self._synchronize_code = synchronize_code

    @property
    def synchronize_data(self):
        """
        Gets the synchronize_data of this EnvironmentSynchronizesynchronize.

        :return: The synchronize_data of this EnvironmentSynchronizesynchronize.
        :rtype: bool
        """
        return self._synchronize_data

    @synchronize_data.setter
    def synchronize_data(self, synchronize_data):
        """
        Sets the synchronize_data of this EnvironmentSynchronizesynchronize.

        :param synchronize_data: The synchronize_data of this EnvironmentSynchronizesynchronize.
        :type: bool
        """
        if synchronize_data is None:
            raise ValueError("Invalid value for `synchronize_data`, must not be `None`")

        self._synchronize_data = synchronize_data

    @property
    def synchronize_code(self):
        """
        Gets the synchronize_code of this EnvironmentSynchronizesynchronize.

        :return: The synchronize_code of this EnvironmentSynchronizesynchronize.
        :rtype: bool
        """
        return self._synchronize_code

    @synchronize_code.setter
    def synchronize_code(self, synchronize_code):
        """
        Sets the synchronize_code of this EnvironmentSynchronizesynchronize.

        :param synchronize_code: The synchronize_code of this EnvironmentSynchronizesynchronize.
        :type: bool
        """
        if synchronize_code is None:
            raise ValueError("Invalid value for `synchronize_code`, must not be `None`")

        self._synchronize_code = synchronize_code

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
        if not isinstance(other, EnvironmentSynchronizesynchronize):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
