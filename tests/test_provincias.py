import unittest
from ria import RIA


class TestProvincias(unittest.TestCase):
    ria_stations = RIA()

    def test_todas_las_provincias(self):

        provincias = self.ria_stations.listar_todas_las_provincias()

        number_provincias_returned = len(provincias)
        number_provincias_expected = 52

        self.assertEqual(number_provincias_expected, number_provincias_returned)

    def test_una_provincia(self):

        provincia = self.ria_stations.obtener_informacion_de_una_provincia(
            provincia_id=14
        )

        provincia_name_returned = provincia["nombre"]
        provincia_name_expected = "Córdoba"

        self.assertEqual(provincia_name_returned, provincia_name_expected)


if __name__ == "__main__":
    unittest.main()
