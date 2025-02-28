# GetInstallerRequestBody


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `organization_id`                                                        | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Organization identifier                                                  |
| `location_id`                                                            | *Optional[int]*                                                          | :heavy_minus_sign:                                                       | Location identifier                                                      |
| `installer_type`                                                         | [Optional[models.InstallerType]](../models/installertype.md)             | :heavy_minus_sign:                                                       | Agent installer type                                                     |
| `content`                                                                | [Optional[models.GetInstallerContent]](../models/getinstallercontent.md) | :heavy_minus_sign:                                                       | content                                                                  |