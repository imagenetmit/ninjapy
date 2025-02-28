# GetDeviceInstalledOSPatchesRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `id`                                            | *int*                                           | :heavy_check_mark:                              | Device identifier                               |
| `status`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Status filter (FAILED, INSTALLED)         |
| `installed_before`                              | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed before specified date |
| `installed_after`                               | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed after specified date  |