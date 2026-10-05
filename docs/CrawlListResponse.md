# CrawlListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawls** | [**List[CrawlResponse]**](CrawlResponse.md) |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**total** | **int** |  | 
**total_pages** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_list_response import CrawlListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlListResponse from a JSON string
crawl_list_response_instance = CrawlListResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlListResponse.to_json())

# convert the object into a dict
crawl_list_response_dict = crawl_list_response_instance.to_dict()
# create an instance of CrawlListResponse from a dict
crawl_list_response_from_dict = CrawlListResponse.from_dict(crawl_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


