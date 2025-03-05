# Client SDK

## Overview

Messaging Gateway SzybkiSMS.pl (former GSMService.pl): This package includes Messaging SDK for Python to send SMS and MMS messages directly from your app via [https://szybkisms.pl](https://szybkisms.pl) messaging platform.

*Client* class is used to initialize SDK environment.

Please initialize it this way:

```
from gsmservice_gateway import Client
import os

s = Client(
      bearer=os.getenv("GATEWAY_API_BEARER", ""),
   )
```

If you want to use a Sandbox test system please initialize it as follows:

```
from gsmservice_gateway import Client, SERVER_SANDBOX

s = Client(
      bearer=os.getenv("GATEWAY_API_BEARER", ""),
      server=SERVER_SANDBOX
) var sdk = new Client(bearer: "YOUR API ACCESS TOKEN", null, SDKConfig.Server.Sandbox);

```

SzybkiSMS.pl
<https://szybkisms.pl>

### Available Operations
