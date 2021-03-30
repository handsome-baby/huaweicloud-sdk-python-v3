# coding: utf-8

import pprint
import re

import six





class ResourcesByTag:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_detail': 'str',
        'tags': 'list[ResourceTag]',
        'super_resource_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'super_resource_id': 'super_resource_id'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_detail=None, tags=None, super_resource_id=None):
        """ResourcesByTag - a model defined in huaweicloud sdk"""
        
        

        self._resource_id = None
        self._resource_name = None
        self._resource_detail = None
        self._tags = None
        self._super_resource_id = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_detail = resource_detail
        self.tags = tags
        if super_resource_id is not None:
            self.super_resource_id = super_resource_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ResourcesByTag.

        资源ID.

        :return: The resource_id of this ResourcesByTag.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ResourcesByTag.

        资源ID.

        :param resource_id: The resource_id of this ResourcesByTag.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ResourcesByTag.

        资源名称。

        :return: The resource_name of this ResourcesByTag.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ResourcesByTag.

        资源名称。

        :param resource_name: The resource_name of this ResourcesByTag.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_detail(self):
        """Gets the resource_detail of this ResourcesByTag.

        资源描述。

        :return: The resource_detail of this ResourcesByTag.
        :rtype: str
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        """Sets the resource_detail of this ResourcesByTag.

        资源描述。

        :param resource_detail: The resource_detail of this ResourcesByTag.
        :type: str
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        """Gets the tags of this ResourcesByTag.

        资源标签。

        :return: The tags of this ResourcesByTag.
        :rtype: list[ResourceTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourcesByTag.

        资源标签。

        :param tags: The tags of this ResourcesByTag.
        :type: list[ResourceTag]
        """
        self._tags = tags

    @property
    def super_resource_id(self):
        """Gets the super_resource_id of this ResourcesByTag.

        父级资源ID。

        :return: The super_resource_id of this ResourcesByTag.
        :rtype: str
        """
        return self._super_resource_id

    @super_resource_id.setter
    def super_resource_id(self, super_resource_id):
        """Sets the super_resource_id of this ResourcesByTag.

        父级资源ID。

        :param super_resource_id: The super_resource_id of this ResourcesByTag.
        :type: str
        """
        self._super_resource_id = super_resource_id

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
        if not isinstance(other, ResourcesByTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
