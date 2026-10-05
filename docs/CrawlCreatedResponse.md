# CrawlCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**status** | **str** |  | 
**status_url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_created_response import CrawlCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlCreatedResponse from a JSON string
crawl_created_response_instance = CrawlCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlCreatedResponse.to_json())

# convert the object into a dict
crawl_created_response_dict = crawl_created_response_instance.to_dict()
# create an instance of CrawlCreatedResponse from a dict
crawl_created_response_from_dict = CrawlCreatedResponse.from_dict(crawl_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


