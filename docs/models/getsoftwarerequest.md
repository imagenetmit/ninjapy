# GetSoftwareRequest


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `df`                                             | *Optional[str]*                                  | :heavy_minus_sign:                               | Device filter                                    |
| `cursor`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Cursor name                                      |
| `page_size`                                      | *Optional[int]*                                  | :heavy_minus_sign:                               | Limit number of records per page                 |
| `installed_before`                               | *Optional[str]*                                  | :heavy_minus_sign:                               | Include software installed before specified date |
| `installed_after`                                | *Optional[str]*                                  | :heavy_minus_sign:                               | Include software installed after specified date  |