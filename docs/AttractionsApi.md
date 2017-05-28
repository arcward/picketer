# picketer.AttractionsApi

All URIs are relative to *https://app.ticketmaster.com/discovery/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attraction_details**](AttractionsApi.md#attraction_details) | **GET** /attractions/{id} | Get attraction details by ID
[**search_attractions**](AttractionsApi.md#search_attractions) | **GET** /attractions | Search attractions


# **attraction_details**
> Attraction attraction_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get attraction details by ID

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
api_instance = picketer.AttractionsApi()
id = 'id_example' # str | Attraction ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get attraction details by ID
    api_response = api_instance.attraction_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttractionsApi->attraction_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attraction ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**Attraction**](Attraction.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_attractions**
> Container search_attractions(id=id, keyword=keyword, source=source, locale=locale, include_test=include_test, size=size, page=page, include_licensed_content=include_licensed_content, sort=sort, classification_name=classification_name, classification_id=classification_id)

Search attractions

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
api_instance = picketer.AttractionsApi()
id = 'id_example' # str |  (optional)
keyword = 'keyword_example' # str |  (optional)
source = 'source_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
include_test = 'include_test_example' # str |  (optional)
size = 'size_example' # str |  (optional)
page = 'page_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)
classification_name = 'classification_name_example' # str |  (optional)
classification_id = 'classification_id_example' # str |  (optional)

try: 
    # Search attractions
    api_response = api_instance.search_attractions(id=id, keyword=keyword, source=source, locale=locale, include_test=include_test, size=size, page=page, include_licensed_content=include_licensed_content, sort=sort, classification_name=classification_name, classification_id=classification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttractionsApi->search_attractions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **keyword** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **include_test** | **str**|  | [optional] 
 **size** | **str**|  | [optional] 
 **page** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **classification_name** | **str**|  | [optional] 
 **classification_id** | **str**|  | [optional] 

### Return type

[**Container**](Container.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

