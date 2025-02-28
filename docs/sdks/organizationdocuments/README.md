# OrganizationDocuments
(*organization_documents*)

## Overview

Organization Documents

### Available Operations

* [archive_client_document](#archive_client_document) - Archive an organization document
* [archive_multi_page_client_documents](#archive_multi_page_client_documents) - Archives organization documents
* [create_organization_document](#create_organization_document) - Create organization document
* [get_client_documents_with_attribute_values](#get_client_documents_with_attribute_values) - List all organization documents with field values
* [create_organization_documents](#create_organization_documents) - Create organization documents
* [update_organization_documents](#update_organization_documents) - Update organization documents
* [delete_client_document](#delete_client_document) - Delete an archived organization document
* [get_client_document_signed_urls](#get_client_document_signed_urls) - Get organization document signed urls
* [get_organization_documents](#get_organization_documents) - List organization documents with field values
* [restore_client_document](#restore_client_document) - Restore an organization document
* [restore_multi_page_client_documents](#restore_multi_page_client_documents) - Restore multiple multi page organization documents
* [update_organization_document](#update_organization_document) - Update organization document

## archive_client_document

Archives an organization document by id

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

    res = n_client.organization_documents.archive_client_document(client_document_id=752902)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_document_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## archive_multi_page_client_documents

Archives multiple organization documents by id

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

    res = n_client.organization_documents.archive_multi_page_client_documents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_organization_document

Creates an organization document and returns the document created

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

    res = n_client.organization_documents.create_organization_document(organization_id=258814, document_template_id=949525)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                      | *int*                                                                                                  | :heavy_check_mark:                                                                                     | Organization identifier                                                                                |
| `document_template_id`                                                                                 | *int*                                                                                                  | :heavy_check_mark:                                                                                     | Document template identifier                                                                           |
| `document_name`                                                                                        | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Document Name                                                                                          |
| `document_description`                                                                                 | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Document Description                                                                                   |
| `fields`                                                                                               | Dict[str, [models.CreateOrganizationDocumentFields](../../models/createorganizationdocumentfields.md)] | :heavy_minus_sign:                                                                                     | Fields                                                                                                 |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[models.CreateOrganizationDocumentResponseBody](../../models/createorganizationdocumentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_client_documents_with_attribute_values

List all organization documents with field values

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

    res = n_client.organization_documents.get_client_documents_with_attribute_values()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_by`                                                          | [Optional[models.GroupBy]](../../models/groupby.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `organization_ids`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `template_ids`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `template_name`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `document_name`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetClientDocumentsWithAttributeValuesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_organization_documents

Creates organization documents and returns the documents created

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

    res = n_client.organization_documents.create_organization_documents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [List[models.CreateOrganizationDocumentsRequestBody]](../../models/.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.CreateOrganizationDocumentsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_organization_documents

Updates organization documents and returns the documents updated

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

    res = n_client.organization_documents.update_organization_documents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [List[models.UpdateOrganizationDocumentsRequestBody]](../../models/.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.UpdateOrganizationDocumentsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_client_document

Deletes an archived organization document by id

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

    n_client.organization_documents.delete_client_document(client_document_id=134113)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_document_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_client_document_signed_urls

Get organization document signed urls

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

    res = n_client.organization_documents.get_client_document_signed_urls(client_document_id=614605)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_document_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_organization_documents

List organization documents with field values

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

    res = n_client.organization_documents.get_organization_documents(organization_id=34758)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | Organization identifier                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetOrganizationDocumentsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## restore_client_document

Restores an organization document by id

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

    res = n_client.organization_documents.restore_client_document(client_document_id=686619)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `client_document_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## restore_multi_page_client_documents

Restores multiple organization documents by id

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

    res = n_client.organization_documents.restore_multi_page_client_documents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_organization_document

Updates an organization document and returns the updated version

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

    res = n_client.organization_documents.update_organization_document(organization_id=556376, client_document_id=614049)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                      | *int*                                                                                                  | :heavy_check_mark:                                                                                     | Organization identifier                                                                                |
| `client_document_id`                                                                                   | *int*                                                                                                  | :heavy_check_mark:                                                                                     | Organization document identifier                                                                       |
| `document_name`                                                                                        | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Document Name                                                                                          |
| `document_description`                                                                                 | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Document Description                                                                                   |
| `fields`                                                                                               | Dict[str, [models.UpdateOrganizationDocumentFields](../../models/updateorganizationdocumentfields.md)] | :heavy_minus_sign:                                                                                     | Fields                                                                                                 |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[models.UpdateOrganizationDocumentResponseBody](../../models/updateorganizationdocumentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |