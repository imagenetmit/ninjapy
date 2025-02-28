# GetOperatingSystemsResults


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `manufacturer`                               | *Optional[str]*                              | :heavy_minus_sign:                           | Manufacturer                                 |
| `name`                                       | *Optional[str]*                              | :heavy_minus_sign:                           | Name                                         |
| `architecture`                               | *Optional[str]*                              | :heavy_minus_sign:                           | Architecture                                 |
| `last_boot_time`                             | *Optional[float]*                            | :heavy_minus_sign:                           | Last boot time                               |
| `build_number`                               | *Optional[str]*                              | :heavy_minus_sign:                           | Build number                                 |
| `release_id`                                 | *Optional[str]*                              | :heavy_minus_sign:                           | Release ID                                   |
| `service_pack_major_version`                 | *Optional[int]*                              | :heavy_minus_sign:                           | Service Pack Major Version                   |
| `service_pack_minor_version`                 | *Optional[int]*                              | :heavy_minus_sign:                           | Service Pack Minor Version                   |
| `locale`                                     | *Optional[str]*                              | :heavy_minus_sign:                           | Locale                                       |
| `language`                                   | *Optional[str]*                              | :heavy_minus_sign:                           | Language                                     |
| `needs_reboot`                               | *Optional[bool]*                             | :heavy_minus_sign:                           | Operating system has pending reboot requests |
| `device_id`                                  | *Optional[int]*                              | :heavy_minus_sign:                           | Device identifier                            |
| `timestamp`                                  | *Optional[float]*                            | :heavy_minus_sign:                           | Date/Time when data was collected/updated    |