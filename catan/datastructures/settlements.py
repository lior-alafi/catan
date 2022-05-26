from enum import Enum

from catan.datastructures.node_abc import Node


class SettlementType(Enum):
    VILLAGE = 0
    CITY = 1
    CASTLE = 2

class Settlement(Node):
    NODE_TYPE = "SETTLEMENT"
    
    def __init__(self, settlement_type = SettlementType.VILLAGE,isEdge = False) -> None:
        super().__init__()
        self.roads = []
        self.port = None
        self.resources = []
        self.player = None
        self.isEdge = isEdge
        self.node_type = settlement_type

    def add_road(self,road):
        if len(self.roads) < 2 and self.isEdge:
            self.roads.append(road)

    def upgrade(self):
        if SettlementType.VILLAGE == self.get_type():
            self.node_type = SettlementType.CITY
        elif self.get_type() == SettlementType.CITY:
            self.node_type = SettlementType.CASTLE

    def assign_player(self,player):
        if self.player is not None:
            self.player = player

    def get_player(self):
        return self.player
        
        

