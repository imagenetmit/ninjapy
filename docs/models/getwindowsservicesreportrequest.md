# GetWindowsServicesReportRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `df`                                                             | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Device filter                                                    |
| `name`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Service name                                                     |
| `state`                                                          | [Optional[models.QueryParamState]](../models/queryparamstate.md) | :heavy_minus_sign:                                               | Service state                                                    |
| `cursor`                                                         | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Cursor name                                                      |
| `page_size`                                                      | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Limit number of records per page                                 |