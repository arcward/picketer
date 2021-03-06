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


class Venue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, type=None, distance=None, units=None, locale=None, description=None, address=None, city=None, additional_info=None, state=None, country=None, url=None, postal_code=None, location=None, timezone=None, currency=None, markets=None, images=None, dma=None, social=None, box_office_info=None, parking_detail=None, accessible_seating_detail=None, general_info=None, external_links=None, test=None, links=None):
        """
        Venue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'distance': 'float',
            'units': 'str',
            'locale': 'str',
            'description': 'str',
            'address': 'Address',
            'city': 'City',
            'additional_info': 'str',
            'state': 'State',
            'country': 'Country',
            'url': 'str',
            'postal_code': 'str',
            'location': 'Location',
            'timezone': 'str',
            'currency': 'str',
            'markets': 'list[Market]',
            'images': 'list[Image]',
            'dma': 'list[DMA]',
            'social': 'Social',
            'box_office_info': 'BoxOfficeInfo',
            'parking_detail': 'str',
            'accessible_seating_detail': 'str',
            'general_info': 'GeneralInfo',
            'external_links': 'list[Link]',
            'test': 'bool',
            'links': 'Links'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'distance': 'distance',
            'units': 'units',
            'locale': 'locale',
            'description': 'description',
            'address': 'address',
            'city': 'city',
            'additional_info': 'additionalInfo',
            'state': 'state',
            'country': 'country',
            'url': 'url',
            'postal_code': 'postalCode',
            'location': 'location',
            'timezone': 'timezone',
            'currency': 'currency',
            'markets': 'markets',
            'images': 'images',
            'dma': 'dma',
            'social': 'social',
            'box_office_info': 'boxOfficeInfo',
            'parking_detail': 'parkingDetail',
            'accessible_seating_detail': 'accessibleSeatingDetail',
            'general_info': 'generalInfo',
            'external_links': 'externalLinks',
            'test': 'test',
            'links': '_links'
        }

        self._id = id
        self._name = name
        self._type = type
        self._distance = distance
        self._units = units
        self._locale = locale
        self._description = description
        self._address = address
        self._city = city
        self._additional_info = additional_info
        self._state = state
        self._country = country
        self._url = url
        self._postal_code = postal_code
        self._location = location
        self._timezone = timezone
        self._currency = currency
        self._markets = markets
        self._images = images
        self._dma = dma
        self._social = social
        self._box_office_info = box_office_info
        self._parking_detail = parking_detail
        self._accessible_seating_detail = accessible_seating_detail
        self._general_info = general_info
        self._external_links = external_links
        self._test = test
        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Venue.

        :return: The id of this Venue.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Venue.

        :param id: The id of this Venue.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Venue.

        :return: The name of this Venue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Venue.

        :param name: The name of this Venue.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Venue.

        :return: The type of this Venue.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Venue.

        :param type: The type of this Venue.
        :type: str
        """

        self._type = type

    @property
    def distance(self):
        """
        Gets the distance of this Venue.

        :return: The distance of this Venue.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """
        Sets the distance of this Venue.

        :param distance: The distance of this Venue.
        :type: float
        """

        self._distance = distance

    @property
    def units(self):
        """
        Gets the units of this Venue.

        :return: The units of this Venue.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this Venue.

        :param units: The units of this Venue.
        :type: str
        """

        self._units = units

    @property
    def locale(self):
        """
        Gets the locale of this Venue.

        :return: The locale of this Venue.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this Venue.

        :param locale: The locale of this Venue.
        :type: str
        """

        self._locale = locale

    @property
    def description(self):
        """
        Gets the description of this Venue.

        :return: The description of this Venue.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Venue.

        :param description: The description of this Venue.
        :type: str
        """

        self._description = description

    @property
    def address(self):
        """
        Gets the address of this Venue.

        :return: The address of this Venue.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Venue.

        :param address: The address of this Venue.
        :type: Address
        """

        self._address = address

    @property
    def city(self):
        """
        Gets the city of this Venue.

        :return: The city of this Venue.
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Venue.

        :param city: The city of this Venue.
        :type: City
        """

        self._city = city

    @property
    def additional_info(self):
        """
        Gets the additional_info of this Venue.

        :return: The additional_info of this Venue.
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """
        Sets the additional_info of this Venue.

        :param additional_info: The additional_info of this Venue.
        :type: str
        """

        self._additional_info = additional_info

    @property
    def state(self):
        """
        Gets the state of this Venue.

        :return: The state of this Venue.
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Venue.

        :param state: The state of this Venue.
        :type: State
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this Venue.

        :return: The country of this Venue.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Venue.

        :param country: The country of this Venue.
        :type: Country
        """

        self._country = country

    @property
    def url(self):
        """
        Gets the url of this Venue.

        :return: The url of this Venue.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Venue.

        :param url: The url of this Venue.
        :type: str
        """

        self._url = url

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Venue.

        :return: The postal_code of this Venue.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Venue.

        :param postal_code: The postal_code of this Venue.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def location(self):
        """
        Gets the location of this Venue.

        :return: The location of this Venue.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Venue.

        :param location: The location of this Venue.
        :type: Location
        """

        self._location = location

    @property
    def timezone(self):
        """
        Gets the timezone of this Venue.

        :return: The timezone of this Venue.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this Venue.

        :param timezone: The timezone of this Venue.
        :type: str
        """

        self._timezone = timezone

    @property
    def currency(self):
        """
        Gets the currency of this Venue.

        :return: The currency of this Venue.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Venue.

        :param currency: The currency of this Venue.
        :type: str
        """

        self._currency = currency

    @property
    def markets(self):
        """
        Gets the markets of this Venue.

        :return: The markets of this Venue.
        :rtype: list[Market]
        """
        return self._markets

    @markets.setter
    def markets(self, markets):
        """
        Sets the markets of this Venue.

        :param markets: The markets of this Venue.
        :type: list[Market]
        """

        self._markets = markets

    @property
    def images(self):
        """
        Gets the images of this Venue.

        :return: The images of this Venue.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Venue.

        :param images: The images of this Venue.
        :type: list[Image]
        """

        self._images = images

    @property
    def dma(self):
        """
        Gets the dma of this Venue.

        :return: The dma of this Venue.
        :rtype: list[DMA]
        """
        return self._dma

    @dma.setter
    def dma(self, dma):
        """
        Sets the dma of this Venue.

        :param dma: The dma of this Venue.
        :type: list[DMA]
        """

        self._dma = dma

    @property
    def social(self):
        """
        Gets the social of this Venue.

        :return: The social of this Venue.
        :rtype: Social
        """
        return self._social

    @social.setter
    def social(self, social):
        """
        Sets the social of this Venue.

        :param social: The social of this Venue.
        :type: Social
        """

        self._social = social

    @property
    def box_office_info(self):
        """
        Gets the box_office_info of this Venue.

        :return: The box_office_info of this Venue.
        :rtype: BoxOfficeInfo
        """
        return self._box_office_info

    @box_office_info.setter
    def box_office_info(self, box_office_info):
        """
        Sets the box_office_info of this Venue.

        :param box_office_info: The box_office_info of this Venue.
        :type: BoxOfficeInfo
        """

        self._box_office_info = box_office_info

    @property
    def parking_detail(self):
        """
        Gets the parking_detail of this Venue.

        :return: The parking_detail of this Venue.
        :rtype: str
        """
        return self._parking_detail

    @parking_detail.setter
    def parking_detail(self, parking_detail):
        """
        Sets the parking_detail of this Venue.

        :param parking_detail: The parking_detail of this Venue.
        :type: str
        """

        self._parking_detail = parking_detail

    @property
    def accessible_seating_detail(self):
        """
        Gets the accessible_seating_detail of this Venue.

        :return: The accessible_seating_detail of this Venue.
        :rtype: str
        """
        return self._accessible_seating_detail

    @accessible_seating_detail.setter
    def accessible_seating_detail(self, accessible_seating_detail):
        """
        Sets the accessible_seating_detail of this Venue.

        :param accessible_seating_detail: The accessible_seating_detail of this Venue.
        :type: str
        """

        self._accessible_seating_detail = accessible_seating_detail

    @property
    def general_info(self):
        """
        Gets the general_info of this Venue.

        :return: The general_info of this Venue.
        :rtype: GeneralInfo
        """
        return self._general_info

    @general_info.setter
    def general_info(self, general_info):
        """
        Sets the general_info of this Venue.

        :param general_info: The general_info of this Venue.
        :type: GeneralInfo
        """

        self._general_info = general_info

    @property
    def external_links(self):
        """
        Gets the external_links of this Venue.

        :return: The external_links of this Venue.
        :rtype: list[Link]
        """
        return self._external_links

    @external_links.setter
    def external_links(self, external_links):
        """
        Sets the external_links of this Venue.

        :param external_links: The external_links of this Venue.
        :type: list[Link]
        """

        self._external_links = external_links

    @property
    def test(self):
        """
        Gets the test of this Venue.

        :return: The test of this Venue.
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """
        Sets the test of this Venue.

        :param test: The test of this Venue.
        :type: bool
        """

        self._test = test

    @property
    def links(self):
        """
        Gets the links of this Venue.

        :return: The links of this Venue.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Venue.

        :param links: The links of this Venue.
        :type: Links
        """

        self._links = links

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
        if not isinstance(other, Venue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
