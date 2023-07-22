import json

from ria._typing import HttpGetRequestRet
from requests import request


def http_get_callback(url: str) -> HttpGetRequestRet:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    payload = {}
    response = request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return {"status": response.status_code, "data": json.loads(response.text)}
    else:
        if response.status_code == 404:
            response_google = request("GET","http://www.google.com")
            if response_google.status_code == 404:
                raise Exception(
                    "No es posible conectar con la API. Compruebe que está conectado a internet."
                )
            raise Exception(
                "No es posible conectar con la API. Compruebe que los datos introducidos estén bien."
            )
        else:
            raise Exception(response.text)
