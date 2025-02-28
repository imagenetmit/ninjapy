# GetPendingFailedRejectedOSPatchesRequest


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `df`                             | *Optional[str]*                  | :heavy_minus_sign:               | Device filter                    |
| `ts`                             | *Optional[str]*                  | :heavy_minus_sign:               | Monitoring timestamp filter      |
| `status`                         | *Optional[str]*                  | :heavy_minus_sign:               | Patch Status filter              |
| `type`                           | *Optional[str]*                  | :heavy_minus_sign:               | Patch Type filter                |
| `severity`                       | *Optional[str]*                  | :heavy_minus_sign:               | Patch Severity filter            |
| `cursor`                         | *Optional[str]*                  | :heavy_minus_sign:               | Cursor name                      |
| `page_size`                      | *Optional[int]*                  | :heavy_minus_sign:               | Limit number of records per page |