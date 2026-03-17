from models import Animal, Dog, Cat

def main():
    animal1 = Animal("Generic", 5, "gray")
    dog1 = Dog("Rex", 3, "black", "Shepherd")
    cat1 = Cat("Mimi", 2, "white", True)

    animals = [animal1, dog1, cat1]

    for animal in animals:
        print(animal)
        print(animal.eat())
        print(animal.speak())
        print()

    print(dog1.fetch())
    print(cat1.climb())


if __name__ == "__main__":
    main()