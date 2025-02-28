<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import ninjapy
from ninjapy import Ninjapy
import os


with Ninjapy(
    server_url="https://api.example.com",
    security=ninjapy.Security(
        oauth2=os.getenv("NINJAPY_OAUTH2", ""),
    ),
) as n_client:

    res = n_client.management.get_custom_fields_policy_conditions(policy_id=373422)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import ninjapy
from ninjapy import Ninjapy
import os

async def main():

    async with Ninjapy(
        server_url="https://api.example.com",
        security=ninjapy.Security(
            oauth2=os.getenv("NINJAPY_OAUTH2", ""),
        ),
    ) as n_client:

        res = await n_client.management.get_custom_fields_policy_conditions_async(policy_id=373422)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->