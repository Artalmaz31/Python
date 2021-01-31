class Furniture:
    def material(self):
        pass
    def use(self):
        pass

class SeatingFurniture(Furniture):
    def use(self):
        return 'Seat'

class LyingFurniture(Furniture):
    def use(self):
        return 'Lie'

class SupportFurniture(Furniture):
    def use(self):
        return 'Put smth up'

class StorageFurniture(Furniture):
    def use(self):
        return 'Store smth'

class HybridFurniture(Furniture):
    def use(self):
        return 'Seat, Lie'

class Table(SupportFurniture):
    def __init__(self, material1):
        self.material1 = material1

class Chair(SeatingFurniture):
    def __init__(self, material1):
        self.material1 = material1

class Armchair(SeatingFurniture):
    def __init__(self, material1):
        self.material1 = material1

class Bed(LyingFurniture):
    def material(self):
        return 'Wood'

class Sofa(LyingFurniture):
    def material(self):
        return 'Leather'

class ArmchairBed(HybridFurniture):
    def material(self):
        return 'Fabric'

class Stool(SeatingFurniture):
    def __init__(self, material1):
        self.material1 = material1

class Cupboard(StorageFurniture):
    def material(self):
        return 'Glass'

furniture = [Table('Iron'), Chair('Plastic'), Armchair('Fabric'), Bed(), Sofa(), ArmchairBed(), Stool('Wood'), Cupboard()]

for object in furniture:
    if isinstance(object, SeatingFurniture) or isinstance(object, SupportFurniture):
        print(object.material1)
    else:
        print(object.material())
    print(object.use())