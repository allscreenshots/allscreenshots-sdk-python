# CrawlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_ads** | **bool** |  | [optional] [default to True]
**block_cookie_banners** | **bool** |  | [optional] [default to True]
**block_popups** | **bool** |  | [optional] [default to True]
**crawl_delay_ms** | **int** |  | [optional] [default to 500]
**dark_mode** | **bool** |  | [optional] [default to False]
**depth** | **int** |  | [optional] [default to 2]
**exclude_patterns** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] [default to 'png']
**full_page** | **bool** |  | [optional] [default to True]
**include_patterns** | **List[str]** |  | [optional] 
**include_subdomains** | **bool** |  | [optional] [default to False]
**limit** | **int** |  | [optional] [default to 25]
**outputs** | [**List[OutputSpec]**](OutputSpec.md) |  | [optional] 
**quality** | **int** |  | [optional] [default to 80]
**render_delay** | **int** |  | [optional] [default to 0]
**timeout** | **int** |  | [optional] [default to 30000]
**url** | **str** |  | 
**viewport** | [**ViewportConfig**](ViewportConfig.md) |  | [optional] 
**wait_until** | **str** |  | [optional] [default to 'domcontentloaded']

## Example

```python
from allscreenshots_sdk.models.crawl_request import CrawlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrawlRequest from a JSON string
crawl_request_instance = CrawlRequest.from_json(json)
# print the JSON string representation of the object
print(CrawlRequest.to_json())

# convert the object into a dict
crawl_request_dict = crawl_request_instance.to_dict()
# create an instance of CrawlRequest from a dict
crawl_request_from_dict = CrawlRequest.from_dict(crawl_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


