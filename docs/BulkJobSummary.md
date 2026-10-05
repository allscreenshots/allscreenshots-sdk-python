# BulkJobSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **datetime** |  | [optional] 
**completed_jobs** | **int** |  | 
**created_at** | **datetime** |  | 
**failed_jobs** | **int** |  | 
**id** | **str** |  | 
**progress** | **int** |  | 
**status** | **str** |  | 
**total_jobs** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.bulk_job_summary import BulkJobSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BulkJobSummary from a JSON string
bulk_job_summary_instance = BulkJobSummary.from_json(json)
# print the JSON string representation of the object
print(BulkJobSummary.to_json())

# convert the object into a dict
bulk_job_summary_dict = bulk_job_summary_instance.to_dict()
# create an instance of BulkJobSummary from a dict
bulk_job_summary_from_dict = BulkJobSummary.from_dict(bulk_job_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


