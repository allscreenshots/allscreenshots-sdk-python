# BulkUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**BulkUrlOptions**](BulkUrlOptions.md) |  | [optional] 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.bulk_url_request import BulkUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUrlRequest from a JSON string
bulk_url_request_instance = BulkUrlRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUrlRequest.to_json())

# convert the object into a dict
bulk_url_request_dict = bulk_url_request_instance.to_dict()
# create an instance of BulkUrlRequest from a dict
bulk_url_request_from_dict = BulkUrlRequest.from_dict(bulk_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


