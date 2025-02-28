# GetDeviceActiveJobsResponseBody


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `uid`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Task/Job UID (activity series UID)                       |
| `device_id`                                              | *Optional[int]*                                          | :heavy_minus_sign:                                       | Device identifier                                        |
| `message`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | Job message                                              |
| `create_time`                                            | *Optional[float]*                                        | :heavy_minus_sign:                                       | Job start timestamp                                      |
| `update_time`                                            | *Optional[float]*                                        | :heavy_minus_sign:                                       | Job last updated                                         |
| `source_type`                                            | [Optional[models.SourceType]](../models/sourcetype.md)   | :heavy_minus_sign:                                       | Job origin                                               |
| `source_config_uid`                                      | *Optional[str]*                                          | :heavy_minus_sign:                                       | Source configuration/policy element reference            |
| `source_name`                                            | *Optional[str]*                                          | :heavy_minus_sign:                                       | Source configuration/policy element name                 |
| `subject`                                                | *Optional[str]*                                          | :heavy_minus_sign:                                       | Job subject                                              |
| `user_id`                                                | *Optional[int]*                                          | :heavy_minus_sign:                                       | User identifier                                          |
| `psa_ticket_id`                                          | [Optional[models.PsaTicketID]](../models/psaticketid.md) | :heavy_minus_sign:                                       | Related PSA ticket ID                                    |
| `ticket_template_id`                                     | *Optional[int]*                                          | :heavy_minus_sign:                                       | PSA ticket template                                      |
| `data`                                                   | Dict[str, *Any*]                                         | :heavy_minus_sign:                                       | Job data                                                 |
| `device`                                                 | [Optional[models.Device]](../models/device.md)           | :heavy_minus_sign:                                       | Device information.                                      |
| `job_status`                                             | [Optional[models.JobStatus]](../models/jobstatus.md)     | :heavy_minus_sign:                                       | Job Status                                               |
| `job_result`                                             | [Optional[models.JobResult]](../models/jobresult.md)     | :heavy_minus_sign:                                       | Job result                                               |
| `job_type`                                               | [Optional[models.JobType]](../models/jobtype.md)         | :heavy_minus_sign:                                       | Job Type                                                 |