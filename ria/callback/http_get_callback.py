import json

from ria._typing import HttpGetRequestRet
from requests import get


def http_get_callback(url: str) -> HttpGetRequestRet:
    response = get(url)
    if response.status_code == 200:
        return {"status": response.status_code, "data": json.loads(response.text)}
    else:
        if response.status_code == 404:
            response_google = get("http://www.google.com")
            if response_google.status_code == 404:
                raise Exception(
                    "No es posible conectar con la API. Compruebe que está conectado a internet."
                )
            raise Exception(
                "No es posible conectar con la API. Compruebe que los datos introducidos estén bien."
            )
        else:
            raise Exception(response.text)
