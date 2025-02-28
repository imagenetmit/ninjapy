# Scripts

Policy condition script


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `script_id`                                                  | *Optional[int]*                                              | :heavy_minus_sign:                                           | Policy condition script id                                   |
| `run_as`                                                     | [Optional[models.RunAs]](../models/runas.md)                 | :heavy_minus_sign:                                           | Policy condition script runAs                                |
| `script_param`                                               | *Optional[str]*                                              | :heavy_minus_sign:                                           | Policy condition script parameter                            |
| `script_variables`                                           | List[[models.ScriptVariables](../models/scriptvariables.md)] | :heavy_minus_sign:                                           | Policy condition script variables                            |