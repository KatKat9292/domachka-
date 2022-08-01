class Car:
    def __init__(self, color: str, type: str, year: int):
        self.color = color
        self.type = type
        self.year = year

    def star(self):
        print('car started')

    def finish(self):
        print('car turned off')

    def __str__(self) -> str:
        return f"Color: {self.color}, Type: {self.type}, Year: {self.year}"

audi = Car("black", "sedan", "2020")
print(audi)
audi.star(), audi.finish()