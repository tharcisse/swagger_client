# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Project(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, description=None, repository=None, title=None, created_at=None, updated_at=None, default_domain=None, entropy=None, owner=None, vpn=None, subscription=None):
        """
        Project - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'ProjectStatus',
            'description': 'str',
            'repository': 'GitRepositoryInformation',
            'title': 'str',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'default_domain': 'str',
            'entropy': 'str',
            'owner': 'str',
            'vpn': 'VpnConfiguration',
            'subscription': 'ProjectSubscription'
        }

        self.attribute_map = {
            'status': 'status',
            'description': 'description',
            'repository': 'repository',
            'title': 'title',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'default_domain': 'default_domain',
            'entropy': 'entropy',
            'owner': 'owner',
            'vpn': 'vpn',
            'subscription': 'subscription'
        }

        self._status = status
        self._description = description
        self._repository = repository
        self._title = title
        self._created_at = created_at
        self._updated_at = updated_at
        self._default_domain = default_domain
        self._entropy = entropy
        self._owner = owner
        self._vpn = vpn
        self._subscription = subscription

    @property
    def status(self):
        """
        Gets the status of this Project.

        :return: The status of this Project.
        :rtype: ProjectStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Project.

        :param status: The status of this Project.
        :type: ProjectStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def description(self):
        """
        Gets the description of this Project.

        :return: The description of this Project.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Project.

        :param description: The description of this Project.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def repository(self):
        """
        Gets the repository of this Project.

        :return: The repository of this Project.
        :rtype: GitRepositoryInformation
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """
        Sets the repository of this Project.

        :param repository: The repository of this Project.
        :type: GitRepositoryInformation
        """
        if repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")

        self._repository = repository

    @property
    def title(self):
        """
        Gets the title of this Project.

        :return: The title of this Project.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Project.

        :param title: The title of this Project.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def created_at(self):
        """
        Gets the created_at of this Project.

        :return: The created_at of this Project.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Project.

        :param created_at: The created_at of this Project.
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Project.

        :return: The updated_at of this Project.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Project.

        :param updated_at: The updated_at of this Project.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def default_domain(self):
        """
        Gets the default_domain of this Project.

        :return: The default_domain of this Project.
        :rtype: str
        """
        return self._default_domain

    @default_domain.setter
    def default_domain(self, default_domain):
        """
        Sets the default_domain of this Project.

        :param default_domain: The default_domain of this Project.
        :type: str
        """
        if default_domain is None:
            raise ValueError("Invalid value for `default_domain`, must not be `None`")

        self._default_domain = default_domain

    @property
    def entropy(self):
        """
        Gets the entropy of this Project.

        :return: The entropy of this Project.
        :rtype: str
        """
        return self._entropy

    @entropy.setter
    def entropy(self, entropy):
        """
        Sets the entropy of this Project.

        :param entropy: The entropy of this Project.
        :type: str
        """
        if entropy is None:
            raise ValueError("Invalid value for `entropy`, must not be `None`")

        self._entropy = entropy

    @property
    def owner(self):
        """
        Gets the owner of this Project.

        :return: The owner of this Project.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this Project.

        :param owner: The owner of this Project.
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    @property
    def vpn(self):
        """
        Gets the vpn of this Project.

        :return: The vpn of this Project.
        :rtype: VpnConfiguration
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn):
        """
        Sets the vpn of this Project.

        :param vpn: The vpn of this Project.
        :type: VpnConfiguration
        """
        if vpn is None:
            raise ValueError("Invalid value for `vpn`, must not be `None`")

        self._vpn = vpn

    @property
    def subscription(self):
        """
        Gets the subscription of this Project.

        :return: The subscription of this Project.
        :rtype: ProjectSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this Project.

        :param subscription: The subscription of this Project.
        :type: ProjectSubscription
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")

        self._subscription = subscription

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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other