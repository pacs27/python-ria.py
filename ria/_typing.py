from typing import Any, TypedDict


class HttpGetRequestRet(TypedDict):
    status: int
    data: Any


class ProvinciaInfo(TypedDict):
    id: int
    nombre: str


class EstacionInfo(TypedDict):
    provincia: ProvinciaInfo
    codigoEstacion: str
    nombre: str
    bajoplastico: bool
    activa: bool
    visible: bool
    longitud: str
    latitud: str
    altitud: int
    xutm: float
    yutm: float
    huso: int


class DatosDia(TypedDict):
    bateria: int
    dia: int
    dirViento: float
    dirVientoVelMax: float
    et0: float
    fecha: str
    fechaUtlMod: str
    horMinHumMax: str
    horMinHumMin: str
    horMinTempMax: str
    horMinTempMin: str
    horMinVelMax: str
    humedadMax: float
    humedadMedia: float
    humedadMin: float
    precipitacion: float
    radiacion: float
    tempMax: float
    tempMedia: float
    tempMin: float
    velViento: float
    velVientoMax: float

class DatosMes(TypedDict):
    anyo: int
    mes: int
    numDias: int
    tempMedia: float
    tempMax: float
    diaHorMinTempMax: str
    tempMin: float
    diaHorMinTempMin: str
    humedadMedia: float
    humedadMax: float
    diahorMinHumMax: str
    humedadMin: float
    diahorMinHumMin: str
    velViento: float
    dirViento: float
    velVientoMax: float
    diahorMinVelMax: str
    dirVientoVelMax: float
    precipitacion: float
    radiacion: float
    bateria: float
    fechaUtlMod: str