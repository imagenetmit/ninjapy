# ConfigureWebhookRequestBody


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `url`                                             | *Optional[str]*                                   | :heavy_minus_sign:                                | Callback (WebHook) URL for activity notifications |
| `activities`                                      | Dict[str, List[*str*]]                            | :heavy_minus_sign:                                | Activity filter                                   |
| `expand`                                          | List[*str*]                                       | :heavy_minus_sign:                                | Which references to expand in payloads            |
| `headers`                                         | List[[models.Headers](../models/headers.md)]      | :heavy_minus_sign:                                | Custom HTTP Headers (i.e. Authorization)          |