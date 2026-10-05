# CrawlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**depth** | **int** |  | 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**id** | **str** |  | 
**limit** | **int** |  | 
**outputs** | [**List[OutputSpec]**](OutputSpec.md) |  | 
**progress** | [**CrawlProgressResponse**](CrawlProgressResponse.md) |  | 
**started_at** | **datetime** |  | [optional] 
**status** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_response import CrawlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlResponse from a JSON string
crawl_response_instance = CrawlResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlResponse.to_json())

# convert the object into a dict
crawl_response_dict = crawl_response_instance.to_dict()
# create an instance of CrawlResponse from a dict
crawl_response_from_dict = CrawlResponse.from_dict(crawl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


