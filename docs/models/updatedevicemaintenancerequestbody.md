# UpdateDeviceMaintenanceRequestBody


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `disabled_features`                                            | List[[models.DisabledFeatures](../models/disabledfeatures.md)] | :heavy_minus_sign:                                             | List of features that will be disabled during maintenance      |
| `start`                                                        | *Optional[float]*                                              | :heavy_minus_sign:                                             | Maintenance window start (optional, defaults to now)           |
| `end`                                                          | *Optional[float]*                                              | :heavy_minus_sign:                                             | Maintenance window end                                         |