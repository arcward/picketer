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


class Place(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, area=None, address=None, city=None, state=None, country=None, location=None, postal_code=None, name=None):
        """
        Place - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'area': 'Area',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'location': 'Location',
            'postal_code': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'area': 'area',
            'address': 'address',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'location': 'location',
            'postal_code': 'postalCode',
            'name': 'name'
        }

        self._area = area
        self._address = address
        self._city = city
        self._state = state
        self._country = country
        self._location = location
        self._postal_code = postal_code
        self._name = name

    @property
    def area(self):
        """
        Gets the area of this Place.

        :return: The area of this Place.
        :rtype: Area
        """
        return self._area

    @area.setter
    def area(self, area):
        """
        Sets the area of this Place.

        :param area: The area of this Place.
        :type: Area
        """

        self._area = area

    @property
    def address(self):
        """
        Gets the address of this Place.

        :return: The address of this Place.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Place.

        :param address: The address of this Place.
        :type: Address
        """

        self._address = address

    @property
    def city(self):
        """
        Gets the city of this Place.

        :return: The city of this Place.
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Place.

        :param city: The city of this Place.
        :type: City
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this Place.

        :return: The state of this Place.
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Place.

        :param state: The state of this Place.
        :type: State
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this Place.

        :return: The country of this Place.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Place.

        :param country: The country of this Place.
        :type: Country
        """

        self._country = country

    @property
    def location(self):
        """
        Gets the location of this Place.

        :return: The location of this Place.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Place.

        :param location: The location of this Place.
        :type: Location
        """

        self._location = location

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Place.

        :return: The postal_code of this Place.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Place.

        :param postal_code: The postal_code of this Place.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def name(self):
        """
        Gets the name of this Place.

        :return: The name of this Place.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Place.

        :param name: The name of this Place.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Place):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
