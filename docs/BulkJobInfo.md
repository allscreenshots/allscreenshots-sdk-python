# BulkJobInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**id** | **str** |  | 
**result_url** | **str** |  | [optional] 
**status** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.bulk_job_info import BulkJobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BulkJobInfo from a JSON string
bulk_job_info_instance = BulkJobInfo.from_json(json)
# print the JSON string representation of the object
print(BulkJobInfo.to_json())

# convert the object into a dict
bulk_job_info_dict = bulk_job_info_instance.to_dict()
# create an instance of BulkJobInfo from a dict
bulk_job_info_from_dict = BulkJobInfo.from_dict(bulk_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


