
from abc import ABC

class Resource(ABC):
    NODE_TYPE = "RESOURCE"

    def resource_type(self):
        pass
    def __init__(self,resource_value: int) -> None:
        super().__init__()
        self.resource_value = resource_value
        self.settlements_around = []
        self.hasThief = False
        
    def get_value(self):
        return self.resource_value

    def add_settlement(self,settlement):
        if len(self.settlements_around) < 6:
            self.settlements_around.append(settlement)
    
    def get_settlements_around(self):
        return self.settlements_around
    
 

class Desert(Resource):
    def __init__(self, resource_value: int) -> None:
        super().__init__(resource_value)
        self.resource_value = 7
        
    def resource_type(self):
        return None

class Bricks(Resource):
    def __init__(self, resource_value: int) -> None:
        super().__init__(resource_value)

    def resource_type(self):
        return "Bricks"


class Stones(Resource):
    def __init__(self, resource_value: int) -> None:
        super().__init__(resource_value)

    def resource_type(self):
        return "Stones"

class Trees(Resource):
    def __init__(self, resource_value: int) -> None:
        super().__init__(resource_value)

    def resource_type(self):
        return "Trees"

class Meat(Resource):
    def __init__(self, resource_value: int) -> None:
        super().__init__(resource_value)

    def resource_type(self):
        return "Meat"

class Wheat(Resource):
    def __init__(self, resource_value: int) -> None:
        super().__init__(resource_value)

    def resource_type(self):
        return "Wheat"