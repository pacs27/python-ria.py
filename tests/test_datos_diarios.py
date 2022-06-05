from datetime import date
import unittest
from ria import RIA


class TestDatosDias(unittest.TestCase):
    ria_stations = RIA()

    def test_datos_dia(self):

        dia = self.ria_stations.obtener_datos_dia(
            provincia_id=14, estacion_id="2", fecha=date(2021, 10, 10), lg_et0=True
        )

        dia_temMax_returned = dia["tempMax"]
        dia_temMax_expected = 30.46

        self.assertEqual(dia_temMax_returned, dia_temMax_expected)

    def test_datos_diarios_periodo(self):
        datos_diarios = self.ria_stations.obtener_datos_diarios_periodo(
            provincia_id=14,
            estacion_id="2",
            fecha_inicio=date(2021, 10, 10),
            fecha_fin=date(2021, 11, 10),
            lg_et0=True,
        )

        num_days_returned = len(datos_diarios)
        num_days_expected = 32

        self.assertGreaterEqual(num_days_expected, num_days_returned)

    def test_datos_diarios_periodo_con_et0(self):
        datos_diarios = self.ria_stations.obtener_datos_diarios_periodo_con_et0(
            provincia_id=14,
            estacion_id="2",
            fecha_inicio=date(2021, 10, 10),
            fecha_fin=date(2021, 11, 10),
        )

        num_days_returned = len(datos_diarios)
        num_days_expected = 32

        self.assertGreaterEqual(num_days_expected, num_days_returned)

    def test_exception(self):

        with self.assertRaises(Exception):
            self.ria_stations.obtener_datos_diarios_periodo(
                provincia_id=14,
                estacion_id="6",
                fecha_inicio="2021-1-1",
                fecha_fin="2021-12-31",
                lg_et0=True,
            )


if __name__ == "__main__":
    unittest.main()
