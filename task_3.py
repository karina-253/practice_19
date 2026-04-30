class NotSleeping:
    """
    This class represents a person who cannot
    fall asleep and is counting sheep.

    Attributes:
         name (str): The name of the person who cannot sleep.
         count_sheeps (int): The current number of sheep counted.
    """

    def __init__(self, name: str, count_sheeps: int=0) -> None:
        """
        Initializes a new NotSleeping object.

        Args:
            name (str): The name of the person
            count_sheeps (int): The initial number of sheep. The default value is 0.
        """

        self.name = name
        self.count_sheeps = count_sheeps

    def add_sheep(self) -> None:
        """
        Increases the sheep counter by 1.
        """

        self.count_sheeps += 1

    def lost(self) -> None:
        """
        It resets the sheep counter to 0, simulating a person losing count.
        """

        self.count_sheeps = 0

    def get_count_sheeps(self) -> int:
        """
        Returns the current number of counted sheep.

        Returns:
            int: The number of counted sheep.
        """

        return self.count_sheeps


human = NotSleeping('Мистер Смит')
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
print(human.name, 'насчитал', human.count_sheeps, 'овец')
human.add_sheep()
human.lost()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
human.add_sheep()
print(human.name, 'насчитал', human.get_count_sheeps(), 'овец')
