# TotalsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_bytes** | **int** |  | 
**bandwidth_formatted** | **str** |  | 
**screenshots_count** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.totals_response import TotalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TotalsResponse from a JSON string
totals_response_instance = TotalsResponse.from_json(json)
# print the JSON string representation of the object
print(TotalsResponse.to_json())

# convert the object into a dict
totals_response_dict = totals_response_instance.to_dict()
# create an instance of TotalsResponse from a dict
totals_response_from_dict = TotalsResponse.from_dict(totals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


