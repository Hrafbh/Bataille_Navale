from dao.game_dao import GameDao
from game import Game
from battlefield import Battlefield
from player import Player
from game_dao import VesselEntity
from game_dao import GameDao

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
        self.game_dao.find_game(game_id).add_player(Player(player_name))
        return print(str(player_name)+" added to "+str(game_id))
        
    def get_game(self, game_id: int) -> Game:
        self.game_dao.find_game(game_id).get_id
        self.game_dao.find_game(game_id).get_players
        return self.game_dao.find_game(game_id)


    def add_vessel(self, game_id: int, player_name: str, vessel_type: str,x: int, y: int, z: int) -> bool:
        add = False
        vesselentity = VesselEntity()
        vesselentity.coord_x = x
        vesselentity.coord_y = y
        vesselentity.coord_z = z
        vesselentity.type = vessel_type
        vessel = self.game_dao.map_to_vessel(vesselentity)
        if Player(player_name,) in self.game_dao.find_game(game_id).players:
            add = True
            Player(player_name,).battle_field.add_vessel(vessel)
            return add
        else :
            return add
            

               
    def shoot_at(self, game_id: int, shooter_name: str, vessel_id: int, x: int,y: int, z: int) -> bool:
        shoot = False
        vesselentity = VesselEntity()
        vesselentity.id = vessel_id
        vessel = self.game_dao.map_to_vessel(vesselentity)
        player = Player(shooter_name,)
        if  player in self.game_dao.find_game(game_id).players:
            if vessel in player.battle_field.vessels :
                shoot = True
                vessel.fire_at(x,y,z) 
                return shoot
            else :
                return shoot
        else :
            return shoot
 

                
    def get_game_status(self, game_id: int, shooter_name: str) -> str:
        player = Player(shooter_name,)
        if player in self.game_dao.find_game(game_id).players:
                Sp=0
                Sa=0
                adversaire = Player()
                for p in self.game_dao.find_game(game_id).players:
                    if p == player:
                        pass
                    else :
                        p = adversaire

                for vessel in player.battle_field.vessels:
                    Sp = Sp + vessel.hits_to_be_destroyed 
                for vessel in adversaire.battle_field.vessels:
                    Sa = Sa + vessel.hits_to_be_destroyed    

                if Sp == 0 or player.battle_field.get_power == 0:
                    return print("PERDU")
                elif (Sp != 0 or player.battle_field.get_power != 0) and (Sa != 0 or adversaire.battle_field.get_power !=0) :
                    return print("ENCOURS")
                elif  Sa == 0 or adversaire.battle_field.get_power ==0:
                    return print("GAGNE")
        else:
            return print(str(shooter_name)+" is not in "+str(game_id))                


