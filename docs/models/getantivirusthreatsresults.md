# GetAntivirusThreatsResults


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `name`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | Threat name                                       |
| `product_code`                                    | *Optional[str]*                                   | :heavy_minus_sign:                                | AntiVirus vendor product code                     |
| `quarantine_id`                                   | *Optional[str]*                                   | :heavy_minus_sign:                                | Threat Quarantine ID                              |
| `status`                                          | *Optional[str]*                                   | :heavy_minus_sign:                                | Threat Status (vendor specific)                   |
| `type`                                            | *Optional[str]*                                   | :heavy_minus_sign:                                | Type of Threat                                    |
| `threat_id`                                       | *Optional[int]*                                   | :heavy_minus_sign:                                | Threat ID                                         |
| `category`                                        | *Optional[str]*                                   | :heavy_minus_sign:                                | Threat Category                                   |
| `level`                                           | *Optional[str]*                                   | :heavy_minus_sign:                                | Threat Level                                      |
| `detection_source`                                | *Optional[str]*                                   | :heavy_minus_sign:                                | Detection source                                  |
| `trace_list`                                      | *Optional[str]*                                   | :heavy_minus_sign:                                | Trace list (Files, Cookies, etc. Vendor specific) |
| `device_id`                                       | *Optional[int]*                                   | :heavy_minus_sign:                                | Device identifier                                 |
| `timestamp`                                       | *Optional[float]*                                 | :heavy_minus_sign:                                | Date/Time when data was collected/updated         |