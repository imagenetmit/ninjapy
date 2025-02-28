# GetDevicesReferences

Expanded entity references


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `organization`                                                                 | [Optional[models.GetDevicesOrganization]](../models/getdevicesorganization.md) | :heavy_minus_sign:                                                             | Organization                                                                   |
| `location`                                                                     | [Optional[models.GetDevicesLocation]](../models/getdeviceslocation.md)         | :heavy_minus_sign:                                                             | Location                                                                       |
| `role_policy`                                                                  | [Optional[models.GetDevicesRolePolicy]](../models/getdevicesrolepolicy.md)     | :heavy_minus_sign:                                                             | Assigned policy (overrides organization and location policy mapping)           |
| `policy`                                                                       | [Optional[models.GetDevicesPolicy]](../models/getdevicespolicy.md)             | :heavy_minus_sign:                                                             | Assigned policy (overrides organization and location policy mapping)           |
| `role`                                                                         | [Optional[models.GetDevicesRole]](../models/getdevicesrole.md)                 | :heavy_minus_sign:                                                             | Device Role                                                                    |
| `backup_usage`                                                                 | [Optional[models.GetDevicesBackupUsage]](../models/getdevicesbackupusage.md)   | :heavy_minus_sign:                                                             | Device Backup Usage                                                            |
| `warranty`                                                                     | [Optional[models.GetDevicesWarranty]](../models/getdeviceswarranty.md)         | :heavy_minus_sign:                                                             | Warranty Info                                                                  |