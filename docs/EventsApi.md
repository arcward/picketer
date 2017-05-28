# picketer.EventsApi

All URIs are relative to *https://app.ticketmaster.com/discovery/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_details**](EventsApi.md#event_details) | **GET** /events/{id} | Get event details by ID
[**event_images**](EventsApi.md#event_images) | **GET** /events/{id}/images | Get event images
[**search_events**](EventsApi.md#search_events) | **GET** /events | Event search


# **event_details**
> Event event_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get event details by ID

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
api_instance = picketer.EventsApi()
id = 'id_example' # str | Event ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get event details by ID
    api_response = api_instance.event_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->event_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_images**
> EventImages event_images(id, locale=locale, include_licensed_content=include_licensed_content)

Get event images

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
api_instance = picketer.EventsApi()
id = 'id_example' # str | Event ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get event images
    api_response = api_instance.event_images(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->event_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**EventImages**](EventImages.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_events**
> Container search_events(id=id, keyword=keyword, attraction_id=attraction_id, venue_id=venue_id, postal_code=postal_code, latlong=latlong, radius=radius, unit=unit, source=source, locale=locale, market_id=market_id, start_date_time=start_date_time, end_date_time=end_date_time, include_tba=include_tba, include_tbd=include_tbd, include_test=include_test, size=size, page=page, sort=sort, onsale_start_date_time=onsale_start_date_time, onsale_end_date_time=onsale_end_date_time, city=city, country_code=country_code, state_code=state_code, classification_name=classification_name, classification_id=classification_id, dma_id=dma_id, onsale_on_start_date=onsale_on_start_date, onsale_on_after_start_date=onsale_on_after_start_date, segment_id=segment_id, segment_name=segment_name, promoter_id=promoter_id, client_visibility=client_visibility, nlp=nlp, include_licensed_content=include_licensed_content)

Event search

Event search

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
api_instance = picketer.EventsApi()
id = 'id_example' # str | Event ID (optional)
keyword = 'keyword_example' # str | Search by keyword (optional)
attraction_id = 'attraction_id_example' # str |  (optional)
venue_id = 'venue_id_example' # str |  (optional)
postal_code = 'postal_code_example' # str |  (optional)
latlong = 'latlong_example' # str |  (optional)
radius = 'radius_example' # str |  (optional)
unit = 'unit_example' # str |  (optional)
source = 'source_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
market_id = 'market_id_example' # str |  (optional)
start_date_time = 'start_date_time_example' # str |  (optional)
end_date_time = 'end_date_time_example' # str |  (optional)
include_tba = 'include_tba_example' # str |  (optional)
include_tbd = 'include_tbd_example' # str |  (optional)
include_test = 'include_test_example' # str |  (optional)
size = 'size_example' # str |  (optional)
page = 'page_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)
onsale_start_date_time = 'onsale_start_date_time_example' # str |  (optional)
onsale_end_date_time = 'onsale_end_date_time_example' # str |  (optional)
city = 'city_example' # str |  (optional)
country_code = 'country_code_example' # str |  (optional)
state_code = 'state_code_example' # str |  (optional)
classification_name = 'classification_name_example' # str |  (optional)
classification_id = 'classification_id_example' # str |  (optional)
dma_id = 'dma_id_example' # str |  (optional)
onsale_on_start_date = 'onsale_on_start_date_example' # str |  (optional)
onsale_on_after_start_date = 'onsale_on_after_start_date_example' # str |  (optional)
segment_id = 'segment_id_example' # str |  (optional)
segment_name = 'segment_name_example' # str |  (optional)
promoter_id = 'promoter_id_example' # str |  (optional)
client_visibility = 'client_visibility_example' # str |  (optional)
nlp = 'nlp_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Event search
    api_response = api_instance.search_events(id=id, keyword=keyword, attraction_id=attraction_id, venue_id=venue_id, postal_code=postal_code, latlong=latlong, radius=radius, unit=unit, source=source, locale=locale, market_id=market_id, start_date_time=start_date_time, end_date_time=end_date_time, include_tba=include_tba, include_tbd=include_tbd, include_test=include_test, size=size, page=page, sort=sort, onsale_start_date_time=onsale_start_date_time, onsale_end_date_time=onsale_end_date_time, city=city, country_code=country_code, state_code=state_code, classification_name=classification_name, classification_id=classification_id, dma_id=dma_id, onsale_on_start_date=onsale_on_start_date, onsale_on_after_start_date=onsale_on_after_start_date, segment_id=segment_id, segment_name=segment_name, promoter_id=promoter_id, client_visibility=client_visibility, nlp=nlp, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->search_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event ID | [optional] 
 **keyword** | **str**| Search by keyword | [optional] 
 **attraction_id** | **str**|  | [optional] 
 **venue_id** | **str**|  | [optional] 
 **postal_code** | **str**|  | [optional] 
 **latlong** | **str**|  | [optional] 
 **radius** | **str**|  | [optional] 
 **unit** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **market_id** | **str**|  | [optional] 
 **start_date_time** | **str**|  | [optional] 
 **end_date_time** | **str**|  | [optional] 
 **include_tba** | **str**|  | [optional] 
 **include_tbd** | **str**|  | [optional] 
 **include_test** | **str**|  | [optional] 
 **size** | **str**|  | [optional] 
 **page** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **onsale_start_date_time** | **str**|  | [optional] 
 **onsale_end_date_time** | **str**|  | [optional] 
 **city** | **str**|  | [optional] 
 **country_code** | **str**|  | [optional] 
 **state_code** | **str**|  | [optional] 
 **classification_name** | **str**|  | [optional] 
 **classification_id** | **str**|  | [optional] 
 **dma_id** | **str**|  | [optional] 
 **onsale_on_start_date** | **str**|  | [optional] 
 **onsale_on_after_start_date** | **str**|  | [optional] 
 **segment_id** | **str**|  | [optional] 
 **segment_name** | **str**|  | [optional] 
 **promoter_id** | **str**|  | [optional] 
 **client_visibility** | **str**|  | [optional] 
 **nlp** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**Container**](Container.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

