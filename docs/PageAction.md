# PageAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | **bool** |  | [optional] [default to False]
**selector** | **str** |  | 
**timeout** | **int** |  | [optional] 
**type** | **str** |  | 
**clear** | **bool** |  | [optional] [default to True]
**text** | **str** |  | 
**key** | **str** |  | 
**value** | **str** |  | 
**to_bottom** | **bool** |  | [optional] [default to False]
**y** | **int** |  | [optional] 
**ms** | **int** |  | [optional] 
**network_idle** | **bool** |  | [optional] [default to False]

## Example

```python
from allscreenshots_sdk.models.page_action import PageAction

# TODO update the JSON string below
json = "{}"
# create an instance of PageAction from a JSON string
page_action_instance = PageAction.from_json(json)
# print the JSON string representation of the object
print(PageAction.to_json())

# convert the object into a dict
page_action_dict = page_action_instance.to_dict()
# create an instance of PageAction from a dict
page_action_from_dict = PageAction.from_dict(page_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


