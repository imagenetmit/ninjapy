# GetAllUserAndContactsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `page_size`                                                            | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Limit number of records per page                                       |
| `anchor_natural_id`                                                    | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Last User Identifier from previous page                                |
| `search_criteria`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Search by first name, last name or email address                       |
| `user_type`                                                            | [Optional[models.QueryParamUserType]](../models/queryparamusertype.md) | :heavy_minus_sign:                                                     | User Type                                                              |
| `client_id`                                                            | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | Organization identifier                                                |