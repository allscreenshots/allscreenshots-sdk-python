# CrawlPageOutputResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**expires_at** | **datetime** |  | 
**result_url** | **str** |  | 
**size** | **int** |  | 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_page_output_response import CrawlPageOutputResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlPageOutputResponse from a JSON string
crawl_page_output_response_instance = CrawlPageOutputResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlPageOutputResponse.to_json())

# convert the object into a dict
crawl_page_output_response_dict = crawl_page_output_response_instance.to_dict()
# create an instance of CrawlPageOutputResponse from a dict
crawl_page_output_response_from_dict = CrawlPageOutputResponse.from_dict(crawl_page_output_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


