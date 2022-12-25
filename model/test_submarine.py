from unittest import TestCase

from exceptions import OutOfRangeError
from submarine import Submarine


class TestSubmarine(TestCase):
    def test_go_to_success(self):
        # Arrange
        submarine = Submarine(0, 0, 0)

        # Act
        submarine.go_to(1, 1, 0)
        submarine.go_to(1, 1, -1)

        # Assert
        self.assertEqual((1, 1, -1), submarine.get_coordinates())

    def test_go_to_raise_error(self):
        # Arrange
        submarine = Submarine(0, 0, 0)

        # Act
        with self.assertRaises(ValueError) as error_context:
            submarine.go_to(1, 1, 1)

        # Assert
        self.assertEqual("Coordonnées de déplacement invalides !",
                         str(error_context.exception))

    def test_fire_at_success(self):
        # Arrange
        submarine = Submarine(0, 0, 0)

        # Act
        submarine.fire_at(1, 1, 0)

        # Assert
        self.assertEqual(14, submarine.get_weapon().get_ammunitions())

    def test_fire_at_raise_error_when_target_out_of_range(self):
        # Arrange
        submarine = Submarine(0, 0, -1)

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            submarine.fire_at(60, 60, 0)

        # Assert
        self.assertEqual("La cible est hors de portée!",
                         str(error_context.exception))

    def test_fire_at_raise_error_when_z_gt_0(self):
        # Arrange
        submarine = Submarine(0, 0, -1)

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            submarine.fire_at(2, 2, 1)

        # Assert
        self.assertEqual("Impossible d'atteindre la cible ! z doit être <= 0",
                         str(error_context.exception))
