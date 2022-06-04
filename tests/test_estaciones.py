import unittest
from ria import RIA


class TestEstaciones(unittest.TestCase):
    ria_stations = RIA()

    def test_todas_las_estaciones(self):

        estaciones = self.ria_stations.listar_todas_las_estaciones()

        number_estaciones_returned = len(estaciones)
        number_estaciones_expected = 122

        self.assertGreaterEqual(number_estaciones_returned, number_estaciones_expected)

    def test_estaciones_en_provincia(self):

        estaciones = self.ria_stations.listar_todas_estaciones_en_una_provincia(
            provincia_id=14
        )

        number_estaciones_returned = len(estaciones)

        number_estaciones_expected = 11

        self.assertGreaterEqual(number_estaciones_returned, number_estaciones_expected)

    def test_estacion(self):

        estacion = self.ria_stations.obtener_informacion_de_una_estacion(
            provincia_id=14, estacion_id="2"
        )

        estacion_altitude_returned = estacion["altitud"]

        estacion_altitude_expected = 145

        self.assertEqual(estacion_altitude_returned, estacion_altitude_expected)


if __name__ == "__main__":
    unittest.main()
