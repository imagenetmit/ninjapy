# Location
(*location*)

## Overview

Location

### Available Operations

* [get_node_custom_fields_2](#get_node_custom_fields_2) - Location custom fields
* [update_node_attribute_values_2](#update_node_attribute_values_2) - Update Field Values

## get_node_custom_fields_2

Returns list of location custom fields

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

    res = n_client.location.get_node_custom_fields_2(id=360277, location_id=912137)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `location_id`                                                       | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `with_inheritance`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Retrieve values using definition scope hierarchy                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, models.GetNodeCustomFields2ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_node_attribute_values_2

Update location custom field values

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

    n_client.location.update_node_attribute_values_2(id=82022, location_id=511611)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                             | *int*                                                                                                            | :heavy_check_mark:                                                                                               | N/A                                                                                                              |
| `location_id`                                                                                                    | *int*                                                                                                            | :heavy_check_mark:                                                                                               | N/A                                                                                                              |
| `request_body`                                                                                                   | Dict[str, [models.UpdateNodeAttributeValues2RequestBody](../../models/updatenodeattributevalues2requestbody.md)] | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |