# Management
(*management*)

## Overview

Management

### Available Operations

* [get_custom_fields_policy_conditions](#get_custom_fields_policy_conditions) - Get custom fields policy conditions
* [create_custom_fields_policy_condition](#create_custom_fields_policy_condition) - Create custom fields policy condition
* [get_windows_event_policy_conditions](#get_windows_event_policy_conditions) - Get windows event conditions
* [create_windows_event_policy_condition](#create_windows_event_policy_condition) - Create windows event condition
* [delete_policy_condition](#delete_policy_condition) - Delete policy condition
* [get_custom_fields_policy_condition](#get_custom_fields_policy_condition) - Get custom fields policy condition
* [get_windows_event_policy_condition](#get_windows_event_policy_condition) - Get windows event condition
* [create_organization](#create_organization) - Create new organization
* [node_approval_operation](#node_approval_operation) - Approve/Reject devices
* [reset_alert](#reset_alert) - Reset alert/condition
* [reset_alert_set_activity_data](#reset_alert_set_activity_data) - Reset alert/condition and provide custom data for activity
* [update_device_maintenance](#update_device_maintenance) - Schedule maintenance
* [cancel_device_maintenance](#cancel_device_maintenance) - Cancel maintenance
* [control_windows_service](#control_windows_service) - Windows service control
* [update_device](#update_device) - Update device information
* [get_device_link](#get_device_link) - Device link
* [reset_policy_overrides](#reset_policy_overrides) - Reset device policy overrides
* [reboot_devices](#reboot_devices) - Reboot device
* [remove_device_owner](#remove_device_owner) - Remove device owner
* [request_scripting_options](#request_scripting_options) - Device scripting options
* [run_script_on_device](#run_script_on_device) - Run script or built-in action
* [set_device_owner](#set_device_owner) - Set device owner
* [set_windows_service_configuration](#set_windows_service_configuration) - Modify Windows Service configuration
* [submit_os_patch_apply](#submit_os_patch_apply) - Run OS patch apply
* [submit_os_patch_scan](#submit_os_patch_scan) - Run OS patch scan
* [submit_software_patch_apply](#submit_software_patch_apply) - Run Software patch apply
* [submit_software_patch_scan](#submit_software_patch_scan) - Run Software patch scan
* [create_location_for_organization](#create_location_for_organization) - Add new location to organization
* [get_installer](#get_installer) - Generate installer
* [get_installer_for_location](#get_installer_for_location) - Generate installer
* [update_organization](#update_organization) - Update organization
* [update_location](#update_location) - Update location
* [update_node_role_policy_assignment_for_organization](#update_node_role_policy_assignment_for_organization) - Change organization policy mappings
* [create_policy](#create_policy) - Creates new Policy

## get_custom_fields_policy_conditions

Get all custom fields policy conditions for specified policy

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

    res = n_client.management.get_custom_fields_policy_conditions(policy_id=373422)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_custom_fields_policy_condition

Creates custom fields policy condition for specified policy

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

    res = n_client.management.create_custom_fields_policy_condition(policy_id=76374)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `policy_id`                                                               | *int*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `enabled`                                                                 | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Policy condition enabled                                                  |
| `display_name`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | Policy condition display name                                             |
| `severity`                                                                | [Optional[models.Severity]](../../models/severity.md)                     | :heavy_minus_sign:                                                        | Policy condition severity                                                 |
| `priority`                                                                | [Optional[models.Priority]](../../models/priority.md)                     | :heavy_minus_sign:                                                        | Policy condition priority                                                 |
| `channels`                                                                | List[*int*]                                                               | :heavy_minus_sign:                                                        | Policy condition notification channels                                    |
| `scripts`                                                                 | List[[models.Scripts](../../models/scripts.md)]                           | :heavy_minus_sign:                                                        | Policy condition scripts                                                  |
| `notification_action`                                                     | [Optional[models.NotificationAction]](../../models/notificationaction.md) | :heavy_minus_sign:                                                        | Policy condition notification action                                      |
| `notify_on_reset`                                                         | *Optional[bool]*                                                          | :heavy_minus_sign:                                                        | Policy condition notify on reset                                          |
| `reset_threshold`                                                         | *Optional[int]*                                                           | :heavy_minus_sign:                                                        | Policy condition reset threshold (seconds)                                |
| `match_all`                                                               | List[[models.MatchAll](../../models/matchall.md)]                         | :heavy_minus_sign:                                                        | Custom field value must meet all conditions                               |
| `match_any`                                                               | List[[models.MatchAny](../../models/matchany.md)]                         | :heavy_minus_sign:                                                        | Custom field value must meet any conditions                               |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.CreateCustomFieldsPolicyConditionResponseBody](../../models/createcustomfieldspolicyconditionresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_windows_event_policy_conditions

Get all windows event conditions for specified policy

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

    res = n_client.management.get_windows_event_policy_conditions(policy_id=282848)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.GetWindowsEventPolicyConditionsResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_windows_event_policy_condition

Creates windows event condition for specified policy

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

    res = n_client.management.create_windows_event_policy_condition(policy_id=67109, source="<value>", event_ids=[
        67109,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `policy_id`                                                                                                                                 | *int*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `source`                                                                                                                                    | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | Event Source                                                                                                                                |
| `event_ids`                                                                                                                                 | List[*int*]                                                                                                                                 | :heavy_check_mark:                                                                                                                          | Event IDs                                                                                                                                   |
| `enabled`                                                                                                                                   | *Optional[bool]*                                                                                                                            | :heavy_minus_sign:                                                                                                                          | Policy condition enabled                                                                                                                    |
| `display_name`                                                                                                                              | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Policy condition display name                                                                                                               |
| `severity`                                                                                                                                  | [Optional[models.CreateWindowsEventPolicyConditionSeverity]](../../models/createwindowseventpolicyconditionseverity.md)                     | :heavy_minus_sign:                                                                                                                          | Policy condition severity                                                                                                                   |
| `priority`                                                                                                                                  | [Optional[models.CreateWindowsEventPolicyConditionPriority]](../../models/createwindowseventpolicyconditionpriority.md)                     | :heavy_minus_sign:                                                                                                                          | Policy condition priority                                                                                                                   |
| `channels`                                                                                                                                  | List[*int*]                                                                                                                                 | :heavy_minus_sign:                                                                                                                          | Policy condition notification channels                                                                                                      |
| `scripts`                                                                                                                                   | List[[models.CreateWindowsEventPolicyConditionScripts](../../models/createwindowseventpolicyconditionscripts.md)]                           | :heavy_minus_sign:                                                                                                                          | Policy condition scripts                                                                                                                    |
| `notification_action`                                                                                                                       | [Optional[models.CreateWindowsEventPolicyConditionNotificationAction]](../../models/createwindowseventpolicyconditionnotificationaction.md) | :heavy_minus_sign:                                                                                                                          | Policy condition notification action                                                                                                        |
| `notify_on_reset`                                                                                                                           | *Optional[bool]*                                                                                                                            | :heavy_minus_sign:                                                                                                                          | Policy condition notify on reset                                                                                                            |
| `reset_threshold`                                                                                                                           | *Optional[int]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Policy condition reset threshold (seconds)                                                                                                  |
| `text`                                                                                                                                      | [Optional[models.Text]](../../models/text.md)                                                                                               | :heavy_minus_sign:                                                                                                                          | Windows event policy condition text                                                                                                         |
| `occurrence`                                                                                                                                | [Optional[models.Occurrence]](../../models/occurrence.md)                                                                                   | :heavy_minus_sign:                                                                                                                          | Windows event policy condition occurrence                                                                                                   |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.CreateWindowsEventPolicyConditionResponseBody](../../models/createwindowseventpolicyconditionresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## delete_policy_condition

Deletes specified policy condition from specified agent policy

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

    n_client.management.delete_policy_condition(policy_id=679235, condition_id="04b357cc-e156-459c-a845-cd9071c70a1e")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `condition_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_custom_fields_policy_condition

Get specified custom fields condition for specified policy

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

    res = n_client.management.get_custom_fields_policy_condition(policy_id=29379, condition_id="5ea0d6b7-e023-4d08-8861-cf15246ed92f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `condition_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCustomFieldsPolicyConditionResponseBody](../../models/getcustomfieldspolicyconditionresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_windows_event_policy_condition

Get specified windows event condition for specified policy

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

    res = n_client.management.get_windows_event_policy_condition(policy_id=800373, condition_id="0de7c1eb-7755-40a5-aa42-f928a984fa15")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `policy_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `condition_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetWindowsEventPolicyConditionResponseBody](../../models/getwindowseventpolicyconditionresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_organization

Creates new organization with optional list of locations and policy mappings.
Template organization ID can be specified to copy various settings

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

    res = n_client.management.create_organization()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `template_organization_id`                                                                      | *Optional[int]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `request_body`                                                                                  | [Optional[models.CreateOrganizationRequestBody]](../../models/createorganizationrequestbody.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.CreateOrganizationResponseBody](../../models/createorganizationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## node_approval_operation

Approve or reject devices that are waiting for approval

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

    n_client.management.node_approval_operation(mode=ninjapy.Mode.APPROVE)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `mode`                                                              | [models.Mode](../../models/mode.md)                                 | :heavy_check_mark:                                                  | Approval action to perform                                          |
| `devices`                                                           | List[*int*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reset_alert

Resets alert/condition by UID

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

    n_client.management.reset_alert(uid="1ec6692a-aa0f-4b93-8f6a-d518540b5012")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `uid`                                                               | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reset_alert_set_activity_data

Resets alert/condition by UID

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

    n_client.management.reset_alert_set_activity_data(uid="7276ccad-eb23-4ac3-8c6e-80024f1e4ecb")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `uid`                                                                                                         | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `request_body`                                                                                                | [Optional[models.ResetAlertSetActivityDataRequestBody]](../../models/resetalertsetactivitydatarequestbody.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_device_maintenance

Schedule maintenance window for device

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

    n_client.management.update_device_maintenance(id=231198)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `disabled_features`                                                 | List[[models.DisabledFeatures](../../models/disabledfeatures.md)]   | :heavy_minus_sign:                                                  | List of features that will be disabled during maintenance           |
| `start`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Maintenance window start (optional, defaults to now)                |
| `end`                                                               | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Maintenance window end                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## cancel_device_maintenance

Cancel pending or active maintenance for device

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

    n_client.management.cancel_device_maintenance(id=520239)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## control_windows_service

Start/Stop/Restart Windows Service on a device

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

    n_client.management.control_windows_service(id=53056, service_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service identifier                                                  |
| `action`                                                            | [Optional[models.Action]](../../models/action.md)                   | :heavy_minus_sign:                                                  | Action                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_device

Change device friendly name, user data, etc.

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

    n_client.management.update_device(id=525669)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *int*                                                                                                 | :heavy_check_mark:                                                                                    | Device identifier                                                                                     |
| `display_name`                                                                                        | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Display name (User assigned)                                                                          |
| `user_data`                                                                                           | Dict[str, *Any*]                                                                                      | :heavy_minus_sign:                                                                                    | Custom attributes                                                                                     |
| `node_role_id`                                                                                        | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Node Role identifier                                                                                  |
| `policy_id`                                                                                           | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Assigned policy ID (overrides organization policy mapping, or reverts to organization policy if Null) |
| `organization_id`                                                                                     | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Organization identifier                                                                               |
| `location_id`                                                                                         | *Optional[int]*                                                                                       | :heavy_minus_sign:                                                                                    | Location identifier                                                                                   |
| `warranty`                                                                                            | [Optional[models.Warranty]](../../models/warranty.md)                                                 | :heavy_minus_sign:                                                                                    | Warranty Info                                                                                         |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_device_link

Returns link to device

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

    res = n_client.management.get_device_link(id=34272)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `redirect`                                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Return redirect response                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetDeviceLinkResponseBody](../../models/getdevicelinkresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reset_policy_overrides

Submit request to remove device policy overrides

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

    n_client.management.reset_policy_overrides(id=790327)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## reboot_devices

Sends a command to restart the computer

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

    n_client.management.reboot_devices(id=452601, mode=ninjapy.PathParamMode.NORMAL)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `mode`                                                              | [models.PathParamMode](../../models/pathparammode.md)               | :heavy_check_mark:                                                  | Reboot mode                                                         |
| `reason`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Stated reboot reason                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## remove_device_owner

Removes the owner of the device.

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

    n_client.management.remove_device_owner(id=586714)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## request_scripting_options

Returns scripting options (built-in actions, custom scripts) available for device

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

    res = n_client.management.request_scripting_options(id=963994)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `lang`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Language                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestScriptingOptionsResponseBody](../../models/requestscriptingoptionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## run_script_on_device

Run script or built-in action on a device

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

    n_client.management.run_script_on_device(id_param=392541)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id_param`                                                                      | *int*                                                                           | :heavy_check_mark:                                                              | Device identifier                                                               |
| `type`                                                                          | [Optional[models.RunScriptOnDeviceType]](../../models/runscriptondevicetype.md) | :heavy_minus_sign:                                                              | Type                                                                            |
| `id`                                                                            | *Optional[int]*                                                                 | :heavy_minus_sign:                                                              | Script identifier                                                               |
| `uid`                                                                           | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Built-in action identifier                                                      |
| `parameters`                                                                    | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Action/Script parameters                                                        |
| `run_as`                                                                        | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Credential role/identifier                                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## set_device_owner

Sets the owner of the device.

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

    n_client.management.set_device_owner(id=22171, owner_uid="09c191c5-319d-4f8d-8e8b-e9f1bd696443")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `owner_uid`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Device owner identifier                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## set_windows_service_configuration

Configures Windows Service startup settings

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

    n_client.management.set_windows_service_configuration(id=613762, service_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `service_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Service identifier                                                  |
| `start_type`                                                        | [Optional[models.StartType]](../../models/starttype.md)             | :heavy_minus_sign:                                                  | Start Type                                                          |
| `user_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Username                                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## submit_os_patch_apply

Submit a job to start a device OS patch apply

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

    n_client.management.submit_os_patch_apply(id=918967)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## submit_os_patch_scan

Submit a job to start a device OS patch scan

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

    n_client.management.submit_os_patch_scan(id=349148)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## submit_software_patch_apply

Submit a job to start a device software patch apply

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

    n_client.management.submit_software_patch_apply(id=989479)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## submit_software_patch_scan

Submit a job to start a device software patch scan

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

    n_client.management.submit_software_patch_scan(id=784427)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *int*                                                               | :heavy_check_mark:                                                  | Device identifier                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_location_for_organization

Creates new location for organization

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

    res = n_client.management.create_location_for_organization(id=641376)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                         | *int*                                                                                                        | :heavy_check_mark:                                                                                           | N/A                                                                                                          |
| `name`                                                                                                       | *Optional[str]*                                                                                              | :heavy_minus_sign:                                                                                           | Location name                                                                                                |
| `address`                                                                                                    | *Optional[str]*                                                                                              | :heavy_minus_sign:                                                                                           | Address                                                                                                      |
| `description`                                                                                                | *Optional[str]*                                                                                              | :heavy_minus_sign:                                                                                           | Description                                                                                                  |
| `user_data`                                                                                                  | Dict[str, *Any*]                                                                                             | :heavy_minus_sign:                                                                                           | Custom attributes                                                                                            |
| `tags`                                                                                                       | List[*str*]                                                                                                  | :heavy_minus_sign:                                                                                           | Tags                                                                                                         |
| `fields`                                                                                                     | Dict[str, [models.CreateLocationForOrganizationFields](../../models/createlocationfororganizationfields.md)] | :heavy_minus_sign:                                                                                           | Custom Fields                                                                                                |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[models.CreateLocationForOrganizationResponseBody](../../models/createlocationfororganizationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_installer

Generates and returns URL for installer with specified settings

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

    res = n_client.management.get_installer(request={
        "organization_id": 1,
        "location_id": 1,
        "installer_type": ninjapy.InstallerType.WINDOWS_MSI,
        "content": {},
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.GetInstallerRequestBody](../../models/getinstallerrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.GetInstallerResponseBody](../../models/getinstallerresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_installer_for_location

Generates and returns URL for installer for specified organization/location

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

    res = n_client.management.get_installer_for_location(id=645124, location_id=827642, installer_type=ninjapy.PathParamInstallerType.MAC_DMG)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `location_id`                                                           | *int*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `installer_type`                                                        | [models.PathParamInstallerType](../../models/pathparaminstallertype.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.GetInstallerForLocationResponseBody](../../models/getinstallerforlocationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_organization

Change organization name, description and policy mappings

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

    n_client.management.update_organization(id=138796)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                      | *int*                                                                                                     | :heavy_check_mark:                                                                                        | Organization identifier                                                                                   |
| `name`                                                                                                    | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Organization full name                                                                                    |
| `description`                                                                                             | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Organization Description                                                                                  |
| `user_data`                                                                                               | Dict[str, *Any*]                                                                                          | :heavy_minus_sign:                                                                                        | Custom attributes                                                                                         |
| `node_approval_mode`                                                                                      | [Optional[models.UpdateOrganizationNodeApprovalMode]](../../models/updateorganizationnodeapprovalmode.md) | :heavy_minus_sign:                                                                                        | Device Approval Mode                                                                                      |
| `tags`                                                                                                    | List[*str*]                                                                                               | :heavy_minus_sign:                                                                                        | Tags                                                                                                      |
| `fields`                                                                                                  | Dict[str, [models.UpdateOrganizationFields](../../models/updateorganizationfields.md)]                    | :heavy_minus_sign:                                                                                        | Custom Fields                                                                                             |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_location

Change location name, address, description, custom data

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

    res = n_client.management.update_location(id=907554, location_id=652608)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *int*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `location_id`                                                                  | *int*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `name`                                                                         | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Location name                                                                  |
| `address`                                                                      | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Address                                                                        |
| `description`                                                                  | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | Description                                                                    |
| `user_data`                                                                    | Dict[str, *Any*]                                                               | :heavy_minus_sign:                                                             | Custom attributes                                                              |
| `tags`                                                                         | List[*str*]                                                                    | :heavy_minus_sign:                                                             | Tags                                                                           |
| `fields`                                                                       | Dict[str, [models.UpdateLocationFields](../../models/updatelocationfields.md)] | :heavy_minus_sign:                                                             | Custom Fields                                                                  |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[models.UpdateLocationResponseBody](../../models/updatelocationresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_node_role_policy_assignment_for_organization

Update policy assignment for node role(s). Returns list of affected device IDs

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

    res = n_client.management.update_node_role_policy_assignment_for_organization(id=503142)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                              | *int*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `request_body`                                                                                                                                    | List[[models.UpdateNodeRolePolicyAssignmentForOrganizationRequestBody](../../models/updatenoderolepolicyassignmentfororganizationrequestbody.md)] | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create_policy

Creates new policy using (New Root, Child, Copy)

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

    res = n_client.management.create_policy()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `mode`                                                                              | [Optional[models.QueryParamMode]](../../models/queryparammode.md)                   | :heavy_minus_sign:                                                                  | Policy creation mode                                                                |
| `template_policy_id`                                                                | *Optional[int]*                                                                     | :heavy_minus_sign:                                                                  | Template Policy identifier                                                          |
| `request_body`                                                                      | [Optional[models.CreatePolicyRequestBody]](../../models/createpolicyrequestbody.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CreatePolicyResponseBody](../../models/createpolicyresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |