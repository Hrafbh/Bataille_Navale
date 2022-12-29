from unittest import TestCase

from exceptions import DestroyedError
from vessel import Vessel


class TestVessel(TestCase):
    def test_go_to_success(self):
        # Arrange
        vessel = Vessel(0, 0, 0, 1, None)

        # Act
        vessel.go_to(1, 1, 1)

        # Assert
        self.assertEqual((1, 1, 1), vessel.get_coordinates())

    def test_go_to_raise_error_when_hits_eq_zero(self):
        # Arrange
        vessel = Vessel(0, 0, 0, 0, None)

        # Act
        with self.assertRaises(DestroyedError) as error_context:
            vessel.go_to(1, 1, 1)

        # Assert
        self.assertEqual("Vessel destroyed !",
                         str(error_context.exception))
        self.assertEqual((0, 0, 0), vessel.get_coordinates())

    def test_calculate_distance_to(self):
        # Arrange
        vessel = Vessel(0, 0, 0, 1, None)

        # Act
        distance = vessel.calculate_distance_to(9, 0, 0)

        # Assert
        self.assertEqual(9, distance)
