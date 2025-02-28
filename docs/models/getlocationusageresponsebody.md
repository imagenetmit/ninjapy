# GetLocationUsageResponseBody

Returns a location backup usage


## Fields

| Field                        | Type                         | Required                     | Description                  |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `location_id`                | *Optional[int]*              | :heavy_minus_sign:           | Device location id           |
| `location_name`              | *Optional[str]*              | :heavy_minus_sign:           | Device location name         |
| `location_description`       | *Optional[str]*              | :heavy_minus_sign:           | Device location description  |
| `revisions_current_size`     | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `revisions_previous_size`    | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `revisions_deleted_size`     | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `local_file_folder_size`     | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `local_image_size`           | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `local_image_v2_size`        | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `cloud_file_folder_size`     | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `cloud_image_size`           | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `cloud_image_v2_size`        | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `last_successful_backup_job` | *Optional[float]*            | :heavy_minus_sign:           | N/A                          |
| `last_failed_backup_job`     | *Optional[float]*            | :heavy_minus_sign:           | N/A                          |
| `organization_id`            | *Optional[int]*              | :heavy_minus_sign:           | N/A                          |
| `organization_name`          | *Optional[str]*              | :heavy_minus_sign:           | N/A                          |
| `revisions_total_size`       | *Optional[int]*              | :heavy_minus_sign:           | Revisions total size         |
| `cloud_total_size`           | *Optional[int]*              | :heavy_minus_sign:           | Revisions cloud total size   |
| `local_total_size`           | *Optional[int]*              | :heavy_minus_sign:           | Revisions local total size   |