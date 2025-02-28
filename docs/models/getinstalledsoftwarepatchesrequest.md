# GetInstalledSoftwarePatchesRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `df`                                            | *Optional[str]*                                 | :heavy_minus_sign:                              | Device filter                                   |
| `type`                                          | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Type filter                               |
| `impact`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Impact filter                             |
| `status`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Status filter                             |
| `product_identifier`                            | *Optional[str]*                                 | :heavy_minus_sign:                              | Product Identifier                              |
| `installed_before`                              | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed before specified date |
| `installed_after`                               | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed after specified date  |
| `cursor`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Cursor name                                     |
| `page_size`                                     | *Optional[int]*                                 | :heavy_minus_sign:                              | Limit number of records per page                |