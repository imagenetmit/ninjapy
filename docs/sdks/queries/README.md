# Queries
(*queries*)

## Overview

Queries

### Available Operations

* [get_antivirus_status_report](#get_antivirus_status_report) - Antivirus status report
* [get_antivirus_threats](#get_antivirus_threats) - Antivirus threats report
* [get_computer_systems](#get_computer_systems) - Computer systems report
* [get_custom_fields_detailed_report](#get_custom_fields_detailed_report) - Custom fields detailed report
* [get_custom_fields_report](#get_custom_fields_report) - Custom fields report
* [get_device_health_report](#get_device_health_report) - Device health report
* [get_device_usage](#get_device_usage) - Device backup usage
* [get_disk_drives](#get_disk_drives) - Disk drives report
* [get_installed_os_patches](#get_installed_os_patches) - OS Patch installation report
* [get_installed_software_patches](#get_installed_software_patches) - Software Patch history report
* [get_last_logged_on_users_report](#get_last_logged_on_users_report) - Last logged-on user report
* [get_network_interfaces](#get_network_interfaces) - List Network Interfaces
* [get_operating_systems](#get_operating_systems) - Operating systems report
* [get_pending_failed_rejected_os_patches](#get_pending_failed_rejected_os_patches) - Pending, Failed and Rejected OS patches report
* [get_pending_failed_rejected_software_patches](#get_pending_failed_rejected_software_patches) - Pending, Failed and Rejected Software patches report
* [get_policy_overrides_1](#get_policy_overrides_1) - Get summary of device policy overrides
* [get_processors](#get_processors) - Processor report
* [get_raid_controller_report](#get_raid_controller_report) - RAID controller report
* [get_raid_drive_report](#get_raid_drive_report) - RAID drive report
* [get_scoped_custom_fields_detailed_report](#get_scoped_custom_fields_detailed_report) - Scoped custom fields detailed report
* [get_scoped_custom_fields_report](#get_scoped_custom_fields_report) - Scoped custom fields report
* [get_software](#get_software) - Software inventory
* [get_volumes](#get_volumes) - Disk volumes report
* [get_windows_services_report](#get_windows_services_report) - Windows services report

## get_antivirus_status_report

Returns list of statues of antivirus software installed on devices

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

    res = n_client.queries.get_antivirus_status_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `product_state`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Product State filter                                                |
| `product_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Product Name filter                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAntivirusStatusReportResponseBody](../../models/getantivirusstatusreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_antivirus_threats

Returns list of antivirus threats

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

    res = n_client.queries.get_antivirus_threats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAntivirusThreatsResponseBody](../../models/getantivirusthreatsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_computer_systems

Returns computer systems information for devices

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

    res = n_client.queries.get_computer_systems()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetComputerSystemsResponseBody](../../models/getcomputersystemsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_custom_fields_detailed_report

Returns Custom Fields report with additional information about each field

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

    res = n_client.queries.get_custom_fields_detailed_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `df`                                                                                  | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Device filter                                                                         |
| `cursor`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Cursor name                                                                           |
| `page_size`                                                                           | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Limit number of records per page                                                      |
| `updated_after`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Custom fields updated after specified date                                            |
| `fields`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Comma-separated list of fields                                                        |
| `show_secure_values`                                                                  | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Flag to indicate if secure values should be returned as plain text without encryption |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetCustomFieldsDetailedReportResponseBody](../../models/getcustomfieldsdetailedreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_custom_fields_report

Returns Custom Fields report

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

    res = n_client.queries.get_custom_fields_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `df`                                                                                  | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Device filter                                                                         |
| `cursor`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Cursor name                                                                           |
| `page_size`                                                                           | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Limit number of records per page                                                      |
| `updated_after`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Custom fields updated after specified date                                            |
| `fields`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Comma-separated list of fields                                                        |
| `show_secure_values`                                                                  | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Flag to indicate if secure values should be returned as plain text without encryption |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetCustomFieldsReportResponseBody](../../models/getcustomfieldsreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_health_report

Returns list of device health summary records

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

    res = n_client.queries.get_device_health_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `health`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Health status filter                                                |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDeviceHealthReportResponseBody](../../models/getdevicehealthreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_usage

Returns the backup usage by device

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

    res = n_client.queries.get_device_usage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `include_deleted_devices`                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether or not include deleted devices                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDeviceUsageResponseBody](../../models/getdeviceusageresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_disk_drives

Returns list of physical disks

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

    res = n_client.queries.get_disk_drives()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDiskDrivesResponseBody](../../models/getdiskdrivesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_installed_os_patches

Returns patch installation history records (successful and failed)

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

    res = n_client.queries.get_installed_os_patches()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter (FAILED, INSTALLED)                             |
| `installed_before`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed before specified date                     |
| `installed_after`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed after specified date                      |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInstalledOSPatchesResponseBody](../../models/getinstalledospatchesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_installed_software_patches

Returns 3rd party software patch installation history records (successful and failed)

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

    res = n_client.queries.get_installed_software_patches()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Type filter                                                   |
| `impact`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Impact filter                                                 |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter                                                 |
| `product_identifier`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Product Identifier                                                  |
| `installed_before`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed before specified date                     |
| `installed_after`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed after specified date                      |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInstalledSoftwarePatchesResponseBody](../../models/getinstalledsoftwarepatchesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_last_logged_on_users_report

Returns usernames and logon times 

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

    res = n_client.queries.get_last_logged_on_users_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetLastLoggedOnUsersReportResponseBody](../../models/getlastloggedonusersreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_network_interfaces

Returns list of Network Interfaces for each device

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

    res = n_client.queries.get_network_interfaces()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetNetworkInterfacesResponseBody](../../models/getnetworkinterfacesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_operating_systems

Returns operating systems' for devices

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

    res = n_client.queries.get_operating_systems()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetOperatingSystemsResponseBody](../../models/getoperatingsystemsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_pending_failed_rejected_os_patches

Returns list of OS patches for which there were no installation attempts

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

    res = n_client.queries.get_pending_failed_rejected_os_patches()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Type filter                                                   |
| `severity`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Severity filter                                               |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPendingFailedRejectedOSPatchesResponseBody](../../models/getpendingfailedrejectedospatchesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_pending_failed_rejected_software_patches

Returns list of 3rd party Software patches for which there were no installation attempts

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

    res = n_client.queries.get_pending_failed_rejected_software_patches()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter                                                 |
| `product_identifier`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Product Identifier                                                  |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Type filter                                                   |
| `impact`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Impact filter                                                 |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPendingFailedRejectedSoftwarePatchesResponseBody](../../models/getpendingfailedrejectedsoftwarepatchesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_policy_overrides_1

Returns list of overridden policy sections for each device

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

    res = n_client.queries.get_policy_overrides_1()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPolicyOverrides1ResponseBody](../../models/getpolicyoverrides1responsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_processors

Returns list of processors

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

    res = n_client.queries.get_processors()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetProcessorsResponseBody](../../models/getprocessorsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_raid_controller_report

Returns list of RAID controllers

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

    res = n_client.queries.get_raid_controller_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRAIDControllerReportResponseBody](../../models/getraidcontrollerreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_raid_drive_report

Returns list of drives connected to RAID controllers

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

    res = n_client.queries.get_raid_drive_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetRAIDDriveReportResponseBody](../../models/getraiddrivereportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_scoped_custom_fields_detailed_report

Returns report for Custom Fields defined at different scopes (device, location, organization) with additional information about each field

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

    res = n_client.queries.get_scoped_custom_fields_detailed_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cursor`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Cursor name                                                                           |
| `page_size`                                                                           | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Limit number of records per page                                                      |
| `updated_after`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Custom fields updated after specified date                                            |
| `fields`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Comma-separated list of fields                                                        |
| `scopes`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Comma-separated list of scopes                                                        |
| `show_secure_values`                                                                  | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Flag to indicate if secure values should be returned as plain text without encryption |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetScopedCustomFieldsDetailedReportResponseBody](../../models/getscopedcustomfieldsdetailedreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_scoped_custom_fields_report

Returns report for Custom Fields defined at different scopes (device, location, organization)

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

    res = n_client.queries.get_scoped_custom_fields_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `cursor`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Cursor name                                                                           |
| `page_size`                                                                           | *Optional[int]*                                                                       | :heavy_minus_sign:                                                                    | Limit number of records per page                                                      |
| `updated_after`                                                                       | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Custom fields updated after specified date                                            |
| `fields`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Comma-separated list of fields                                                        |
| `scopes`                                                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Comma-separated list of scopes                                                        |
| `show_secure_values`                                                                  | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Flag to indicate if secure values should be returned as plain text without encryption |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GetScopedCustomFieldsReportResponseBody](../../models/getscopedcustomfieldsreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_software

Returns list software installed on devices

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

    res = n_client.queries.get_software()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `installed_before`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include software installed before specified date                    |
| `installed_after`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include software installed after specified date                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetSoftwareResponseBody](../../models/getsoftwareresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_volumes

Returns list of disk volumes

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

    res = n_client.queries.get_volumes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `ts`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Monitoring timestamp filter                                         |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `include`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Additional information to include (bl - BitLocker status)           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetVolumesResponseBody](../../models/getvolumesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_windows_services_report

Returns list of Windows Services and their statuses

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

    res = n_client.queries.get_windows_services_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `df`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Device filter                                                       |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Service name                                                        |
| `state`                                                             | [Optional[models.QueryParamState]](../../models/queryparamstate.md) | :heavy_minus_sign:                                                  | Service state                                                       |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cursor name                                                         |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Limit number of records per page                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetWindowsServicesReportResponseBody](../../models/getwindowsservicesreportresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |