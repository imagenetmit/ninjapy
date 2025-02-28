# CustomFields
(*custom_fields*)

## Overview

Custom Fields

### Available Operations

* [get_node_attribute_signed_urls](#get_node_attribute_signed_urls) - Get custom field signed urls

## get_node_attribute_signed_urls

Get custom field signed urls

### Example Usage

```python
import ninjapy
from ninjapy import Ninjapy
import os


with Ninjapy(
    server_url="https://api.example.com",
    security=ninjapy.Security(
        oauth2=os.getenv("NINJAPY_OAUTH2", ""),
    ),
) as n_client:

    res = n_client.custom_fields.get_node_attribute_signed_urls(entity_type=ninjapy.PathParamEntityType.NODE, entity_id=346939)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `entity_type`                                                       | [models.PathParamEntityType](../../models/pathparamentitytype.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `entity_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |