from unittest import TestCase

from battlefield import Battlefield
from cruiser import Cruiser
from exceptions import OutOfRangeError
from frigate import Frigate


class TestBattleField(TestCase):

    def test_add_vessel_success(self):
        # Arrange
        battlefield = Battlefield(0, 100, 0, 100, -1, 1)

        # Act
        battlefield.add_vessel(Frigate(50, 50, 0))

        # Assert
        self.assertEqual(1, len(battlefield.get_vessels()))

    def test_add_vessel_x_out_of_range(self):
        # Arrange
        battlefield = Battlefield(0, 100, 0, 100, -1, 1)

        # Act
        with self.assertRaises(OutOfRangeError) as error_context:
            battlefield.add_vessel(Frigate(101, 50, 0))

        # Assert
        self.assertEqual(
            "Les coordonnées du vaisseau sont en dehors de l'espace réservé !",
            str(error_context.exception))

    def test_add_vessel_position_not_empty(self):
        # Arrange
        battlefield = Battlefield(0, 100, 0, 100, -1, 1)

        # Act
        battlefield.add_vessel(Cruiser(50, 50, 0))
        with self.assertRaises(ValueError) as error_context:
            battlefield.add_vessel(Frigate(50, 50, 0))

        # Assert
        self.assertEqual(
            "Il y a déjà un vaisseau positionné ici !",
            str(error_context.exception))

    def test_add_vessel_when_max_power_reached(self):
        # Arrange
        battlefield = Battlefield(0, 100, 0, 100, -1, 1, 2)

        # Act
        with self.assertRaises(ValueError) as error_context:
            battlefield.add_vessel(Frigate(50, 50, 0))

        # Assert
        self.assertEqual(
            "La puissance dépasse la maximum autorisé 2 !",
            str(error_context.exception))

    def test_fired_at_fail(self):
        # Arrange
        battlefield = Battlefield(0, 100, 0, 100, -1, 1)
        battlefield.add_vessel(Frigate(50, 50, 0))

        # Act
        touched = battlefield.fired_at(1, 1, 0)

        # Assert
        self.assertFalse(touched)

    def test_fired_at_success(self):
        # Arrange
        battlefield = Battlefield(0, 100, 0, 100, -1, 1)
        battlefield.add_vessel(Frigate(50, 50, 0))

        # Act
        touched = battlefield.fired_at(50, 50, 0)

        # Assert
        self.assertTrue(touched)
