![BANNER](https://github.com/kartikmehta8/HTMLaaS/assets/77505989/061ffb2d-9ac8-4367-a57c-65c5b7302363)

<h3 align="center">
  Why to use a third party API when you can yourself create one?
</h3>

HTMLaaS offers users the ability to query and extract specific information from HTML documents. Users can retrieve the page `title`, extract all `links`, access the `entire HTML content`, and query elements by `tag names`, `classes`, and `IDs`. This simplifies working with HTML, allowing users to extract desired data efficiently.

### Technologies
```py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
```

### Run
```
pip install uvicorn
uvicorn app:app --reload
```

```
Visit /docs route for Swagger documentation.
```

<h3 align="center">
  Made & open-sourced with ❤️ by <a href="https://www.kartikmehta.xyz">kartikmehta8</a>
</h3>
