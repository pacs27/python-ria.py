from typing import List


from .constants import (
    OBTENER_TODAS_LAS_PROVINCIAS_URL,
    OBTENER_INFORMACION_DE_UNA_PROVINCIA_URL,
    OBTENER_TODAS_LAS_ESTACIONES_URL,
    OBTENER_TODAS_LAS_ESTACIONES_EN_UNA_PROVINCIA_URL,
    OBTENER_INFORMACION_DE_ESTACION_URL,
    DATO_DIARIO_DIA_URL,
    DATO_DIARIO_INTERVALO_URL,
    DATO_DIARIO_INTERVALO_ET0_URL,
    DATA_MENSUAL_MES_CONCRETO_URL,
    DATA_MENSUAL_INTERVALO_URL,
)

from datetime import date
from ._typing import ProvinciaInfo, EstacionInfo, DatosDia, DatosMes
from .callback.http_get_callback import http_get_callback


class RIA:
    def __init__(self):
        pass

    def listar_todas_las_provincias(self) -> List[ProvinciaInfo]:
        """Devuelve todas las provincias

        Returns:
            List[ProvinciaInfo]:
            ProvinciaInfo = {
                id: int
                nombre: str
            }

        """
        provincias_datos = http_get_callback(url=OBTENER_TODAS_LAS_PROVINCIAS_URL())[
            "data"
        ]

        return provincias_datos

    def obtener_informacion_de_una_provincia(self, provincia_id: int) -> ProvinciaInfo:
        """Devuelve la provincia preguntada

        Args:
            provincia_id (int): Id de la provincia a consultar

        Returns:
            ProvinciaInfo = {
                id: int
                nombre: str
            }
        """
        provincias_datos = http_get_callback(
            url=OBTENER_INFORMACION_DE_UNA_PROVINCIA_URL(codigo_provincia=provincia_id)
        )["data"]

        return provincias_datos

    def listar_todas_las_estaciones(self) -> List[EstacionInfo]:
        """Devuelve todas las estaciones

        Returns:
            List[EstacionInfo]: Array con la informacion de todas las estaciones
            EstacionInfo = {
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
        """
        estaciones_datos = http_get_callback(url=OBTENER_TODAS_LAS_ESTACIONES_URL())[
            "data"
        ]

        return estaciones_datos

    def listar_todas_estaciones_en_una_provincia(
        self, provincia_id: int
    ) -> List[EstacionInfo]:
        """Devuelve todas las estaciones dentro de una provincia

        Args:
            provincia_id (int): Id de la provincia

        Returns:
            List[EstacionInfo]: Array con la informacion de todas las estaciones
            EstacionInfo = {
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
        """
        estaciones_datos = http_get_callback(
            url=OBTENER_TODAS_LAS_ESTACIONES_EN_UNA_PROVINCIA_URL(
                codigo_provincia=provincia_id
            )
        )["data"]

        return estaciones_datos

    def obtener_informacion_de_una_estacion(
        self, provincia_id: int, estacion_id: str
    ) -> EstacionInfo:
        """Devuelve la estacion seleccionada

        Args:
            provincia_id (int): Id de la provincia
            estacion_id (str): Id de la provincia

        Returns:
            EstacionInfo: Informacion de la estacion solicitada

            EstacionInfo = {
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
        """
        estacion_dato = http_get_callback(
            url=OBTENER_INFORMACION_DE_ESTACION_URL(
                codigo_provincia=provincia_id, codigo_estacion=estacion_id
            )
        )["data"]

        return estacion_dato

    def obtener_datos_dia(
        self, provincia_id: int, estacion_id: str, fecha: str, lg_et0: bool = True
    ) -> DatosDia:
        """Obtiene los datos de un dia concreto

        Args:
            provincia_id (int): Id de la provincia
            estacion_id (str): Id de la provincia
            fecha (str): fecha del dia. YYYY-MM-dd
            lg_et0 (bool, optional): Booleano que indica si se desea el cálculo de la Et0
                mediante el algoritmo de Penman Monteith o no. Defaults to True.

        Returns:
            DatosDia: Dato del dia.

            DatosDia = {
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
        """
        dia_datos = http_get_callback(
            url=DATO_DIARIO_DIA_URL(
                codigo_provincia=provincia_id,
                codigo_estacion=estacion_id,
                fecha=fecha,
                lg_et0=lg_et0,
            )
        )["data"]

        return dia_datos

    def obtener_datos_diarios_periodo(
        self,
        provincia_id: int,
        estacion_id: str,
        fecha_inicio: str,
        fecha_fin: str,
        lg_et0: bool = True,
    ) -> List[DatosDia]:
        """Obtiene los datos darios de un periodo de tiempo seleccionado

        Args:
            provincia_id (int): Id de la provincia
            estacion_id (str): Id de la provincia
            fecha_inicio (str): fecha del dia. YYYY-MM-dd
            fecha_fin (str): fecha del dia. YYYY-MM-dd
            lg_et0 (bool, optional): Booleano que indica si se desea el cálculo de la Et0
                mediante el algoritmo de Penman Monteith o no. Defaults to True.

        Returns:
            List[DatosDia]: Array con los datos diarios

            DatosDia = {
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
        """

        datos_diarios_periodo = http_get_callback(
            url=DATO_DIARIO_INTERVALO_URL(
                codigo_provincia=provincia_id,
                codigo_estacion=estacion_id,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                lg_et0=lg_et0,
            )
        )["data"]

        return datos_diarios_periodo

    def obtener_datos_diarios_periodo_con_et0(
        self,
        provincia_id: int,
        estacion_id: str,
        fecha_inicio: str,
        fecha_fin: str,
    ) -> List[DatosDia]:
        """Obtiene los datos darios de un periodo de tiempo seleccionado
            con la Et0 calculada o nula en caso de no poder calcularla por falta de datos

        Args:
            provincia_id (int): Id de la provincia
            estacion_id (str): Id de la provincia
            fecha_inicio (str): fecha del dia. YYYY-MM-dd
            fecha_fin (str): fecha del dia. YYYY-MM-dd

        Returns:
            List[DatosDia]: Array con los datos diarios

            DatosDia = {
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
        """

        datos_diarios_periodo = http_get_callback(
            url=DATO_DIARIO_INTERVALO_ET0_URL(
                codigo_provincia=provincia_id,
                codigo_estacion=estacion_id,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
            )
        )["data"]

        return datos_diarios_periodo

    def obtener_datos_mes(
        self, provincia_id: int, estacion_id: str, anyo: int, mes: int
    ) -> DatosMes:
        """Obtiene los datos de un mes concreto

        Args:
            provincia_id (int): Id de la provincia
            estacion_id (str): Id de la provincia
            anyo (int): año
            mes (int): mes

        Returns:
            DatosMes: Datos del mes.

            DatosMes = {
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
        """
        datos_mes = http_get_callback(
            url=DATA_MENSUAL_MES_CONCRETO_URL(
                codigo_provincia=provincia_id,
                codigo_estacion=estacion_id,
                anyo=anyo,
                mes=mes,
            )
        )["data"]

        return datos_mes

    def obtener_datos_mensuales_periodo(
        self,
        provincia_id: int,
        estacion_id: str,
        anyo: int,
        mes_inicio: int,
        mes_fin: int,
    ) -> List[DatosMes]:
        """Obtiene los datos mensuales de un periodo de tiempo seleccionado

        Args:
            provincia_id (int): Id de la provincia
            estacion_id (str): Id de la provincia
            anyo (int): año
            mes_inicio (int): mes de inicio
            mes_fin (int): mes de fin

        Returns:
            List[DatosMes]: Array con los datos de cada mes

            DatosMes = {
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
        """

        datos_mensuales_periodo = http_get_callback(
            url=DATA_MENSUAL_INTERVALO_URL(
                codigo_provincia=provincia_id,
                codigo_estacion=estacion_id,
                anyo=anyo,
                mes_inicio=mes_inicio,
                mes_fin=mes_fin,
            )
        )["data"]

        return datos_mensuales_periodo
