# GetVolumesRequest


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `df`                                                      | *Optional[str]*                                           | :heavy_minus_sign:                                        | Device filter                                             |
| `ts`                                                      | *Optional[str]*                                           | :heavy_minus_sign:                                        | Monitoring timestamp filter                               |
| `cursor`                                                  | *Optional[str]*                                           | :heavy_minus_sign:                                        | Cursor name                                               |
| `page_size`                                               | *Optional[int]*                                           | :heavy_minus_sign:                                        | Limit number of records per page                          |
| `include`                                                 | *Optional[str]*                                           | :heavy_minus_sign:                                        | Additional information to include (bl - BitLocker status) |