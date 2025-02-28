# RelatedItems
(*related_items*)

## Overview

Related Items

### Available Operations

* [create_related_item](#create_related_item) - Create Attachment Relation
* [create_related_item_for_entity](#create_related_item_for_entity) - Create entity relation
* [create_related_item_for_entity_1](#create_related_item_for_entity_1) - Create entity relations
* [create_secure_related_item_for_entity](#create_secure_related_item_for_entity) - Create Secure Relation
* [delete_related_item](#delete_related_item) - Delete related item
* [delete_related_items](#delete_related_items) - Delete related items
* [get_all_related_items](#get_all_related_items) - List all related items
* [get_related_items_for_host_entity](#get_related_items_for_host_entity) - List host entity related items by scope
* [get_related_items_with_entity](#get_related_items_with_entity) - List related entity related items
* [get_related_items_with_entity_type](#get_related_items_with_entity_type) - List related entity type related items
* [get_related_items_with_host_entity_type](#get_related_items_with_host_entity_type) - List host entity type related items

## create_related_item

Relate an attachment to an entity

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

    res = n_client.related_items.create_related_item(entity_type=ninjapy.CreateRelatedItemPathParamEntityType.LOCATION, entity_id=296653)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                       | [models.CreateRelatedItemPathParamEntityType](../../models/createrelateditempathparamentitytype.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `entity_id`                                                                                         | *int*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `file`                                                                                              | [Optional[models.File]](../../models/file.md)                                                       | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.CreateRelatedItemResponseBody](../../models/createrelateditemresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_related_item_for_entity

Create a relation between two entities

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

    res = n_client.related_items.create_related_item_for_entity(entity_type=ninjapy.CreateRelatedItemForEntityPathParamEntityType.DOCUMENT, entity_id=93985)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                         | [models.CreateRelatedItemForEntityPathParamEntityType](../../models/createrelateditemforentitypathparamentitytype.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `entity_id`                                                                                                           | *int*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `request_body`                                                                                                        | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*                                                                | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.CreateRelatedItemForEntityResponseBody](../../models/createrelateditemforentityresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_related_item_for_entity_1

Create multiple relations between two entities

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

    res = n_client.related_items.create_related_item_for_entity_1(entity_type=ninjapy.CreateRelatedItemForEntity1PathParamEntityType.LOCATION, entity_id=420486)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                           | [models.CreateRelatedItemForEntity1PathParamEntityType](../../models/createrelateditemforentity1pathparamentitytype.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `entity_id`                                                                                                             | *int*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `request_body`                                                                                                          | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*                                                                  | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[List[models.CreateRelatedItemForEntity1ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_secure_related_item_for_entity

Create a relation to a secure value

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

    res = n_client.related_items.create_secure_related_item_for_entity(entity_type=ninjapy.CreateSecureRelatedItemForEntityPathParamEntityType.KB_DOCUMENT, entity_id=55964)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                                     | [models.CreateSecureRelatedItemForEntityPathParamEntityType](../../models/createsecurerelateditemforentitypathparamentitytype.md) | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `entity_id`                                                                                                                       | *int*                                                                                                                             | :heavy_check_mark:                                                                                                                | N/A                                                                                                                               |
| `request_body`                                                                                                                    | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*                                                                            | :heavy_minus_sign:                                                                                                                | N/A                                                                                                                               |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.CreateSecureRelatedItemForEntityResponseBody](../../models/createsecurerelateditemforentityresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_related_item

Deletes related item

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

    n_client.related_items.delete_related_item(related_item_id=571103)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `related_item_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_related_items

Deletes related items associated with an entity

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

    n_client.related_items.delete_related_items(entity_type=ninjapy.DeleteRelatedItemsPathParamEntityType.KB_DOCUMENT, entity_id=935534)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                         | [models.DeleteRelatedItemsPathParamEntityType](../../models/deleterelateditemspathparamentitytype.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `entity_id`                                                                                           | *int*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_all_related_items

List all related items

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

    res = n_client.related_items.get_all_related_items()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetAllRelatedItemsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_related_items_for_host_entity

List related items for a specific host entity filterable by scope

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

    res = n_client.related_items.get_related_items_for_host_entity(entity_type=ninjapy.GetRelatedItemsForHostEntityPathParamEntityType.LOCATION, entity_id=442502)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                             | [models.GetRelatedItemsForHostEntityPathParamEntityType](../../models/getrelateditemsforhostentitypathparamentitytype.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `entity_id`                                                                                                               | *int*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `scope`                                                                                                                   | [Optional[models.Scope]](../../models/scope.md)                                                                           | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[List[models.GetRelatedItemsForHostEntityResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_related_items_with_entity

List related items for a specific related entity

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

    res = n_client.related_items.get_related_items_with_entity(rel_entity_type=ninjapy.PathParamRelEntityType.CONTACT, rel_entity_id=610598)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `rel_entity_type`                                                       | [models.PathParamRelEntityType](../../models/pathparamrelentitytype.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `rel_entity_id`                                                         | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.GetRelatedItemsWithEntityResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_related_items_with_entity_type

List related entities for a related entity type

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

    res = n_client.related_items.get_related_items_with_entity_type(related_entity_type=ninjapy.RelatedEntityType.END_USER)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `related_entity_type`                                               | [models.RelatedEntityType](../../models/relatedentitytype.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetRelatedItemsWithEntityTypeResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_related_items_with_host_entity_type

List relations and references for a host entity type

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

    res = n_client.related_items.get_related_items_with_host_entity_type(entity_type=ninjapy.GetRelatedItemsWithHostEntityTypePathParamEntityType.NODE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                                       | [models.GetRelatedItemsWithHostEntityTypePathParamEntityType](../../models/getrelateditemswithhostentitytypepathparamentitytype.md) | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[List[models.GetRelatedItemsWithHostEntityTypeResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |