# GetVolumesBitLockerStatus

BitLocker Status


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `conversion_status`                                                                    | [Optional[models.GetVolumesConversionStatus]](../models/getvolumesconversionstatus.md) | :heavy_minus_sign:                                                                     | Volume encryption or decryption status.                                                |
| `encryption_method`                                                                    | [Optional[models.GetVolumesEncryptionMethod]](../models/getvolumesencryptionmethod.md) | :heavy_minus_sign:                                                                     | Indicated the encryption algorithm and key size used on the volume                     |
| `protection_status`                                                                    | [Optional[models.GetVolumesProtectionStatus]](../models/getvolumesprotectionstatus.md) | :heavy_minus_sign:                                                                     |  indicates whether the volume and its encryption key (if any) are secured.             |
| `lock_status`                                                                          | [Optional[models.GetVolumesLockStatus]](../models/getvolumeslockstatus.md)             | :heavy_minus_sign:                                                                     | Indicates whether the contents of the volume are accessible from Windows               |
| `initialized_for_protection`                                                           | *Optional[bool]*                                                                       | :heavy_minus_sign:                                                                     | Is initialized for protection                                                          |