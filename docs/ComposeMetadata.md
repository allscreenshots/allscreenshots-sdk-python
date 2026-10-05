# ComposeMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canvas_height** | **int** |  | 
**canvas_width** | **int** |  | 
**captures** | [**List[CaptureInfo]**](CaptureInfo.md) |  | 
**layout_type** | **str** |  | 
**total_captures** | **int** |  | 

## Example

```python
from allscreenshots_sdk.models.compose_metadata import ComposeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeMetadata from a JSON string
compose_metadata_instance = ComposeMetadata.from_json(json)
# print the JSON string representation of the object
print(ComposeMetadata.to_json())

# convert the object into a dict
compose_metadata_dict = compose_metadata_instance.to_dict()
# create an instance of ComposeMetadata from a dict
compose_metadata_from_dict = ComposeMetadata.from_dict(compose_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


