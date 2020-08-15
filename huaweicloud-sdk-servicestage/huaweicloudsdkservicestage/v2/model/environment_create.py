# coding: utf-8

import pprint
import re

import six





class EnvironmentCreate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'alias': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'charge_mode': 'ChargeMode',
        'vpc_id': 'str',
        'base_resources': 'list[Resource]',
        'optional_resources': 'list[Resource]'
    }

    attribute_map = {
        'name': 'name',
        'alias': 'alias',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'charge_mode': 'charge_mode',
        'vpc_id': 'vpc_id',
        'base_resources': 'base_resources',
        'optional_resources': 'optional_resources'
    }

    def __init__(self, name=None, alias=None, description=None, enterprise_project_id='0', charge_mode=None, vpc_id=None, base_resources=None, optional_resources=None):
        """EnvironmentCreate - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._alias = None
        self._description = None
        self._enterprise_project_id = None
        self._charge_mode = None
        self._vpc_id = None
        self._base_resources = None
        self._optional_resources = None
        self.discriminator = None

        self.name = name
        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        self.vpc_id = vpc_id
        self.base_resources = base_resources
        if optional_resources is not None:
            self.optional_resources = optional_resources

    @property
    def name(self):
        """Gets the name of this EnvironmentCreate.

        环境名称。

        :return: The name of this EnvironmentCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentCreate.

        环境名称。

        :param name: The name of this EnvironmentCreate.
        :type: str
        """
        self._name = name

    @property
    def alias(self):
        """Gets the alias of this EnvironmentCreate.

        环境别名。

        :return: The alias of this EnvironmentCreate.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this EnvironmentCreate.

        环境别名。

        :param alias: The alias of this EnvironmentCreate.
        :type: str
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this EnvironmentCreate.

        环境描述。

        :return: The description of this EnvironmentCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnvironmentCreate.

        环境描述。

        :param description: The description of this EnvironmentCreate.
        :type: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EnvironmentCreate.

        企业项目ID。

        :return: The enterprise_project_id of this EnvironmentCreate.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EnvironmentCreate.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this EnvironmentCreate.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charge_mode(self):
        """Gets the charge_mode of this EnvironmentCreate.


        :return: The charge_mode of this EnvironmentCreate.
        :rtype: ChargeMode
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this EnvironmentCreate.


        :param charge_mode: The charge_mode of this EnvironmentCreate.
        :type: ChargeMode
        """
        self._charge_mode = charge_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EnvironmentCreate.

        虚拟私有云ID。

        :return: The vpc_id of this EnvironmentCreate.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EnvironmentCreate.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this EnvironmentCreate.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def base_resources(self):
        """Gets the base_resources of this EnvironmentCreate.

        基础资源。

        :return: The base_resources of this EnvironmentCreate.
        :rtype: list[Resource]
        """
        return self._base_resources

    @base_resources.setter
    def base_resources(self, base_resources):
        """Sets the base_resources of this EnvironmentCreate.

        基础资源。

        :param base_resources: The base_resources of this EnvironmentCreate.
        :type: list[Resource]
        """
        self._base_resources = base_resources

    @property
    def optional_resources(self):
        """Gets the optional_resources of this EnvironmentCreate.

        可选资源。

        :return: The optional_resources of this EnvironmentCreate.
        :rtype: list[Resource]
        """
        return self._optional_resources

    @optional_resources.setter
    def optional_resources(self, optional_resources):
        """Sets the optional_resources of this EnvironmentCreate.

        可选资源。

        :param optional_resources: The optional_resources of this EnvironmentCreate.
        :type: list[Resource]
        """
        self._optional_resources = optional_resources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnvironmentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
