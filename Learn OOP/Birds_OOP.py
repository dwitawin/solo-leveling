# create Birdy Class
class Bird:
    def __init__(self, name, color, size, food):
        self.name = name
        self.color = color
        self.size = size
        self.food = food

    def purint(self):
        print(f"This bird is called {self.name}. The color is {self.color}, and it is {self.size} in size. Also {self.name} eats {self.food} for survival.")

#test
if __name__ == "__main__":
    bird1 = Bird("Owl", "gray", "medium", "small animal")
    bird2 = Bird("Raven", "black", "small", "seeds")

    bird1.purint()
    bird2.purint()