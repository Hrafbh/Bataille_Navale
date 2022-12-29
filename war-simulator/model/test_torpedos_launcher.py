from unittest import TestCase

from exceptions import OutOfRangeError, NoAmmunitionError
from torpedos_launcher import TorpedoLauncher


class TestTorpedoLauncher(TestCase):
    def test_fire_at_success(self):
        # Arrange
        torpedo_launcher = TorpedoLauncher()

        # Act
        torpedo_launcher.fire_at(3, 3, -1)

        # Assert
        self.assertEqual(14, torpedo_launcher.get_ammunitions())

    def test_fire_at_raise_error_when_z_gt_zero(self):
        # Arrange
        torpedo_launcher = TorpedoLauncher()

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            torpedo_launcher.fire_at(3, 3, 1)

        # Assert
        self.assertEqual("Impossible d'atteindre la cible ! z doit être <= 0",
                         str(error_context.exception))
        self.assertEqual(14, torpedo_launcher.get_ammunitions())

    def test_fire_at_raise_error_when_ammunitions_eq_zero(self):
        # Arrange
        torpedo_launcher = TorpedoLauncher()

        # Act
        with self.assertRaises(NoAmmunitionError) as error_context:
            for _ in range(16):
                torpedo_launcher.fire_at(3, 3, 0)

        # Assert
        self.assertEqual("Vous n'avez plus de munitions !",
                         str(error_context.exception))
