# picketer.VenuesApi

All URIs are relative to *https://app.ticketmaster.com/discovery/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_venues**](VenuesApi.md#search_venues) | **GET** /venues | Venue search
[**venue_details**](VenuesApi.md#venue_details) | **GET** /venues/{id} | Get venue details by ID


# **search_venues**
> Container search_venues(id=id, keyword=keyword, latlong=latlong, radius=radius, unit=unit, source=source, locale=locale, include_test=include_test, size=size, page=page, sort=sort, country_code=country_code, state_code=state_code, include_licensed_content=include_licensed_content)

Venue search

Venue search

### Example 
```python
from __future__ import print_statement
import time
import picketer
from picketer.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyQueryParam
picketer.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# picketer.configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = picketer.VenuesApi()
id = 'id_example' # str | Venue ID (optional)
keyword = 'keyword_example' # str | Search by keyword (optional)
latlong = 'latlong_example' # str |  (optional)
radius = 'radius_example' # str |  (optional)
unit = 'unit_example' # str |  (optional)
source = 'source_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
include_test = 'include_test_example' # str |  (optional)
size = 'size_example' # str |  (optional)
page = 'page_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)
country_code = 'country_code_example' # str |  (optional)
state_code = 'state_code_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Venue search
    api_response = api_instance.search_venues(id=id, keyword=keyword, latlong=latlong, radius=radius, unit=unit, source=source, locale=locale, include_test=include_test, size=size, page=page, sort=sort, country_code=country_code, state_code=state_code, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VenuesApi->search_venues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Venue ID | [optional] 
 **keyword** | **str**| Search by keyword | [optional] 
 **latlong** | **str**|  | [optional] 
 **radius** | **str**|  | [optional] 
 **unit** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **include_test** | **str**|  | [optional] 
 **size** | **str**|  | [optional] 
 **page** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **country_code** | **str**|  | [optional] 
 **state_code** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**Container**](Container.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **venue_details**
> Venue venue_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get venue details by ID

### Example 
```python
from __future__ import print_statement
import time
import picketer
from picketer.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyQueryParam
picketer.configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# picketer.configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = picketer.VenuesApi()
id = 'id_example' # str | Venue ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get venue details by ID
    api_response = api_instance.venue_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VenuesApi->venue_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Venue ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**Venue**](Venue.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

