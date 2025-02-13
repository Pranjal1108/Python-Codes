class Animal:
    def __init__(self, speak, walk):
        self.speak = speak
        self.walk = walk

class mammals(Animal):
    def __init__(self, speak, walk):
        super().__init__(speak , walk)
        
        
class reptiles(Animal):
    def __init__(self, speak, walk):
        super().__init__(speak, walk)
        

lizard = reptiles("mute", "4")
cow = mammals("moo", "4")

print(f" lizard  {lizard.speak} and has {lizard.walk} no. of legs")
print(f"cow say {cow.speak} and has {cow.walk} no. of legs")