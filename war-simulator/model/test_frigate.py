from unittest import TestCase

from exceptions import OutOfRangeError
from frigate import Frigate


class TestFrigate(TestCase):
    def test_go_to_success(self):
        # Arrange
        frigate = Frigate(0, 0, 0)

        # Act
        frigate.go_to(1, 1, 0)

        # Assert
        self.assertEqual((1, 1, 0), frigate.get_coordinates())

    def test_go_to_raise_error(self):
        # Arrange
        frigate = Frigate(0, 0, 0)

        # Act
        with self.assertRaises(ValueError) as error_context:
            frigate.go_to(1, 1, 1)

        # Assert
        self.assertEqual("Coordonnées de déplacement invalides !",
                         str(error_context.exception))

    def test_fire_at_success(self):
        # Arrange
        frigate = Frigate(0, 0, 0)

        # Act
        frigate.fire_at(1, 1, 0)

        # Assert
        self.assertEqual(39, frigate.get_weapon().get_ammunitions())

    def test_fire_at_raise_error_when_target_out_of_range(self):
        # Arrange
        frigate = Frigate(0, 0, 0)

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            frigate.fire_at(60, 60, 1)

        # Assert
        self.assertEqual("La cible est hors de portée!",
                         str(error_context.exception))
