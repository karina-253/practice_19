class Dog:
    """
    This class represents a dog with a name and the
    ability to bark.

    Attributes:
        name (str): The name of the dog.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a dog with the given name

        Args:
            name (str): The name of the dog.
        """
        self.name = name

    def __str__(self) -> str:
        """
        Returns a string representation of the Dog object.

        Returns:
            str: The dog's name.
        """
        return self.name

    def say(self) -> None:
        """
        Make the dog bark.

        Prints the barking "Гав!" to the console.
        """
        print("Гав!")
        

small_dog = Dog('Снупи')
print(small_dog)
small_dog.say()
print('Кличка собаки', small_dog.name)
