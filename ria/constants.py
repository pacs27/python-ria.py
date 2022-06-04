BASE_URL = "http://www.juntadeandalucia.es/agriculturaypesca/ifapa/riaws"

DIARIO_URL = BASE_URL + "/datosdiarios"

MENSUAL_URL = BASE_URL + "/datosmensuales"

PROVINCIA_URL = BASE_URL + "/provincias"

ESTACIONES_URL = BASE_URL + "/estaciones"


def DATO_DIARIO_DIA_URL(
    codigo_provincia: int, codigo_estacion: str, fecha: str, lg_et0: bool
) -> str:
    """Devuelve los datos diarios de una estación para un día concreto


    Args:
        codigo_provincia (int): Identificador del código de provincia al que pertenece la estación
        codigo_estacion (str): Identificador del código de estación
        fecha (str): Fecha para la que se desea consultar los datos registrados
        lg_et0 (bool): Booleano que indica si se desea el cálculo de la Et0 mediante el algoritmo de Penman Monteith o no

    Returns:
        str: API URL
    """

    return f"{DIARIO_URL}/{codigo_provincia}/{codigo_estacion}/{fecha}/{lg_et0}"


def DATO_DIARIO_INTERVALO_URL(
    codigo_provincia: int, codigo_estacion: str, fecha_inicio: str, fecha_fin: str, lg_et0: bool
) -> str:
    """Devuelve los datos diarios de una estación para un intervalo concreto

    Args:
        codigo_provincia (int): Identificador del código de provincia al que pertenece la estación
        codigo_estacion (str): Identificador del código de estación
        fecha_inicio (str): Fecha de inicio para la que se desea consultar los datos registrados
        fecha_fin(str): Fecha final para la que se desea consultar los datos registrados
        lg_et0 (bool): Booleano que indica si se desea el cálculo de la Et0 mediante el algoritmo de Penman Monteith o no

    Returns:
        str: API URL
    """
    return f"{DIARIO_URL}/{codigo_provincia}/{codigo_estacion}/{fecha_inicio}/{fecha_fin}/{lg_et0}"


def DATO_DIARIO_INTERVALO_ET0_URL(
    codigo_provincia: int, codigo_estacion: str, fecha_inicio: str, fecha_fin: str
) -> str:
    """Devuelve los datos diarios de una estación para un intervalo concreto con la Et0 calculada
        o nula en caso de no poder calcularla por falta de datos

    Args:
        codigo_provincia (int): Identificador del código de provincia al que pertenece la estación
        codigo_estacion (str): Identificador del código de estación
        fecha_inicio (str): Fecha de inicio para la que se desea consultar los datos registrados
        fecha_fin(str): Fecha final para la que se desea consultar los datos registrados

    Returns:
        str: API URL
    """

    return (
        f"{DIARIO_URL}/forceEt0/{codigo_provincia}/{codigo_estacion}/{fecha_inicio}/{fecha_fin}"
    )


def DATA_MENSUAL_MES_CONCRETO_URL(
    codigo_provincia: int, codigo_estacion: str, anyo: int, mes: int
) -> str:
    """Devuelve los datos mensuales de una estación para un mes concreto

    Args:
        codigo_provincia (int): Identificador del código de provincia al que pertenece la estación
        codigo_estacion (str): Identificador del código de estación
        anyo (int): Año para el que se desea consultar los datos registrados
        mes (int): Mes para el que se desea consultar los datos registrados

    Returns:
        str: API URL
    """

    return f"{MENSUAL_URL}/{codigo_provincia}/{codigo_estacion}/{anyo}/{mes}"


def DATA_MENSUAL_INTERVALO_URL(
    codigo_provincia: int, codigo_estacion: str, anyo: int, mes_inicio: int, mes_fin: int
) -> str:
    """Devuelve los datos mensuales de una estación para un mes concreto

    Args:
        codigo_provincia (int): Identificador del código de provincia al que pertenece la estación
        codigo_estacion (str): Identificador del código de estación
        anyo (int): Año para el que se desea consultar los datos registrados
        mes_inicio (int): Mes de inicio para el que se desea consultar los datos registrados
        mes_fin (int): Mes de fin para el que se desea consultar los datos registrados
    Returns:
        str: API URL
    """

    return f"{MENSUAL_URL}/{codigo_provincia}/{codigo_estacion}/{anyo}/{mes_inicio}/{mes_fin}"


def OBTENER_TODAS_LAS_ESTACIONES_URL() -> str:
    """Devuelve el listado de estaciones completo

    Returns:
        str: API URL
    """
    return ESTACIONES_URL


def OBTENER_TODAS_LAS_ESTACIONES_EN_UNA_PROVINCIA_URL(codigo_provincia: int) -> str:
    """Devuelve el listado de estaciones para una provincia en concreto

    Args:
        codigo_provincia (int): Identificador del código de provincia para buscar las estaciones

    Returns:
        str: API URL
    """
    return f"{ESTACIONES_URL}/{codigo_provincia}"


def OBTENER_INFORMACION_DE_ESTACION_URL(codigo_provincia: int, codigo_estacion: str) -> str:
    """Devuelve informacion de la estación solicitada

    Args:
        codigo_provincia (int): Identificador del código de provincia al que pertenece la estación
        codigo_estacion (str): Identificador del código de estación

    Returns:
        str: API URL
    """
    return f"{ESTACIONES_URL}/{codigo_provincia}/{codigo_estacion}"


def OBTENER_TODAS_LAS_PROVINCIAS_URL() -> str:
    """Devuelve el listado de provincias completo

    Returns:
        str: API URL
    """
    return PROVINCIA_URL


def OBTENER_INFORMACION_DE_UNA_PROVINCIA_URL(codigo_provincia: int) -> str:
    """evuelve una provincia en concreto

    Args:
        codigo_provincia (int): Identificador del código de provincia para buscar las estaciones

    Returns:
        str: API URL
    """
    return f"{PROVINCIA_URL}/{codigo_provincia}"
