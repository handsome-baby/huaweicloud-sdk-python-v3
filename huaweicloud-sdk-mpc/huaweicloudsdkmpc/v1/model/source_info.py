# coding: utf-8

import pprint
import re

import six





class SourceInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'duration': 'int',
        'format': 'str',
        'size': 'int',
        'video_info': 'VideoInfo',
        'audio_info': 'list[AudioInfo]'
    }

    attribute_map = {
        'duration': 'duration',
        'format': 'format',
        'size': 'size',
        'video_info': 'video_info',
        'audio_info': 'audio_info'
    }

    def __init__(self, duration=None, format=None, size=None, video_info=None, audio_info=None):
        """SourceInfo - a model defined in huaweicloud sdk"""
        
        

        self._duration = None
        self._format = None
        self._size = None
        self._video_info = None
        self._audio_info = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if format is not None:
            self.format = format
        if size is not None:
            self.size = size
        if video_info is not None:
            self.video_info = video_info
        if audio_info is not None:
            self.audio_info = audio_info

    @property
    def duration(self):
        """Gets the duration of this SourceInfo.

        片源时长

        :return: The duration of this SourceInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SourceInfo.

        片源时长

        :param duration: The duration of this SourceInfo.
        :type: int
        """
        self._duration = duration

    @property
    def format(self):
        """Gets the format of this SourceInfo.

        片源格式

        :return: The format of this SourceInfo.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SourceInfo.

        片源格式

        :param format: The format of this SourceInfo.
        :type: str
        """
        self._format = format

    @property
    def size(self):
        """Gets the size of this SourceInfo.

        片源大小

        :return: The size of this SourceInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SourceInfo.

        片源大小

        :param size: The size of this SourceInfo.
        :type: int
        """
        self._size = size

    @property
    def video_info(self):
        """Gets the video_info of this SourceInfo.


        :return: The video_info of this SourceInfo.
        :rtype: VideoInfo
        """
        return self._video_info

    @video_info.setter
    def video_info(self, video_info):
        """Sets the video_info of this SourceInfo.


        :param video_info: The video_info of this SourceInfo.
        :type: VideoInfo
        """
        self._video_info = video_info

    @property
    def audio_info(self):
        """Gets the audio_info of this SourceInfo.

        音频信息

        :return: The audio_info of this SourceInfo.
        :rtype: list[AudioInfo]
        """
        return self._audio_info

    @audio_info.setter
    def audio_info(self, audio_info):
        """Sets the audio_info of this SourceInfo.

        音频信息

        :param audio_info: The audio_info of this SourceInfo.
        :type: list[AudioInfo]
        """
        self._audio_info = audio_info

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
        if not isinstance(other, SourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
