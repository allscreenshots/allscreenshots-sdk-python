# CrawlProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charged** | **int** |  | 
**completed** | **int** |  | 
**discovered** | **int** |  | 
**failed** | **int** |  | 
**queued** | **int** |  | 
**skipped** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.crawl_progress_response import CrawlProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlProgressResponse from a JSON string
crawl_progress_response_instance = CrawlProgressResponse.from_json(json)
# print the JSON string representation of the object
print(CrawlProgressResponse.to_json())

# convert the object into a dict
crawl_progress_response_dict = crawl_progress_response_instance.to_dict()
# create an instance of CrawlProgressResponse from a dict
crawl_progress_response_from_dict = CrawlProgressResponse.from_dict(crawl_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


