# coding: utf-8

"""
    Ticketmaster Discovery API

    Swagger spec based on Ticketmaster Discovery API

    OpenAPI spec version: 1.0.0
    Contact: git@edward.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EndTime(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, local_date=None, date_time=None, approximate=None, no_specific_time=None, local_time=None):
        """
        EndTime - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'local_date': 'str',
            'date_time': 'str',
            'approximate': 'bool',
            'no_specific_time': 'bool',
            'local_time': 'Time'
        }

        self.attribute_map = {
            'local_date': 'localDate',
            'date_time': 'dateTime',
            'approximate': 'approximate',
            'no_specific_time': 'noSpecificTime',
            'local_time': 'localTime'
        }

        self._local_date = local_date
        self._date_time = date_time
        self._approximate = approximate
        self._no_specific_time = no_specific_time
        self._local_time = local_time

    @property
    def local_date(self):
        """
        Gets the local_date of this EndTime.

        :return: The local_date of this EndTime.
        :rtype: str
        """
        return self._local_date

    @local_date.setter
    def local_date(self, local_date):
        """
        Sets the local_date of this EndTime.

        :param local_date: The local_date of this EndTime.
        :type: str
        """

        self._local_date = local_date

    @property
    def date_time(self):
        """
        Gets the date_time of this EndTime.

        :return: The date_time of this EndTime.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Sets the date_time of this EndTime.

        :param date_time: The date_time of this EndTime.
        :type: str
        """

        self._date_time = date_time

    @property
    def approximate(self):
        """
        Gets the approximate of this EndTime.

        :return: The approximate of this EndTime.
        :rtype: bool
        """
        return self._approximate

    @approximate.setter
    def approximate(self, approximate):
        """
        Sets the approximate of this EndTime.

        :param approximate: The approximate of this EndTime.
        :type: bool
        """

        self._approximate = approximate

    @property
    def no_specific_time(self):
        """
        Gets the no_specific_time of this EndTime.

        :return: The no_specific_time of this EndTime.
        :rtype: bool
        """
        return self._no_specific_time

    @no_specific_time.setter
    def no_specific_time(self, no_specific_time):
        """
        Sets the no_specific_time of this EndTime.

        :param no_specific_time: The no_specific_time of this EndTime.
        :type: bool
        """

        self._no_specific_time = no_specific_time

    @property
    def local_time(self):
        """
        Gets the local_time of this EndTime.

        :return: The local_time of this EndTime.
        :rtype: Time
        """
        return self._local_time

    @local_time.setter
    def local_time(self, local_time):
        """
        Sets the local_time of this EndTime.

        :param local_time: The local_time of this EndTime.
        :type: Time
        """

        self._local_time = local_time

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
        if not isinstance(other, EndTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
