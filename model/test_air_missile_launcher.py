from unittest import TestCase

from air_missile_launcher import AirMissileLauncher
from exceptions import OutOfRangeError, NoAmmunitionError


class TestAirMissileLauncher(TestCase):
    def test_fire_at_success(self):
        # Arrange
        air_missile_launcher = AirMissileLauncher()

        # Act
        air_missile_launcher.fire_at(3, 3, 1)

        # Assert
        self.assertEqual(49, air_missile_launcher.get_ammunitions())

    def test_fire_at_raise_error_when_z_eq_zero(self):
        # Arrange
        air_missile_launcher = AirMissileLauncher()

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            air_missile_launcher.fire_at(3, 3, 0)

        # Assert
        self.assertEqual("Impossible d'atteindre la cible ! z doit être > 0",
                         str(error_context.exception))
        self.assertEqual(49, air_missile_launcher.get_ammunitions())

    def test_fire_at_raise_error_when_ammunitions_eq_zero(self):
        # Arrange
        air_missile_launcher = AirMissileLauncher()

        # Act
        with self.assertRaises(NoAmmunitionError) as error_context:
            for _ in range(51):
                air_missile_launcher.fire_at(3, 3, 1)

        # Assert
        self.assertEqual("Vous n'avez plus de munitions !",
                         str(error_context.exception))
