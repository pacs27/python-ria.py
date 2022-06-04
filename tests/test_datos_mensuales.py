from datetime import date
import unittest
from ria import RIA


class TestDatosMensuales(unittest.TestCase):
    ria_stations = RIA()

    def test_datos_mes(self):

        mes = self.ria_stations.obtener_datos_mes(
            provincia_id=14, estacion_id="2", anyo=2021, mes=10
        )

        mes_temMax_returned = mes["tempMax"]
        mes_tempMax_expected = 32

        self.assertEqual(mes_temMax_returned, mes_tempMax_expected)

    def test_datos_mensuales_periodo(self):
        datos_mensuales = self.ria_stations.obtener_datos_mensuales_periodo(
            provincia_id=14,
            estacion_id="2",
            anyo=2021,
            mes_inicio=1,
            mes_fin=5
        )

        num_month_returned = len(datos_mensuales)
        num_month_expected = 5
        
        
        self.assertGreaterEqual(num_month_returned, num_month_expected)
        


if __name__ == "__main__":
    unittest.main()
