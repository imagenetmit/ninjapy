# GetScheduledTasksResponseBody


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *Optional[int]*                      | :heavy_minus_sign:                   | Scheduled Task identifier            |
| `name`                               | *Optional[str]*                      | :heavy_minus_sign:                   | Name                                 |
| `description`                        | *Optional[str]*                      | :heavy_minus_sign:                   | Description                          |
| `enabled`                            | *Optional[bool]*                     | :heavy_minus_sign:                   | Is Enabled ?                         |
| `created`                            | *Optional[float]*                    | :heavy_minus_sign:                   | Timestamp of Scheduled Task creation |
| `last_run`                           | *Optional[float]*                    | :heavy_minus_sign:                   | Timestamp of last Scheduled Task run |
| `run_count`                          | *Optional[int]*                      | :heavy_minus_sign:                   | Number of times scheduled task ran   |