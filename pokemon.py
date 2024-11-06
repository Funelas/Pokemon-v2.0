
class Pokemon:
    def __init__(self,attributes):
        self.name = attributes[0][0]
        self.element = attributes[0][1] 
        self.health = int(attributes[0][2])  # Convert to int
        self.power = int(attributes[0][3])    # Convert to int
        self.potion = int(attributes[0][4])   # Convert to int
        self.poisons = int(attributes[0][5])  # Convert to int
        self.strength = attributes[0][6]
        self.weakness = attributes[0][7]
        self.used = False
        self.heal_amount = 0
        self.after_health = self.health
        self.powerup_amount = 0
        self.temporary_power = self.power
        self.damage_boost = 0
    def status(self):  
        return [str(self.name), str(self.element), f"{str(self.health)}{f' (+{self.heal_amount})' if self.heal_amount > 0 else ''}", f"{str(self.power)}{f' (+{self.powerup_amount})' if self.powerup_amount > 0 else ''}", self.potion, self.poisons, str(self.strength), str(self.weakness)]
     
    def fight(self):
        if self.used == False:
            self.used = True