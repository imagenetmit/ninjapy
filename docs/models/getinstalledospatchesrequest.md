# GetInstalledOSPatchesRequest


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `df`                                            | *Optional[str]*                                 | :heavy_minus_sign:                              | Device filter                                   |
| `status`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Patch Status filter (FAILED, INSTALLED)         |
| `installed_before`                              | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed before specified date |
| `installed_after`                               | *Optional[str]*                                 | :heavy_minus_sign:                              | Include patches installed after specified date  |
| `cursor`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Cursor name                                     |
| `page_size`                                     | *Optional[int]*                                 | :heavy_minus_sign:                              | Limit number of records per page                |