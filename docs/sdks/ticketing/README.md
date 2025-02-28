# Ticketing
(*ticketing*)

## Overview

ticketing

### Available Operations

* [create](#create) - Create ticket
* [create_comment](#create_comment) - Add comment to ticket
* [get_ticket_by_id](#get_ticket_by_id) - Ticket
* [update](#update) - Update ticket
* [get_ticket_log_entries_by_ticket_id](#get_ticket_log_entries_by_ticket_id) - List ticket log entries
* [get_ticket_attributes](#get_ticket_attributes) - List ticket attributes
* [get_contacts](#get_contacts) - List contacts
* [get_ticket_form_by_id](#get_ticket_form_by_id) - Ticket form
* [get_ticket_forms](#get_ticket_forms) - List ticket forms
* [get_all_statuses](#get_all_statuses) - Get list of ticket status
* [get_boards](#get_boards) - List boards
* [get_tickets_by_board](#get_tickets_by_board) - List of tickets for board
* [get_all_user_and_contacts](#get_all_user_and_contacts) - List of users by user type

## create

Create a new ticket, does not accept files

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

    res = n_client.ticketing.create(client_id=1, ticket_form_id=1, subject="CPU with problems", location_id=1, node_id=1, description={
        "body": "new comment",
        "html_body": "<p>new comment</p>",
        "time_tracked": 60,
    }, type_=ninjapy.CreateType.PROBLEM, cc={
        "uids": [
            "1fa74a18-a329-40d8-b5b7-0a22624f7800",
            "b0558cb6-3c4e-438c-b8fd-5247c648bbbe",
        ],
        "emails": [
            "[\"example1@example.com\",\"example2@example.com\"]",
        ],
    }, parent_ticket_id=1, tags=[
        "[\"tag1\",\"tag2\"]",
    ], attributes=[
        {
            "attribute_id": 1,
            "value": "<value>",
            "id": 1,
        },
        {
            "attribute_id": 1,
            "value": "<value>",
            "id": 1,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               | Example                                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `client_id`                                                               | *int*                                                                     | :heavy_check_mark:                                                        | Client (Organization) identifier                                          | 1                                                                         |
| `ticket_form_id`                                                          | *int*                                                                     | :heavy_check_mark:                                                        | Ticket form identifier                                                    | 1                                                                         |
| `subject`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       | CPU with problems                                                         |
| `location_id`                                                             | *OptionalNullable[int]*                                                   | :heavy_minus_sign:                                                        | Location identifier                                                       | 1                                                                         |
| `node_id`                                                                 | *OptionalNullable[int]*                                                   | :heavy_minus_sign:                                                        | Device identifier                                                         | 1                                                                         |
| `description`                                                             | [Optional[models.CreateDescription]](../../models/createdescription.md)   | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `status`                                                                  | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `type`                                                                    | [OptionalNullable[models.CreateType]](../../models/createtype.md)         | :heavy_minus_sign:                                                        | Type of ticket                                                            | PROBLEM                                                                   |
| `cc`                                                                      | [OptionalNullable[models.Cc]](../../models/cc.md)                         | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `assigned_app_user_id`                                                    | *OptionalNullable[int]*                                                   | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `requester_uid`                                                           | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `severity`                                                                | [OptionalNullable[models.CreateSeverity]](../../models/createseverity.md) | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `priority`                                                                | [OptionalNullable[models.CreatePriority]](../../models/createpriority.md) | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `parent_ticket_id`                                                        | *OptionalNullable[int]*                                                   | :heavy_minus_sign:                                                        | Ticket parent identifier                                                  | 1                                                                         |
| `tags`                                                                    | List[*Nullable[str]*]                                                     | :heavy_minus_sign:                                                        | N/A                                                                       | [<br/>"tag1",<br/>"tag2"<br/>]                                            |
| `attributes`                                                              | List[[Nullable[models.Attributes]](../../models/attributes.md)]           | :heavy_minus_sign:                                                        | N/A                                                                       |                                                                           |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |                                                                           |

### Response

**[models.CreateResponseBody](../../models/createresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_comment

Add a new comment to a ticket, allows files

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

    n_client.ticketing.create_comment(ticket_id=874477, comment={
        "body": "new comment",
        "html_body": "<p>new comment</p>",
        "time_tracked": 60,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `ticket_id`                                                           | *int*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `comment`                                                             | [Optional[models.Comment]](../../models/comment.md)                   | :heavy_minus_sign:                                                    | N/A                                                                   |
| `files`                                                               | List[[models.CreateCommentFiles](../../models/createcommentfiles.md)] | :heavy_minus_sign:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ticket_by_id

Returns a ticket

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

    res = n_client.ticketing.get_ticket_by_id(ticket_id=996235)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTicketByIDResponseBody](../../models/getticketbyidresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update

Change ticket fields. Does not accept comments

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

    res = n_client.ticketing.update(ticket_id=519881, version=1, client_id=1, ticket_form_id=1, subject="CPU with problems", requester_uid="d95fa7f0-e743-42ce-b47c-b60cc78135dd", location_id=1, node_id=1, type_=ninjapy.UpdateType.PROBLEM, cc={
        "uids": [
            "1fa74a18-a329-40d8-b5b7-0a22624f7800",
            "b0558cb6-3c4e-438c-b8fd-5247c648bbbe",
        ],
        "emails": [
            "[\"example1@example.com\",\"example2@example.com\"]",
        ],
    }, parent_ticket_id=1, tags=[
        "[\"tag1\",\"tag2\"]",
    ], attributes=[
        {
            "attribute_id": 1,
            "value": "<value>",
            "id": 1,
        },
        {
            "attribute_id": 1,
            "value": "<value>",
            "id": 1,
        },
        {
            "attribute_id": 1,
            "value": "<value>",
            "id": 1,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `ticket_id`                                                                 | *int*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `version`                                                                   | *int*                                                                       | :heavy_check_mark:                                                          | ticket version                                                              | 1                                                                           |
| `client_id`                                                                 | *int*                                                                       | :heavy_check_mark:                                                          | Client (Organization) identifier                                            | 1                                                                           |
| `ticket_form_id`                                                            | *int*                                                                       | :heavy_check_mark:                                                          | Ticket form identifier                                                      | 1                                                                           |
| `subject`                                                                   | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         | CPU with problems                                                           |
| `requester_uid`                                                             | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |                                                                             |
| `location_id`                                                               | *OptionalNullable[int]*                                                     | :heavy_minus_sign:                                                          | Location identifier                                                         | 1                                                                           |
| `node_id`                                                                   | *OptionalNullable[int]*                                                     | :heavy_minus_sign:                                                          | Device identifier                                                           | 1                                                                           |
| `status`                                                                    | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `type`                                                                      | [OptionalNullable[models.UpdateType]](../../models/updatetype.md)           | :heavy_minus_sign:                                                          | Type of ticket                                                              | PROBLEM                                                                     |
| `cc`                                                                        | [OptionalNullable[models.UpdateCc]](../../models/updatecc.md)               | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `assigned_app_user_id`                                                      | *OptionalNullable[int]*                                                     | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `severity`                                                                  | [OptionalNullable[models.UpdateSeverity]](../../models/updateseverity.md)   | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `priority`                                                                  | [OptionalNullable[models.UpdatePriority]](../../models/updatepriority.md)   | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `parent_ticket_id`                                                          | *OptionalNullable[int]*                                                     | :heavy_minus_sign:                                                          | Ticket parent identifier                                                    | 1                                                                           |
| `tags`                                                                      | List[*Nullable[str]*]                                                       | :heavy_minus_sign:                                                          | N/A                                                                         | [<br/>"tag1",<br/>"tag2"<br/>]                                              |
| `attributes`                                                                | List[[Nullable[models.UpdateAttributes]](../../models/updateattributes.md)] | :heavy_minus_sign:                                                          | N/A                                                                         |                                                                             |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.UpdateResponseBody](../../models/updateresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ticket_log_entries_by_ticket_id

Returns list of the ticket log entries for a ticket

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

    res = n_client.ticketing.get_ticket_log_entries_by_ticket_id(ticket_id=806725)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `type`                                                              | [Optional[models.QueryParamType]](../../models/queryparamtype.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `create_time`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `anchor_id`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetTicketLogEntriesByTicketIDResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ticket_attributes

Returns list of the ticket attributes

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

    res = n_client.ticketing.get_ticket_attributes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetTicketAttributesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_contacts

Returns list of contacts

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

    res = n_client.ticketing.get_contacts()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetContactsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ticket_form_by_id

Returns a ticket form with fields 

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

    res = n_client.ticketing.get_ticket_form_by_id(id=61487)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTicketFormByIDResponseBody](../../models/getticketformbyidresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_ticket_forms

Returns list of ticket forms with their fields

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

    res = n_client.ticketing.get_ticket_forms()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetTicketFormsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_all_statuses

Get list of ticket status 

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

    res = n_client.ticketing.get_all_statuses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetAllStatusesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_boards

Returns list of ticketing boards

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

    res = n_client.ticketing.get_boards()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetBoardsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_tickets_by_board

Run a board. Returns list of tickets matching the board condition and filters. Allows pagination

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

    res = n_client.ticketing.get_tickets_by_board(board_id=771882)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `board_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sort_by`                                                           | List[[models.SortBy](../../models/sortby.md)]                       | :heavy_minus_sign:                                                  | N/A                                                                 |
| `filters`                                                           | List[[models.Filters](../../models/filters.md)]                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `search_criteria`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_columns`                                                   | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `last_cursor_id`                                                    | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTicketsByBoardResponseBody](../../models/getticketsbyboardresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_all_user_and_contacts

Returns list of users (contacts, end-user, technician)

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

    res = n_client.ticketing.get_all_user_and_contacts()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `page_size`                                                               | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Limit number of records per page                                          |
| `anchor_natural_id`                                                       | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Last User Identifier from previous page                                   |
| `search_criteria`                                                         | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Search by first name, last name or email address                          |
| `user_type`                                                               | [Optional[models.QueryParamUserType]](../../models/queryparamusertype.md) | :heavy_minus_sign:                                                        | User Type                                                                 |
| `client_id`                                                               | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Organization identifier                                                   |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[List[models.GetAllUserAndContactsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |