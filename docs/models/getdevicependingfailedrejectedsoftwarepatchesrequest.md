# GetDevicePendingFailedRejectedSoftwarePatchesRequest


## Fields

| Field                | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `id`                 | *int*                | :heavy_check_mark:   | Device identifier    |
| `status`             | *Optional[str]*      | :heavy_minus_sign:   | Patch Status filter  |
| `product_identifier` | *Optional[str]*      | :heavy_minus_sign:   | Product Identifier   |
| `type`               | *Optional[str]*      | :heavy_minus_sign:   | Patch Type filter    |
| `impact`             | *Optional[str]*      | :heavy_minus_sign:   | Patch Impact filter  |