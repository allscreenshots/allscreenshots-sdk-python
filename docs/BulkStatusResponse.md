# BulkStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**completed_jobs** | **int** |  | 
**created_at** | **datetime** |  | 
**failed_jobs** | **int** |  | 
**id** | **str** |  | 
**jobs** | [**List[BulkJobDetailInfo]**](BulkJobDetailInfo.md) |  | 
**progress** | **int** |  | 
**status** | **str** |  | 
**total_jobs** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.bulk_status_response import BulkStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkStatusResponse from a JSON string
bulk_status_response_instance = BulkStatusResponse.from_json(json)
# print the JSON string representation of the object
print(BulkStatusResponse.to_json())

# convert the object into a dict
bulk_status_response_dict = bulk_status_response_instance.to_dict()
# create an instance of BulkStatusResponse from a dict
bulk_status_response_from_dict = BulkStatusResponse.from_dict(bulk_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


