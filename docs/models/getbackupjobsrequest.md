# GetBackupJobsRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `df`                                                            | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Device filter                                                   |
| `ddf`                                                           | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Deleted device filter                                           |
| `sf`                                                            | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Backup job status filter                                        |
| `ptf`                                                           | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Backup job planType filter                                      |
| `stf`                                                           | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Backup job startTime filter                                     |
| `include`                                                       | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Which devices include (active\|deleted\|all) default value active |
| `cursor`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Cursor name                                                     |
| `page_size`                                                     | *Optional[int]*                                                 | :heavy_minus_sign:                                              | Limit number of records per page                                |