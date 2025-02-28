# GetDeviceVolumesResponseBody

Disk Volumes


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Name                                                             |
| `drive_letter`                                                   | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Drive Letter                                                     |
| `label`                                                          | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Volume Label                                                     |
| `device_type`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Device Type                                                      |
| `file_system`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | File System Type                                                 |
| `auto_mount`                                                     | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Automatically Mounted                                            |
| `compressed`                                                     | *Optional[bool]*                                                 | :heavy_minus_sign:                                               | Compressed                                                       |
| `capacity`                                                       | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Capacity (bytes)                                                 |
| `free_space`                                                     | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Free Space (bytes)                                               |
| `serial_number`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Serial Number                                                    |
| `bit_locker_status`                                              | [Optional[models.BitLockerStatus]](../models/bitlockerstatus.md) | :heavy_minus_sign:                                               | BitLocker Status                                                 |