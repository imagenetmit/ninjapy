# RequestBody


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *Optional[int]*                                          | :heavy_minus_sign:                                       | Checklist template identifier                            |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | Checklist template name (must be unique)                 |
| `description`                                            | [Optional[models.Description]](../models/description.md) | :heavy_minus_sign:                                       | Task description                                         |
| `tasks`                                                  | List[[models.Tasks](../models/tasks.md)]                 | :heavy_minus_sign:                                       | Checklist's tasks                                        |
| `required`                                               | *Optional[bool]*                                         | :heavy_minus_sign:                                       | Indicates if the checklist is required                   |