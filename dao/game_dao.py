import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:////tmp/tdlog.db', echo=True, future=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class GameEntity(Base):
     __tablename__ = 'game'
     id = Column(Integer, primary_key=True)
     players = relationship("PlayerEntity", back_populates="game",
                            cascade="all, delete-orphan")


class PlayerEntity(Base):
     __tablename__ = 'player'
     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False)
     game_id = Column(Integer, ForeignKey("game.id"), nullable=False) 
     game = relationship("GameEntity", back_populates="player")
     battle_field = relationship("BattlefieldEntity",back_populates="player",uselist=False, cascade="all, delete-orphan")

class BattlefieldEntity(Base):
    __tablename__ = 'battlefield'
    id = Column(Integer, primary_key=True)
    min_x = Column(Integer, nullable=True)
    min_y = Column(Integer, nullable=True)
    min_z = Column(Integer, nullable=True)
    max_x = Column(Integer, nullable=True)
    max_y = Column(Integer, nullable=True)
    max_z = Column(Integer, nullable=True)
    max_power = Column(Integer, nullable=True)
    player_id = Column(Integer, ForeignKey("player.id"), nullable=False)
    player = relationship("PlayerEntity", back_populates="battlefield")
    vessel = relationship("VesselEntity", back_populates="battlefield",uselist=False,cascade="all, delete-orphan")
     


class VesselEntity(Base):
     __tablename__ = 'vessel'
     id = Column(Integer, primary_key=True)
     coord_x=Column(Integer, nullable=True)
     coord_y=Column(Integer, nullable=True)
     coord_z=Column(Integer, nullable=True)
     hits_to_be_destroyed=Column(Integer, nullable=True)
     type=Column(String, nullable=True)
     battle_field_id=Column(Integer, ForeignKey("battlefield.id"),nullable=False)
     battlefield = relationship("BattlefieldEntity", back_populates="vessel")
     weapon = relationship("WeaponEntity" , back_populates="vessel",uselist=False,cascade="all, delete-orphan")
     



class WeaponEntity(Base):
     __tablename__='weapon'
     id = Column(Integer,primary_key=True )
     ammunitions = Column(Integer, nullable=True)
     range = Column(Integer, nullable=True)
     type = Column(String,nullable=True)
     vessel_id = Column(Integer, ForeignKey("vessel.id"),nullable=False)
     vessel = relationship("VesselEntity",back_populates="weapon" )





class GameDao:
     def __init__(self):
        Base.metadata.create_all()
        self.db_session = Session()

     def create_game(self, game: Game) -> int:
        game_entity = map_to_game_entity(game)
        self.db_session.add(game_entity)
        self.db_session.commit()
        return game_entity.id

     def find_game(self, game_id: int) -> Game:
         stmt = select(GameEntity).where(GameEntity.id == game_id)
         game_entity = self.db_session.scalars(stmt).one()
         return map_to_game(game_entity)
     
     def create_player(self, player: Player) ->int:
          player_entity = map_to_player_entity(player)
          self.db_session.add(player_entity)
          self.db_session.commit()
          return player_entity.id

     def create_vessel(self, vessel: Vessel) ->int:
          vessel_entity = map_to_vessel_entity(vessel)
          self.db_session.add(vessel_entity)
          self.db_session.commit()
          return vessel_entity.id

     def  map_to_game_entity(game):
          # à implementer
          pass
     def  map_to_game(game_entity):
          # à implementer
          pass
     def map_to_player_entity(player):
          # à implementer
          pass
     def map_to_vessel_entity(vessel):
          # à implementer
          pass



     




    


