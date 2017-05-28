# picketer.ClassificationsApi

All URIs are relative to *https://app.ticketmaster.com/discovery/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classification_details**](ClassificationsApi.md#classification_details) | **GET** /classifications/{id} | Get classification details by ID
[**genre_details**](ClassificationsApi.md#genre_details) | **GET** /classifications/genres/{id} | Get genre details by ID
[**search_classifications**](ClassificationsApi.md#search_classifications) | **GET** /classifications | Search classifications
[**segment_details**](ClassificationsApi.md#segment_details) | **GET** /classifications/segments/{id} | Get segment details by ID
[**subgenre_details**](ClassificationsApi.md#subgenre_details) | **GET** /classifications/subgenres/{id} | Get subgenre details by ID


# **classification_details**
> Classification classification_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get classification details by ID

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
api_instance = picketer.ClassificationsApi()
id = 'id_example' # str | Classification ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get classification details by ID
    api_response = api_instance.classification_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationsApi->classification_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Classification ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**Classification**](Classification.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genre_details**
> GenreDetails genre_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get genre details by ID

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
api_instance = picketer.ClassificationsApi()
id = 'id_example' # str | Genre ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get genre details by ID
    api_response = api_instance.genre_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationsApi->genre_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Genre ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**GenreDetails**](GenreDetails.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_classifications**
> Container search_classifications(id=id, keyword=keyword, source=source, locale=locale, include_test=include_test, size=size, page=page, include_licensed_content=include_licensed_content, sort=sort)

Search classifications

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
api_instance = picketer.ClassificationsApi()
id = 'id_example' # str |  (optional)
keyword = 'keyword_example' # str |  (optional)
source = 'source_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
include_test = 'include_test_example' # str |  (optional)
size = 'size_example' # str |  (optional)
page = 'page_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)

try: 
    # Search classifications
    api_response = api_instance.search_classifications(id=id, keyword=keyword, source=source, locale=locale, include_test=include_test, size=size, page=page, include_licensed_content=include_licensed_content, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationsApi->search_classifications: %s\n" % e)
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

### Return type

[**Container**](Container.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_details**
> SegmentDetails segment_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get segment details by ID

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
api_instance = picketer.ClassificationsApi()
id = 'id_example' # str | Sub-genre ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get segment details by ID
    api_response = api_instance.segment_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationsApi->segment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Sub-genre ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**SegmentDetails**](SegmentDetails.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subgenre_details**
> SubGenreDetails subgenre_details(id, locale=locale, include_licensed_content=include_licensed_content)

Get subgenre details by ID

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
api_instance = picketer.ClassificationsApi()
id = 'id_example' # str | Sub-genre ID
locale = 'locale_example' # str |  (optional)
include_licensed_content = 'include_licensed_content_example' # str |  (optional)

try: 
    # Get subgenre details by ID
    api_response = api_instance.subgenre_details(id, locale=locale, include_licensed_content=include_licensed_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationsApi->subgenre_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Sub-genre ID | 
 **locale** | **str**|  | [optional] 
 **include_licensed_content** | **str**|  | [optional] 

### Return type

[**SubGenreDetails**](SubGenreDetails.md)

### Authorization

[APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

