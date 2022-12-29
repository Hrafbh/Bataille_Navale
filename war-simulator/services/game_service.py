from dao.game_dao import GameDao

class GameService:
    def __init__(self):

       self.game_dao = GameDao()
    def create_game(self, player_name: str, min_x: int, max_x: int, min_y: int,
                    max_y: int, min_z: int, max_z: int) -> int:
        game = Game()
        battle_field = Battlefield(min_x, max_x, min_y, max_y, min_z, max_z)
        game.add_player(Player(player_name, battle_field))
        return self.game_dao.create_game(game)
    def join_game(self, game_id: int, player_name: str) -> bool:
        pass
        # à implementer
    def get_game(self, game_id: int) -> Game:
        pass
        # à implementer
    def add_vessel(self, game_id: int, player_name: str, vessel_type: str,
                  x: int, y: int, z: int) -> bool:
        pass
        # à implementer
    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int,
                y: int, z: int) -> bool:
        pass        
        # à implementer
    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        pass