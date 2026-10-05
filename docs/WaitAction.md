# WaitAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ms** | **int** |  | [optional] 
**network_idle** | **bool** |  | [optional] [default to False]
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | [optional] 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.wait_action import WaitAction

# TODO update the JSON string below
json = "{}"
# create an instance of WaitAction from a JSON string
wait_action_instance = WaitAction.from_json(json)
# print the JSON string representation of the object
print(WaitAction.to_json())

# convert the object into a dict
wait_action_dict = wait_action_instance.to_dict()
# create an instance of WaitAction from a dict
wait_action_from_dict = WaitAction.from_dict(wait_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


