from unittest import TestCase

from exceptions import NoAmmunitionError, OutOfRangeError
from surface_missile_launcher import SurfaceMissileLauncher


class TestSurfaceMissileLauncher(TestCase):
    def test_fire_at_success(self):
        # Arrange
        surface_missile_launcher = SurfaceMissileLauncher()

        # Act
        surface_missile_launcher.fire_at(3, 3, 0)

        # Assert
        self.assertEqual(39, surface_missile_launcher.get_ammunitions())

    def test_fire_at_raise_error_when_z_gt_zero(self):
        # Arrange
        surface_missile_launcher = SurfaceMissileLauncher()

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            surface_missile_launcher.fire_at(3, 3, 1)

        # Assert
        self.assertEqual("Impossible d'atteindre la cible ! z doit être = 0",
                         str(error_context.exception))
        self.assertEqual(39, surface_missile_launcher.get_ammunitions())

    def test_fire_at_raise_error_when_ammunitions_eq_zero(self):
        # Arrange
        surface_missile_launcher = SurfaceMissileLauncher()

        # Act
        with self.assertRaises(NoAmmunitionError) as error_context:
            for _ in range(41):
                surface_missile_launcher.fire_at(3, 3, 0)

        # Assert
        self.assertEqual("Vous n'avez plus de munitions !",
                         str(error_context.exception))
