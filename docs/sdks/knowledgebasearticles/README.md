# KnowledgeBaseArticles
(*knowledge_base_articles*)

## Overview

Knowledge Base Articles

### Available Operations

* [upload_temp_attachments](#upload_temp_attachments) - Upload temporary attachments
* [archive_knowledge_base_articles](#archive_knowledge_base_articles) - Archive knowledge base articles
* [archive_knowledge_base_folders](#archive_knowledge_base_folders) - Archive knowledge base folders
* [create_knowledge_base_articles](#create_knowledge_base_articles) - Create knowledge base articles
* [update_knowledge_base_articles](#update_knowledge_base_articles) - Update knowledge base articles
* [delete_knowledge_base_articles](#delete_knowledge_base_articles) - Delete knowledge base articles
* [delete_knowledge_base_folders](#delete_knowledge_base_folders) - Delete knowledge base folders
* [download_knowledge_base_article](#download_knowledge_base_article) - Download knowledge base article
* [get_client_knowledge_base_articles](#get_client_knowledge_base_articles) - Lists organization knowledge base articles
* [get_global_knowledge_base_articles](#get_global_knowledge_base_articles) - Lists global knowledge base articles
* [get_knowledge_base_article_signed_urls](#get_knowledge_base_article_signed_urls) - Get knowledge base article signed urls
* [get_knowledge_base_folder_content](#get_knowledge_base_folder_content) - Returns knowledge base folder
* [get_knowledge_base_folder_path_content](#get_knowledge_base_folder_path_content) - Returns knowledge base folder
* [restore_knowledge_base_articles](#restore_knowledge_base_articles) - Restore archive knowledge base articles
* [restore_knowledge_base_folders](#restore_knowledge_base_folders) - Restore archived knowledge base folders
* [upload_knowledge_base_articles](#upload_knowledge_base_articles) - Upload knowledge base articles
* [download_related_item_attachment](#download_related_item_attachment) - Download related item attachment
* [get_related_item_attachments_signed_urls](#get_related_item_attachments_signed_urls) - Get related item attachments signed urls

## upload_temp_attachments

Upload temporary attachment

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

    res = n_client.knowledge_base_articles.upload_temp_attachments()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                         | [Optional[models.EntityType]](../../models/entitytype.md)                                             | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `request_body`                                                                                        | [Optional[models.UploadTempAttachmentsRequestBody]](../../models/uploadtempattachmentsrequestbody.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[List[models.UploadTempAttachmentsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## archive_knowledge_base_articles

Archive knowledge base articles

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

    n_client.knowledge_base_articles.archive_knowledge_base_articles()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## archive_knowledge_base_folders

Archive knowledge base folders

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

    n_client.knowledge_base_articles.archive_knowledge_base_folders()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_knowledge_base_articles

Create knowledge base articles

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

    res = n_client.knowledge_base_articles.create_knowledge_base_articles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.CreateKnowledgeBaseArticlesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_knowledge_base_articles

Update knowledge base articles

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

    res = n_client.knowledge_base_articles.update_knowledge_base_articles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.UpdateKnowledgeBaseArticlesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_knowledge_base_articles

Delete knowledge base articles

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

    n_client.knowledge_base_articles.delete_knowledge_base_articles()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_knowledge_base_folders

Delete knowledge base folders

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

    n_client.knowledge_base_articles.delete_knowledge_base_folders()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## download_knowledge_base_article

Download knowledge base article

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

    n_client.knowledge_base_articles.download_knowledge_base_article(article_id=710722)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `article_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_client_knowledge_base_articles

Lists organization knowledge base articles

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

    res = n_client.knowledge_base_articles.get_client_knowledge_base_articles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_ids`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `article_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_archived`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetClientKnowledgeBaseArticlesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_global_knowledge_base_articles

Lists global knowledge base articles

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

    res = n_client.knowledge_base_articles.get_global_knowledge_base_articles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `article_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_archived`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetGlobalKnowledgeBaseArticlesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_knowledge_base_article_signed_urls

Get knowledge base article signed urls

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

    res = n_client.knowledge_base_articles.get_knowledge_base_article_signed_urls(article_id=884251)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `article_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_knowledge_base_folder_content

Returns knowledge base folder and its content

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

    res = n_client.knowledge_base_articles.get_knowledge_base_folder_content(folder_id=279827)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `include_archived`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetKnowledgeBaseFolderContentResponseBody](../../models/getknowledgebasefoldercontentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_knowledge_base_folder_path_content

Returns knowledge base folder and its content

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

    res = n_client.knowledge_base_articles.get_knowledge_base_folder_path_content()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `folder_path`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `folder_id`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `organization_id`                                                   | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetKnowledgeBaseFolderPathContentResponseBody](../../models/getknowledgebasefolderpathcontentresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## restore_knowledge_base_articles

Restore archived knowledge base articles

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

    n_client.knowledge_base_articles.restore_knowledge_base_articles()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## restore_knowledge_base_folders

Restore archived knowledge base folders

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

    n_client.knowledge_base_articles.restore_knowledge_base_folders()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [Union[bytes, IO[bytes], io.BufferedReader]](../../models/.md)      | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## upload_knowledge_base_articles

Upload knowledge base articles

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

    res = n_client.knowledge_base_articles.upload_knowledge_base_articles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.UploadKnowledgeBaseArticlesRequestBody](../../models/uploadknowledgebasearticlesrequestbody.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[List[models.UploadKnowledgeBaseArticlesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## download_related_item_attachment

Download related item attachment

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

    n_client.knowledge_base_articles.download_related_item_attachment(related_item_id=973216)

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

## get_related_item_attachments_signed_urls

Get related item attachments signed urls for an entity

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

    res = n_client.knowledge_base_articles.get_related_item_attachments_signed_urls(entity_type=ninjapy.GetRelatedItemAttachmentsSignedUrlsPathParamEntityType.KB_DOCUMENT, entity_id=514349)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `entity_type`                                                                                                                           | [models.GetRelatedItemAttachmentsSignedUrlsPathParamEntityType](../../models/getrelateditemattachmentssignedurlspathparamentitytype.md) | :heavy_check_mark:                                                                                                                      | N/A                                                                                                                                     |
| `entity_id`                                                                                                                             | *int*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | N/A                                                                                                                                     |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |