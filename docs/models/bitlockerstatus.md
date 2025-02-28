# BitLockerStatus

BitLocker Status


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `conversion_status`                                                        | [Optional[models.ConversionStatus]](../models/conversionstatus.md)         | :heavy_minus_sign:                                                         | Volume encryption or decryption status.                                    |
| `encryption_method`                                                        | [Optional[models.EncryptionMethod]](../models/encryptionmethod.md)         | :heavy_minus_sign:                                                         | Indicated the encryption algorithm and key size used on the volume         |
| `protection_status`                                                        | [Optional[models.ProtectionStatus]](../models/protectionstatus.md)         | :heavy_minus_sign:                                                         |  indicates whether the volume and its encryption key (if any) are secured. |
| `lock_status`                                                              | [Optional[models.LockStatus]](../models/lockstatus.md)                     | :heavy_minus_sign:                                                         | Indicates whether the contents of the volume are accessible from Windows   |
| `initialized_for_protection`                                               | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Is initialized for protection                                              |