# BulkJobDetailInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**file_size** | **int** |  | [optional] 
**format** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**id** | **str** |  | 
**render_time_ms** | **int** |  | [optional] 
**result_url** | **str** |  | [optional] 
**status** | **str** |  | 
**storage_url** | **str** |  | [optional] 
**url** | **str** |  | 
**width** | **int** |  | [optional] 

## Example

```python
from allscreenshots_sdk.models.bulk_job_detail_info import BulkJobDetailInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BulkJobDetailInfo from a JSON string
bulk_job_detail_info_instance = BulkJobDetailInfo.from_json(json)
# print the JSON string representation of the object
print(BulkJobDetailInfo.to_json())

# convert the object into a dict
bulk_job_detail_info_dict = bulk_job_detail_info_instance.to_dict()
# create an instance of BulkJobDetailInfo from a dict
bulk_job_detail_info_from_dict = BulkJobDetailInfo.from_dict(bulk_job_detail_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


