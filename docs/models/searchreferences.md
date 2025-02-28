# SearchReferences

Expanded entity references


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `organization`                                                         | [Optional[models.SearchOrganization]](../models/searchorganization.md) | :heavy_minus_sign:                                                     | Organization                                                           |
| `location`                                                             | [Optional[models.SearchLocation]](../models/searchlocation.md)         | :heavy_minus_sign:                                                     | Location                                                               |
| `role_policy`                                                          | [Optional[models.SearchRolePolicy]](../models/searchrolepolicy.md)     | :heavy_minus_sign:                                                     | Assigned policy (overrides organization and location policy mapping)   |
| `policy`                                                               | [Optional[models.SearchPolicy]](../models/searchpolicy.md)             | :heavy_minus_sign:                                                     | Assigned policy (overrides organization and location policy mapping)   |
| `role`                                                                 | [Optional[models.SearchRole]](../models/searchrole.md)                 | :heavy_minus_sign:                                                     | Device Role                                                            |
| `backup_usage`                                                         | [Optional[models.SearchBackupUsage]](../models/searchbackupusage.md)   | :heavy_minus_sign:                                                     | Device Backup Usage                                                    |
| `warranty`                                                             | [Optional[models.SearchWarranty]](../models/searchwarranty.md)         | :heavy_minus_sign:                                                     | Warranty Info                                                          |