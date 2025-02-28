# GetDeviceInstalledSoftwarePatchesRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `id`                                            | *int*                                           | :heavy_check_mark:                              | Device identifier                               |
| `type`                                          | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Type filter                               |
| `impact`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Impact filter                             |
| `status`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Status filter                             |
| `product_identifier`                            | *Optional[str]*                                 | :heavy_minus_sign:                              | Product Identifier                              |
| `installed_before`                              | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed before specified date |
| `installed_after`                               | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed after specified date  |