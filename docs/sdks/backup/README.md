# Backup
(*backup*)

## Overview

Backup

### Available Operations

* [get_integrity_check_jobs](#get_integrity_check_jobs) - Integrity check jobs.
* [submit_integrity_check_job](#submit_integrity_check_job) - Create an integrity check job
* [get_backup_jobs](#get_backup_jobs) - Backup jobs

## get_integrity_check_jobs

Returns a list of integrity check jobs.

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

    res = n_client.backup.get_integrity_check_jobs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter.                                                      |
| `ddf`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Deleted device filter.                                              |
| `sf`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Backup job status filter.                                           |
| `ptf`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Backup job planType filter.                                         |
| `stf`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Backup job startTime filter.                                        |
| `include`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Which devices include (active\|deleted\|all) default value active.  |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name.                                                        |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page.                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetIntegrityCheckJobsResponseBody](../../models/getintegritycheckjobsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## submit_integrity_check_job

Creates an integrity check job

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

    res = n_client.backup.submit_integrity_check_job()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.SubmitIntegrityCheckJobRequestBody](../../models/submitintegritycheckjobrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.SubmitIntegrityCheckJobResponseBody](../../models/submitintegritycheckjobresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_backup_jobs

Returns list of backup jobs

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

    res = n_client.backup.get_backup_jobs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ddf`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Deleted device filter                                               |
| `sf`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Backup job status filter                                            |
| `ptf`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Backup job planType filter                                          |
| `stf`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Backup job startTime filter                                         |
| `include`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Which devices include (active\|deleted\|all) default value active   |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetBackupJobsResponseBody](../../models/getbackupjobsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |