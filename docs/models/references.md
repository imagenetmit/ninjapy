# References

Expanded entity references


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `organization`                                                               | [Optional[models.GetDeviceOrganization]](../models/getdeviceorganization.md) | :heavy_minus_sign:                                                           | Organization                                                                 |
| `location`                                                                   | [Optional[models.GetDeviceLocation]](../models/getdevicelocation.md)         | :heavy_minus_sign:                                                           | Location                                                                     |
| `role_policy`                                                                | [Optional[models.RolePolicy]](../models/rolepolicy.md)                       | :heavy_minus_sign:                                                           | Assigned policy (overrides organization and location policy mapping)         |
| `policy`                                                                     | [Optional[models.Policy]](../models/policy.md)                               | :heavy_minus_sign:                                                           | Assigned policy (overrides organization and location policy mapping)         |
| `role`                                                                       | [Optional[models.Role]](../models/role.md)                                   | :heavy_minus_sign:                                                           | Device Role                                                                  |
| `backup_usage`                                                               | [Optional[models.BackupUsage]](../models/backupusage.md)                     | :heavy_minus_sign:                                                           | Device Backup Usage                                                          |
| `warranty`                                                                   | [Optional[models.GetDeviceWarranty]](../models/getdevicewarranty.md)         | :heavy_minus_sign:                                                           | Warranty Info                                                                |