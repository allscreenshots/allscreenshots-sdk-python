# CrawlPageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_url** | **str** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**content_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**depth** | **int** |  | 
**description** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**http_status** | **int** |  | [optional] 
**id** | **str** |  | 
**language** | **str** |  | [optional] 
**outputs** | [**List[OutputSpec]**](OutputSpec.md) |  | 
**parent_id** | **str** |  | [optional] 
**render_time_ms** | **int** |  | [optional] 
**status** | **str** |  | 
**title** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_page_response import CrawlPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlPageResponse from a JSON string
crawl_page_response_instance = CrawlPageResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlPageResponse.to_json())

# convert the object into a dict
crawl_page_response_dict = crawl_page_response_instance.to_dict()
# create an instance of CrawlPageResponse from a dict
crawl_page_response_from_dict = CrawlPageResponse.from_dict(crawl_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


