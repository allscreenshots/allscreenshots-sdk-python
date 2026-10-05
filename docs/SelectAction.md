# SelectAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from allscreenshots_sdk.models.select_action import SelectAction

# TODO update the JSON string below
json = "{}"
# create an instance of SelectAction from a JSON string
select_action_instance = SelectAction.from_json(json)
# print the JSON string representation of the object
print(SelectAction.to_json())

# convert the object into a dict
select_action_dict = select_action_instance.to_dict()
# create an instance of SelectAction from a dict
select_action_from_dict = SelectAction.from_dict(select_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


