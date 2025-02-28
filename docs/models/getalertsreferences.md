# GetAlertsReferences

Expanded entity references


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `organization`                                                               | [Optional[models.GetAlertsOrganization]](../models/getalertsorganization.md) | :heavy_minus_sign:                                                           | Organization                                                                 |
| `location`                                                                   | [Optional[models.GetAlertsLocation]](../models/getalertslocation.md)         | :heavy_minus_sign:                                                           | Location                                                                     |
| `role_policy`                                                                | [Optional[models.GetAlertsRolePolicy]](../models/getalertsrolepolicy.md)     | :heavy_minus_sign:                                                           | Assigned policy (overrides organization and location policy mapping)         |
| `policy`                                                                     | [Optional[models.GetAlertsPolicy]](../models/getalertspolicy.md)             | :heavy_minus_sign:                                                           | Assigned policy (overrides organization and location policy mapping)         |
| `role`                                                                       | [Optional[models.GetAlertsRole]](../models/getalertsrole.md)                 | :heavy_minus_sign:                                                           | Device Role                                                                  |
| `backup_usage`                                                               | [Optional[models.GetAlertsBackupUsage]](../models/getalertsbackupusage.md)   | :heavy_minus_sign:                                                           | Device Backup Usage                                                          |
| `warranty`                                                                   | [Optional[models.GetAlertsWarranty]](../models/getalertswarranty.md)         | :heavy_minus_sign:                                                           | Warranty Info                                                                |