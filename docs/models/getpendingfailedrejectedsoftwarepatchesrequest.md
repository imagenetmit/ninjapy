# GetPendingFailedRejectedSoftwarePatchesRequest


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `df`                             | *Optional[str]*                  | :heavy_minus_sign:               | Device filter                    |
| `ts`                             | *Optional[str]*                  | :heavy_minus_sign:               | Monitoring timestamp filter      |
| `status`                         | *Optional[str]*                  | :heavy_minus_sign:               | Patch Status filter              |
| `product_identifier`             | *Optional[str]*                  | :heavy_minus_sign:               | Product Identifier               |
| `type`                           | *Optional[str]*                  | :heavy_minus_sign:               | Patch Type filter                |
| `impact`                         | *Optional[str]*                  | :heavy_minus_sign:               | Patch Impact filter              |
| `cursor`                         | *Optional[str]*                  | :heavy_minus_sign:               | Cursor name                      |
| `page_size`                      | *Optional[int]*                  | :heavy_minus_sign:               | Limit number of records per page |