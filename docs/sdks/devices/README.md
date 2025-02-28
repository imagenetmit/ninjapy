# Devices
(*devices*)

## Overview

Devices

### Available Operations

* [get_device](#get_device) - Device details
* [get_device_active_jobs](#get_device_active_jobs) - Device currently running (active) jobs
* [get_device_activities](#get_device_activities) - Device activities
* [get_device_alerts](#get_device_alerts) - Device alerts (triggered conditions)
* [get_device_disk_drives](#get_device_disk_drives) - Device disk drives
* [get_device_installed_os_patches](#get_device_installed_os_patches) - OS Patch installation report for device
* [get_device_installed_software_patches](#get_device_installed_software_patches) - Software Patch history for device
* [get_device_last_logged_on_user](#get_device_last_logged_on_user) - Last logged-on user information
* [get_device_network_interfaces](#get_device_network_interfaces) - Device network interfaces
* [get_device_pending_failed_rejected_os_patches](#get_device_pending_failed_rejected_os_patches) - OS Patches
* [get_device_pending_failed_rejected_software_patches](#get_device_pending_failed_rejected_software_patches) - Pending, Failed and Rejected Software patches for device
* [get_device_processors](#get_device_processors) - Device processors
* [get_device_services](#get_device_services) - Windows services
* [get_device_software](#get_device_software) - Device software inventory
* [get_device_volumes](#get_device_volumes) - Device storage volumes
* [get_node_custom_fields](#get_node_custom_fields) - Device custom fields
* [update_node_attribute_values](#update_node_attribute_values) - Update Field Values
* [get_policy_overrides](#get_policy_overrides) - Get summary of device policy overrides

## get_device

Returns device details

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

    res = n_client.devices.get_device(id=700953)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDeviceResponseBody](../../models/getdeviceresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_active_jobs

Returns currently running jobs for device

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

    res = n_client.devices.get_device_active_jobs(id=445995)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `lang`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tz`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time Zone                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceActiveJobsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_activities

Returns activity log for device

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

    res = n_client.devices.get_device_activities(id=729712)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *int*                                                                | :heavy_check_mark:                                                   | Device identifier                                                    |
| `older_than`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Return activities recorded that are newer than specified activity ID |
| `newer_than`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Return activities recorded that are older than specified activity ID |
| `activity_type`                                                      | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Return activities of type                                            |
| `status`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Return activities with status(es)                                    |
| `series_uid`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Return activities related to alert (series)                          |
| `page_size`                                                          | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Limit number of activities to return                                 |
| `lang`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Language tag                                                         |
| `tz`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Time Zone                                                            |
| `retries`                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)     | :heavy_minus_sign:                                                   | Configuration to override the default retry behavior of the client.  |

### Response

**[models.GetDeviceActivitiesResponseBody](../../models/getdeviceactivitiesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_alerts

Returns list of active alerts (triggered conditions) for device

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

    res = n_client.devices.get_device_alerts(id=531355)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `lang`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tz`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Time Zone                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceAlertsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_disk_drives

Returns device disks' details

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

    res = n_client.devices.get_device_disk_drives(id=398874)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceDiskDrivesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_installed_os_patches

Returns patch installation history records (successful and failed) for device

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

    res = n_client.devices.get_device_installed_os_patches(id=685935)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter (FAILED, INSTALLED)                             |
| `installed_before`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed before specified date                     |
| `installed_after`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed after specified date                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceInstalledOSPatchesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_installed_software_patches

Returns 3rd party software patch installation history records for device (successful and failed)

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

    res = n_client.devices.get_device_installed_software_patches(id=533654)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Type filter                                                   |
| `impact`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Impact filter                                                 |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter                                                 |
| `product_identifier`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Product Identifier                                                  |
| `installed_before`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed before specified date                     |
| `installed_after`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Include patches installed after specified date                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceInstalledSoftwarePatchesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_last_logged_on_user

Returns username that was last to login to device

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

    res = n_client.devices.get_device_last_logged_on_user(id=324433)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDeviceLastLoggedOnUserResponseBody](../../models/getdevicelastloggedonuserresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_network_interfaces

Returns device network interfaces' details

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

    res = n_client.devices.get_device_network_interfaces(id=876659)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceNetworkInterfacesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_pending_failed_rejected_os_patches

Returns list of pending/rejected/approved OS patches for device

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

    res = n_client.devices.get_device_pending_failed_rejected_os_patches(id=114890)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Type filter                                                   |
| `severity`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Severity filter                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDevicePendingFailedRejectedOSPatchesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_pending_failed_rejected_software_patches

Returns list of 3rd party Software patches for a device (for which there were no installation attempts)

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

    res = n_client.devices.get_device_pending_failed_rejected_software_patches(id=852494)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `status`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Status filter                                                 |
| `product_identifier`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Product Identifier                                                  |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Type filter                                                   |
| `impact`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Patch Impact filter                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDevicePendingFailedRejectedSoftwarePatchesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_processors

Returns list of device Processor details

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

    res = n_client.devices.get_device_processors(id=867659)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceProcessorsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_services

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

    res = n_client.devices.get_device_services(id=808416)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Service name                                                        |
| `state`                                                             | [Optional[models.State]](../../models/state.md)                     | :heavy_minus_sign:                                                  | Service state                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceServicesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_software

Returns list of software installed on device

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

    res = n_client.devices.get_device_software(id=716699)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceSoftwareResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_volumes

Returns device volumes' details

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

    res = n_client.devices.get_device_volumes(id=94124)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `include`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Additional information to include (bl - BitLocker status)           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetDeviceVolumesResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_node_custom_fields

Returns list of device custom fields

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

    res = n_client.devices.get_node_custom_fields(id=528241)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `with_inheritance`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Retrieve values using definition scope hierarchy                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, models.GetNodeCustomFieldsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_node_attribute_values

Update device custom field values

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

    n_client.devices.update_node_attribute_values(id=131659)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                           | *int*                                                                                                          | :heavy_check_mark:                                                                                             | Device identifier                                                                                              |
| `request_body`                                                                                                 | Dict[str, [models.UpdateNodeAttributeValuesRequestBody](../../models/updatenodeattributevaluesrequestbody.md)] | :heavy_minus_sign:                                                                                             | N/A                                                                                                            |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_policy_overrides

Returns list of overridden policy sections

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

    res = n_client.devices.get_policy_overrides(id=407129)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetPolicyOverridesResponseBody](../../models/getpolicyoverridesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |