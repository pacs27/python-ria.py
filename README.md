# RIA LIBRARY

Python wrapper de la [API de la Red de Información Agroclimática de Andalucía (RIA)](https://www.juntadeandalucia.es/agriculturaypesca/ifapa/riaws/swagger-ui.html#/dato-diario-controller/getDatosDiariosPorIntervaloUsingGET)
 


```python
from ria import RIA

ria = RIA()
estaciones = ria.listar_todas_las_estaciones()

print("Estaciones = ", estaciones)

```

## Installation

```console
$ pip install python-ria
```

# DOCS

## PROVINCIAS

Los métodos públicos disponibles son:

    * listar_todas_las_provincias: Devuelve un array con todas las provincias
    * obtener_informacion_de_una_provincia: Devuelve la provincia preguntada

El formato que tiene la entidad provincia es el siguiente:
```python
{
    id: int
    nombre: str
}
```

## ESTACIONES
Los métodos públicos disponibles son:

    * listar_todas_las_estaciones: Devuelve todas las estaciones
    * listar_todas_estaciones_en_una_provincia: Devuelve un array con todas las estaciones dentro de una provincia
    * obtener_informacion_de_una_estacion: Devuelve informacion de la estación.

El formato que tiene la entidad provincia es el siguiente:
```python
{
    provincia: {
        id: int
        nombre: str
    }
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
}
```
## DATOS DIARIOS
Los métodos públicos disponibles son:

    * obtener_datos_dia: Obtiene los datos de un día concreto
    * obtener_datos_diarios_periodo: Obtiene los datos darios de un periodo de tiempo seleccionado
    * obtener_datos_diarios_periodo_con_et0: Obtiene los datos darios de un periodo de tiempo seleccionado con la Et0 calculada o nula en caso de no poder calcularla por falta de datos

El formato que tienen los datos diarios es el siguiente:
```python
{
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
}
```
## DATOS MENSUALES
Los métodos públicos disponibles son:

    * obtener_datos_mes: Obtiene los datos de un mes concreto
    * obtener_datos_mensuales_periodo: Obtiene los datos mensuales de un periodo de tiempo seleccionado

El formato que tienen los datos mensuales es el siguiente:
```python
{
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
}
'''