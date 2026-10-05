# CrawlPagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_size** | **int** |  | 
**pages** | [**List[CrawlPageResponse]**](CrawlPageResponse.md) |  | 
**total** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_pages_response import CrawlPagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlPagesResponse from a JSON string
crawl_pages_response_instance = CrawlPagesResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlPagesResponse.to_json())

# convert the object into a dict
crawl_pages_response_dict = crawl_pages_response_instance.to_dict()
# create an instance of CrawlPagesResponse from a dict
crawl_pages_response_from_dict = CrawlPagesResponse.from_dict(crawl_pages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


