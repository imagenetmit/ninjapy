# ninjapy

Developer-friendly & type-safe Python SDK specifically catered to leverage *ninjapy* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=ninjapy&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/imagenet/managedit). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

NinjaOne Public API 2.0: Ninja One Public API documentation. <br><br>
See also: <br> 
<a href="https://resources.ninjarmm.com/API/Ninja+RMM+Public+API+v2.0.5+Device+Filter+Syntax.pdf">Device Filter syntax</a><br>
<a href="https://resources.ninjarmm.com/API/Ninja+RMM+Public+API+v2.0.5+Webhooks.pdf">Webhooks</a>
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [ninjapy](#ninjapy)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from ninjapy python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "ninjapy",
# ]
# ///

from ninjapy import Ninjapy

sdk = Ninjapy(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import ninjapy
from ninjapy import Ninjapy
import os

async def main():

    async with Ninjapy(
        server_url="https://api.example.com",
        security=ninjapy.Security(
            oauth2=os.getenv("NINJAPY_OAUTH2", ""),
        ),
    ) as n_client:

        res = await n_client.management.get_custom_fields_policy_conditions_async(policy_id=373422)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type   | Scheme      | Environment Variable  |
| ------------- | ------ | ----------- | --------------------- |
| `oauth2`      | http   | HTTP Bearer | `NINJAPY_OAUTH2`      |
| `session_key` | apiKey | API key     | `NINJAPY_SESSION_KEY` |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [backup](docs/sdks/backup/README.md)

* [get_integrity_check_jobs](docs/sdks/backup/README.md#get_integrity_check_jobs) - Integrity check jobs.
* [submit_integrity_check_job](docs/sdks/backup/README.md#submit_integrity_check_job) - Create an integrity check job
* [get_backup_jobs](docs/sdks/backup/README.md#get_backup_jobs) - Backup jobs

### [checklist_templates](docs/sdks/checklisttemplates/README.md)

* [archive_checklist_template](docs/sdks/checklisttemplates/README.md#archive_checklist_template) - Archive a checklist template
* [get_checklist_templates](docs/sdks/checklisttemplates/README.md#get_checklist_templates) - List checklist templates
* [update_checklist_templates](docs/sdks/checklisttemplates/README.md#update_checklist_templates) - Update checklist templates
* [create_checklist_templates](docs/sdks/checklisttemplates/README.md#create_checklist_templates) - Create checklist templates
* [delete_checklist_template](docs/sdks/checklisttemplates/README.md#delete_checklist_template) - Delete a checklist template
* [delete_checklist_templates](docs/sdks/checklisttemplates/README.md#delete_checklist_templates) - Delete checklist templates
* [restore_checklist_template](docs/sdks/checklisttemplates/README.md#restore_checklist_template) - Restore a checklist template

### [custom_fields](docs/sdks/customfields/README.md)

* [get_node_attribute_signed_urls](docs/sdks/customfields/README.md#get_node_attribute_signed_urls) - Get custom field signed urls

### [devices](docs/sdks/devices/README.md)

* [get_device](docs/sdks/devices/README.md#get_device) - Device details
* [get_device_active_jobs](docs/sdks/devices/README.md#get_device_active_jobs) - Device currently running (active) jobs
* [get_device_activities](docs/sdks/devices/README.md#get_device_activities) - Device activities
* [get_device_alerts](docs/sdks/devices/README.md#get_device_alerts) - Device alerts (triggered conditions)
* [get_device_disk_drives](docs/sdks/devices/README.md#get_device_disk_drives) - Device disk drives
* [get_device_installed_os_patches](docs/sdks/devices/README.md#get_device_installed_os_patches) - OS Patch installation report for device
* [get_device_installed_software_patches](docs/sdks/devices/README.md#get_device_installed_software_patches) - Software Patch history for device
* [get_device_last_logged_on_user](docs/sdks/devices/README.md#get_device_last_logged_on_user) - Last logged-on user information
* [get_device_network_interfaces](docs/sdks/devices/README.md#get_device_network_interfaces) - Device network interfaces
* [get_device_pending_failed_rejected_os_patches](docs/sdks/devices/README.md#get_device_pending_failed_rejected_os_patches) - OS Patches
* [get_device_pending_failed_rejected_software_patches](docs/sdks/devices/README.md#get_device_pending_failed_rejected_software_patches) - Pending, Failed and Rejected Software patches for device
* [get_device_processors](docs/sdks/devices/README.md#get_device_processors) - Device processors
* [get_device_services](docs/sdks/devices/README.md#get_device_services) - Windows services
* [get_device_software](docs/sdks/devices/README.md#get_device_software) - Device software inventory
* [get_device_volumes](docs/sdks/devices/README.md#get_device_volumes) - Device storage volumes
* [get_node_custom_fields](docs/sdks/devices/README.md#get_node_custom_fields) - Device custom fields
* [update_node_attribute_values](docs/sdks/devices/README.md#update_node_attribute_values) - Update Field Values
* [get_policy_overrides](docs/sdks/devices/README.md#get_policy_overrides) - Get summary of device policy overrides

### [document_templates](docs/sdks/documenttemplates/README.md)

* [archive_document_template](docs/sdks/documenttemplates/README.md#archive_document_template) - Archive a document template
* [get_document_templates_with_attributes](docs/sdks/documenttemplates/README.md#get_document_templates_with_attributes) - List document templates with fields
* [create_document_template](docs/sdks/documenttemplates/README.md#create_document_template) - Create document template
* [get_document_template](docs/sdks/documenttemplates/README.md#get_document_template) - Get document template
* [update_document_template](docs/sdks/documenttemplates/README.md#update_document_template) - Update document template
* [delete_document_template](docs/sdks/documenttemplates/README.md#delete_document_template) - Delete a document template
* [restore_document_template](docs/sdks/documenttemplates/README.md#restore_document_template) - Restore a document template

### [groups](docs/sdks/groups/README.md)

* [get_group_device_ids](docs/sdks/groups/README.md#get_group_device_ids) - Group members

### [knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md)

* [upload_temp_attachments](docs/sdks/knowledgebasearticles/README.md#upload_temp_attachments) - Upload temporary attachments
* [archive_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#archive_knowledge_base_articles) - Archive knowledge base articles
* [archive_knowledge_base_folders](docs/sdks/knowledgebasearticles/README.md#archive_knowledge_base_folders) - Archive knowledge base folders
* [create_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#create_knowledge_base_articles) - Create knowledge base articles
* [update_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#update_knowledge_base_articles) - Update knowledge base articles
* [delete_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#delete_knowledge_base_articles) - Delete knowledge base articles
* [delete_knowledge_base_folders](docs/sdks/knowledgebasearticles/README.md#delete_knowledge_base_folders) - Delete knowledge base folders
* [download_knowledge_base_article](docs/sdks/knowledgebasearticles/README.md#download_knowledge_base_article) - Download knowledge base article
* [get_client_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#get_client_knowledge_base_articles) - Lists organization knowledge base articles
* [get_global_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#get_global_knowledge_base_articles) - Lists global knowledge base articles
* [get_knowledge_base_article_signed_urls](docs/sdks/knowledgebasearticles/README.md#get_knowledge_base_article_signed_urls) - Get knowledge base article signed urls
* [get_knowledge_base_folder_content](docs/sdks/knowledgebasearticles/README.md#get_knowledge_base_folder_content) - Returns knowledge base folder
* [get_knowledge_base_folder_path_content](docs/sdks/knowledgebasearticles/README.md#get_knowledge_base_folder_path_content) - Returns knowledge base folder
* [restore_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#restore_knowledge_base_articles) - Restore archive knowledge base articles
* [restore_knowledge_base_folders](docs/sdks/knowledgebasearticles/README.md#restore_knowledge_base_folders) - Restore archived knowledge base folders
* [upload_knowledge_base_articles](docs/sdks/knowledgebasearticles/README.md#upload_knowledge_base_articles) - Upload knowledge base articles
* [download_related_item_attachment](docs/sdks/knowledgebasearticles/README.md#download_related_item_attachment) - Download related item attachment
* [get_related_item_attachments_signed_urls](docs/sdks/knowledgebasearticles/README.md#get_related_item_attachments_signed_urls) - Get related item attachments signed urls

### [location](docs/sdks/location/README.md)

* [get_node_custom_fields_2](docs/sdks/location/README.md#get_node_custom_fields_2) - Location custom fields
* [update_node_attribute_values_2](docs/sdks/location/README.md#update_node_attribute_values_2) - Update Field Values

### [management](docs/sdks/management/README.md)

* [get_custom_fields_policy_conditions](docs/sdks/management/README.md#get_custom_fields_policy_conditions) - Get custom fields policy conditions
* [create_custom_fields_policy_condition](docs/sdks/management/README.md#create_custom_fields_policy_condition) - Create custom fields policy condition
* [get_windows_event_policy_conditions](docs/sdks/management/README.md#get_windows_event_policy_conditions) - Get windows event conditions
* [create_windows_event_policy_condition](docs/sdks/management/README.md#create_windows_event_policy_condition) - Create windows event condition
* [delete_policy_condition](docs/sdks/management/README.md#delete_policy_condition) - Delete policy condition
* [get_custom_fields_policy_condition](docs/sdks/management/README.md#get_custom_fields_policy_condition) - Get custom fields policy condition
* [get_windows_event_policy_condition](docs/sdks/management/README.md#get_windows_event_policy_condition) - Get windows event condition
* [create_organization](docs/sdks/management/README.md#create_organization) - Create new organization
* [node_approval_operation](docs/sdks/management/README.md#node_approval_operation) - Approve/Reject devices
* [reset_alert](docs/sdks/management/README.md#reset_alert) - Reset alert/condition
* [reset_alert_set_activity_data](docs/sdks/management/README.md#reset_alert_set_activity_data) - Reset alert/condition and provide custom data for activity
* [update_device_maintenance](docs/sdks/management/README.md#update_device_maintenance) - Schedule maintenance
* [cancel_device_maintenance](docs/sdks/management/README.md#cancel_device_maintenance) - Cancel maintenance
* [control_windows_service](docs/sdks/management/README.md#control_windows_service) - Windows service control
* [update_device](docs/sdks/management/README.md#update_device) - Update device information
* [get_device_link](docs/sdks/management/README.md#get_device_link) - Device link
* [reset_policy_overrides](docs/sdks/management/README.md#reset_policy_overrides) - Reset device policy overrides
* [reboot_devices](docs/sdks/management/README.md#reboot_devices) - Reboot device
* [remove_device_owner](docs/sdks/management/README.md#remove_device_owner) - Remove device owner
* [request_scripting_options](docs/sdks/management/README.md#request_scripting_options) - Device scripting options
* [run_script_on_device](docs/sdks/management/README.md#run_script_on_device) - Run script or built-in action
* [set_device_owner](docs/sdks/management/README.md#set_device_owner) - Set device owner
* [set_windows_service_configuration](docs/sdks/management/README.md#set_windows_service_configuration) - Modify Windows Service configuration
* [submit_os_patch_apply](docs/sdks/management/README.md#submit_os_patch_apply) - Run OS patch apply
* [submit_os_patch_scan](docs/sdks/management/README.md#submit_os_patch_scan) - Run OS patch scan
* [submit_software_patch_apply](docs/sdks/management/README.md#submit_software_patch_apply) - Run Software patch apply
* [submit_software_patch_scan](docs/sdks/management/README.md#submit_software_patch_scan) - Run Software patch scan
* [create_location_for_organization](docs/sdks/management/README.md#create_location_for_organization) - Add new location to organization
* [get_installer](docs/sdks/management/README.md#get_installer) - Generate installer
* [get_installer_for_location](docs/sdks/management/README.md#get_installer_for_location) - Generate installer
* [update_organization](docs/sdks/management/README.md#update_organization) - Update organization
* [update_location](docs/sdks/management/README.md#update_location) - Update location
* [update_node_role_policy_assignment_for_organization](docs/sdks/management/README.md#update_node_role_policy_assignment_for_organization) - Change organization policy mappings
* [create_policy](docs/sdks/management/README.md#create_policy) - Creates new Policy


### [organization](docs/sdks/organization/README.md)

* [get_organization_locations](docs/sdks/organization/README.md#get_organization_locations) - Organization locations
* [get_end_users](docs/sdks/organization/README.md#get_end_users) - List users
* [get_location_usage](docs/sdks/organization/README.md#get_location_usage) - Organization location backup usage
* [get_node_custom_fields_1](docs/sdks/organization/README.md#get_node_custom_fields_1) - Organization custom fields
* [update_node_attribute_values_1](docs/sdks/organization/README.md#update_node_attribute_values_1) - Update Field Values
* [get_organization](docs/sdks/organization/README.md#get_organization) - Organization information
* [get_organization_devices](docs/sdks/organization/README.md#get_organization_devices) - Organization devices
* [get_organization_location_usage](docs/sdks/organization/README.md#get_organization_location_usage) - Organization locations backup usage

### [organization_checklists](docs/sdks/organizationchecklists/README.md)

* [archive_organization_checklists](docs/sdks/organizationchecklists/README.md#archive_organization_checklists) - Archive organization checklists
* [get_client_checklists](docs/sdks/organizationchecklists/README.md#get_client_checklists) - List client checklists
* [update_organization_checklists](docs/sdks/organizationchecklists/README.md#update_organization_checklists) - Update organization checklists
* [create_organization_checklists](docs/sdks/organizationchecklists/README.md#create_organization_checklists) - Create organization checklists
* [create_organization_checklists_from_templates](docs/sdks/organizationchecklists/README.md#create_organization_checklists_from_templates) - Create organization checklists from templates
* [get_client_checklist](docs/sdks/organizationchecklists/README.md#get_client_checklist) - Get client checklist
* [delete_client_checklist](docs/sdks/organizationchecklists/README.md#delete_client_checklist) - Delete an organization checklist
* [delete_client_checklists](docs/sdks/organizationchecklists/README.md#delete_client_checklists) - Delete organization checklists
* [get_client_checklist_signed_urls](docs/sdks/organizationchecklists/README.md#get_client_checklist_signed_urls) - Get organization checklist signed urls
* [promote_client_checklists](docs/sdks/organizationchecklists/README.md#promote_client_checklists) - Promote organization checklists
* [promote_client_checklists_1](docs/sdks/organizationchecklists/README.md#promote_client_checklists_1) - Promote organization checklists
* [restore_organization_checklists](docs/sdks/organizationchecklists/README.md#restore_organization_checklists) - Restore organization checklists

### [organization_documents](docs/sdks/organizationdocuments/README.md)

* [archive_client_document](docs/sdks/organizationdocuments/README.md#archive_client_document) - Archive an organization document
* [archive_multi_page_client_documents](docs/sdks/organizationdocuments/README.md#archive_multi_page_client_documents) - Archives organization documents
* [create_organization_document](docs/sdks/organizationdocuments/README.md#create_organization_document) - Create organization document
* [get_client_documents_with_attribute_values](docs/sdks/organizationdocuments/README.md#get_client_documents_with_attribute_values) - List all organization documents with field values
* [create_organization_documents](docs/sdks/organizationdocuments/README.md#create_organization_documents) - Create organization documents
* [update_organization_documents](docs/sdks/organizationdocuments/README.md#update_organization_documents) - Update organization documents
* [delete_client_document](docs/sdks/organizationdocuments/README.md#delete_client_document) - Delete an archived organization document
* [get_client_document_signed_urls](docs/sdks/organizationdocuments/README.md#get_client_document_signed_urls) - Get organization document signed urls
* [get_organization_documents](docs/sdks/organizationdocuments/README.md#get_organization_documents) - List organization documents with field values
* [restore_client_document](docs/sdks/organizationdocuments/README.md#restore_client_document) - Restore an organization document
* [restore_multi_page_client_documents](docs/sdks/organizationdocuments/README.md#restore_multi_page_client_documents) - Restore multiple multi page organization documents
* [update_organization_document](docs/sdks/organizationdocuments/README.md#update_organization_document) - Update organization document

### [queries](docs/sdks/queries/README.md)

* [get_antivirus_status_report](docs/sdks/queries/README.md#get_antivirus_status_report) - Antivirus status report
* [get_antivirus_threats](docs/sdks/queries/README.md#get_antivirus_threats) - Antivirus threats report
* [get_computer_systems](docs/sdks/queries/README.md#get_computer_systems) - Computer systems report
* [get_custom_fields_detailed_report](docs/sdks/queries/README.md#get_custom_fields_detailed_report) - Custom fields detailed report
* [get_custom_fields_report](docs/sdks/queries/README.md#get_custom_fields_report) - Custom fields report
* [get_device_health_report](docs/sdks/queries/README.md#get_device_health_report) - Device health report
* [get_device_usage](docs/sdks/queries/README.md#get_device_usage) - Device backup usage
* [get_disk_drives](docs/sdks/queries/README.md#get_disk_drives) - Disk drives report
* [get_installed_os_patches](docs/sdks/queries/README.md#get_installed_os_patches) - OS Patch installation report
* [get_installed_software_patches](docs/sdks/queries/README.md#get_installed_software_patches) - Software Patch history report
* [get_last_logged_on_users_report](docs/sdks/queries/README.md#get_last_logged_on_users_report) - Last logged-on user report
* [get_network_interfaces](docs/sdks/queries/README.md#get_network_interfaces) - List Network Interfaces
* [get_operating_systems](docs/sdks/queries/README.md#get_operating_systems) - Operating systems report
* [get_pending_failed_rejected_os_patches](docs/sdks/queries/README.md#get_pending_failed_rejected_os_patches) - Pending, Failed and Rejected OS patches report
* [get_pending_failed_rejected_software_patches](docs/sdks/queries/README.md#get_pending_failed_rejected_software_patches) - Pending, Failed and Rejected Software patches report
* [get_policy_overrides_1](docs/sdks/queries/README.md#get_policy_overrides_1) - Get summary of device policy overrides
* [get_processors](docs/sdks/queries/README.md#get_processors) - Processor report
* [get_raid_controller_report](docs/sdks/queries/README.md#get_raid_controller_report) - RAID controller report
* [get_raid_drive_report](docs/sdks/queries/README.md#get_raid_drive_report) - RAID drive report
* [get_scoped_custom_fields_detailed_report](docs/sdks/queries/README.md#get_scoped_custom_fields_detailed_report) - Scoped custom fields detailed report
* [get_scoped_custom_fields_report](docs/sdks/queries/README.md#get_scoped_custom_fields_report) - Scoped custom fields report
* [get_software](docs/sdks/queries/README.md#get_software) - Software inventory
* [get_volumes](docs/sdks/queries/README.md#get_volumes) - Disk volumes report
* [get_windows_services_report](docs/sdks/queries/README.md#get_windows_services_report) - Windows services report

### [related_items](docs/sdks/relateditems/README.md)

* [create_related_item](docs/sdks/relateditems/README.md#create_related_item) - Create Attachment Relation
* [create_related_item_for_entity](docs/sdks/relateditems/README.md#create_related_item_for_entity) - Create entity relation
* [create_related_item_for_entity_1](docs/sdks/relateditems/README.md#create_related_item_for_entity_1) - Create entity relations
* [create_secure_related_item_for_entity](docs/sdks/relateditems/README.md#create_secure_related_item_for_entity) - Create Secure Relation
* [delete_related_item](docs/sdks/relateditems/README.md#delete_related_item) - Delete related item
* [delete_related_items](docs/sdks/relateditems/README.md#delete_related_items) - Delete related items
* [get_all_related_items](docs/sdks/relateditems/README.md#get_all_related_items) - List all related items
* [get_related_items_for_host_entity](docs/sdks/relateditems/README.md#get_related_items_for_host_entity) - List host entity related items by scope
* [get_related_items_with_entity](docs/sdks/relateditems/README.md#get_related_items_with_entity) - List related entity related items
* [get_related_items_with_entity_type](docs/sdks/relateditems/README.md#get_related_items_with_entity_type) - List related entity type related items
* [get_related_items_with_host_entity_type](docs/sdks/relateditems/README.md#get_related_items_with_host_entity_type) - List host entity type related items

### [system](docs/sdks/system/README.md)

* [get_organizations](docs/sdks/system/README.md#get_organizations) - List organizations
* [get_policies](docs/sdks/system/README.md#get_policies) - List policies
* [get_active_jobs](docs/sdks/system/README.md#get_active_jobs) - List active jobs
* [get_activities](docs/sdks/system/README.md#get_activities) - List activities
* [get_alerts](docs/sdks/system/README.md#get_alerts) - List active alerts (triggered conditions)
* [get_automation_scripts](docs/sdks/system/README.md#get_automation_scripts) - List all available automation scripts
* [get_device_global_custom_fields](docs/sdks/system/README.md#get_device_global_custom_fields) - Device Custom Fields
* [get_devices](docs/sdks/system/README.md#get_devices) - List devices
* [get_devices_detailed](docs/sdks/system/README.md#get_devices_detailed) - List devices (detailed)
* [get_enabled_notification_channels](docs/sdks/system/README.md#get_enabled_notification_channels) - List enabled notification channels
* [get_groups](docs/sdks/system/README.md#get_groups) - List groups (saved searches)
* [get_locations](docs/sdks/system/README.md#get_locations) - List locations
* [get_node_roles](docs/sdks/system/README.md#get_node_roles) - List device roles
* [get_notification_channels](docs/sdks/system/README.md#get_notification_channels) - List notification channels
* [get_organizations_detailed](docs/sdks/system/README.md#get_organizations_detailed) - List organizations (Detailed)
* [get_scheduled_tasks](docs/sdks/system/README.md#get_scheduled_tasks) - List scheduled tasks
* [get_software_products](docs/sdks/system/README.md#get_software_products) - List supported 3rd party software
* [get_users](docs/sdks/system/README.md#get_users) - List users
* [search](docs/sdks/system/README.md#search) - Find devices

### [ticketing](docs/sdks/ticketing/README.md)

* [create](docs/sdks/ticketing/README.md#create) - Create ticket
* [create_comment](docs/sdks/ticketing/README.md#create_comment) - Add comment to ticket
* [get_ticket_by_id](docs/sdks/ticketing/README.md#get_ticket_by_id) - Ticket
* [update](docs/sdks/ticketing/README.md#update) - Update ticket
* [get_ticket_log_entries_by_ticket_id](docs/sdks/ticketing/README.md#get_ticket_log_entries_by_ticket_id) - List ticket log entries
* [get_ticket_attributes](docs/sdks/ticketing/README.md#get_ticket_attributes) - List ticket attributes
* [get_contacts](docs/sdks/ticketing/README.md#get_contacts) - List contacts
* [get_ticket_form_by_id](docs/sdks/ticketing/README.md#get_ticket_form_by_id) - Ticket form
* [get_ticket_forms](docs/sdks/ticketing/README.md#get_ticket_forms) - List ticket forms
* [get_all_statuses](docs/sdks/ticketing/README.md#get_all_statuses) - Get list of ticket status
* [get_boards](docs/sdks/ticketing/README.md#get_boards) - List boards
* [get_tickets_by_board](docs/sdks/ticketing/README.md#get_tickets_by_board) - List of tickets for board
* [get_all_user_and_contacts](docs/sdks/ticketing/README.md#get_all_user_and_contacts) - List of users by user type

### [webhooks](docs/sdks/webhooks/README.md)

* [configure_webhook](docs/sdks/webhooks/README.md#configure_webhook) - Update API Webhook configuration
* [disable_webhook](docs/sdks/webhooks/README.md#disable_webhook) - Remove Webhook API channel

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

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
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import ninjapy
from ninjapy import Ninjapy
from ninjapy.utils import BackoffStrategy, RetryConfig
import os


with Ninjapy(
    server_url="https://api.example.com",
    security=ninjapy.Security(
        oauth2=os.getenv("NINJAPY_OAUTH2", ""),
    ),
) as n_client:

    res = n_client.management.get_custom_fields_policy_conditions(policy_id=373422,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import ninjapy
from ninjapy import Ninjapy
from ninjapy.utils import BackoffStrategy, RetryConfig
import os


with Ninjapy(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=ninjapy.Security(
        oauth2=os.getenv("NINJAPY_OAUTH2", ""),
    ),
) as n_client:

    res = n_client.management.get_custom_fields_policy_conditions(policy_id=373422)

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_custom_fields_policy_conditions_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| models.APIError | 4XX, 5XX    | \*/\*        |

### Example

```python
import ninjapy
from ninjapy import Ninjapy, models
import os


with Ninjapy(
    server_url="https://api.example.com",
    security=ninjapy.Security(
        oauth2=os.getenv("NINJAPY_OAUTH2", ""),
    ),
) as n_client:
    res = None
    try:

        res = n_client.management.get_custom_fields_policy_conditions(policy_id=373422)

        # Handle response
        print(res)

    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from ninjapy import Ninjapy
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Ninjapy(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from ninjapy import Ninjapy
from ninjapy.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Ninjapy(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Ninjapy` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import ninjapy
from ninjapy import Ninjapy
import os
def main():

    with Ninjapy(
        server_url="https://api.example.com",
        security=ninjapy.Security(
            oauth2=os.getenv("NINJAPY_OAUTH2", ""),
        ),
    ) as n_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Ninjapy(
        server_url="https://api.example.com",
        security=ninjapy.Security(
            oauth2=os.getenv("NINJAPY_OAUTH2", ""),
        ),
    ) as n_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from ninjapy import Ninjapy
import logging

logging.basicConfig(level=logging.DEBUG)
s = Ninjapy(server_url="https://example.com", debug_logger=logging.getLogger("ninjapy"))
```

You can also enable a default debug logger by setting an environment variable `NINJAPY_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=ninjapy&utm_campaign=python)
