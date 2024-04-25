from coordinates import Coordinates
from entity import Entity, EntityType
from hole import Hole


class Orb(Entity):
    DEFAULT_IMAGE = '...'
    
    def __init__(self, id: int, position: Coordinates | None = None, image: str|None = None) -> None:
        '''Orbs: orbs are sphere entities which would fill the holes inside the field.
            Params note: Not specifying coordinates will make it randomise its position, not specifying image will make the app use default image.'''
        super().__init__(name="Orb", id=id, image=image or Orb.DEFAULT_IMAGE, entityType=EntityType.ORB, position=position)
        
        self.hole: Hole|None = None  # The hole which this orb is dropped to. If orb.hole is None it means this orb is still outside in the field