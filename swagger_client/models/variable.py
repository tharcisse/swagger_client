# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Variable(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, is_enabled=None, environment=None, name=None, is_json=None, created_at=None, updated_at=None, value=None, project=None, inherited=None):
        """
        Variable - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'environment': 'str',
            'name': 'str',
            'is_json': 'bool',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'value': 'str',
            'project': 'str',
            'inherited': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'is_enabled',
            'environment': 'environment',
            'name': 'name',
            'is_json': 'is_json',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'value': 'value',
            'project': 'project',
            'inherited': 'inherited'
        }

        self._is_enabled = is_enabled
        self._environment = environment
        self._name = name
        self._is_json = is_json
        self._created_at = created_at
        self._updated_at = updated_at
        self._value = value
        self._project = project
        self._inherited = inherited

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this Variable.

        :return: The is_enabled of this Variable.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Variable.

        :param is_enabled: The is_enabled of this Variable.
        :type: bool
        """
        if is_enabled is None:
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")

        self._is_enabled = is_enabled

    @property
    def environment(self):
        """
        Gets the environment of this Variable.

        :return: The environment of this Variable.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this Variable.

        :param environment: The environment of this Variable.
        :type: str
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")

        self._environment = environment

    @property
    def name(self):
        """
        Gets the name of this Variable.

        :return: The name of this Variable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Variable.

        :param name: The name of this Variable.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def is_json(self):
        """
        Gets the is_json of this Variable.

        :return: The is_json of this Variable.
        :rtype: bool
        """
        return self._is_json

    @is_json.setter
    def is_json(self, is_json):
        """
        Sets the is_json of this Variable.

        :param is_json: The is_json of this Variable.
        :type: bool
        """
        if is_json is None:
            raise ValueError("Invalid value for `is_json`, must not be `None`")

        self._is_json = is_json

    @property
    def created_at(self):
        """
        Gets the created_at of this Variable.

        :return: The created_at of this Variable.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Variable.

        :param created_at: The created_at of this Variable.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Variable.

        :return: The updated_at of this Variable.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Variable.

        :param updated_at: The updated_at of this Variable.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def value(self):
        """
        Gets the value of this Variable.

        :return: The value of this Variable.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Variable.

        :param value: The value of this Variable.
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    @property
    def project(self):
        """
        Gets the project of this Variable.

        :return: The project of this Variable.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this Variable.

        :param project: The project of this Variable.
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")

        self._project = project

    @property
    def inherited(self):
        """
        Gets the inherited of this Variable.

        :return: The inherited of this Variable.
        :rtype: bool
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """
        Sets the inherited of this Variable.

        :param inherited: The inherited of this Variable.
        :type: bool
        """
        if inherited is None:
            raise ValueError("Invalid value for `inherited`, must not be `None`")

        self._inherited = inherited

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
        if not isinstance(other, Variable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
