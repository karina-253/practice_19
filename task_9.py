class StrandsDNA:
    """
    The class that stores DNA chains.
    Attributes:
        all_strands: A list of all DNA strands.
    """
    def __init__(self) -> None:
        """
        Initializes an object with an empty list of chains.
        """
        self.all_strands = []

    def add_strands(self, strands: str) -> None:
        """
        Adds new DNA strands from a string

        Args:
            strands (str): A string with DNA strands separated by spaces.
        """
        for strand in strands.split():
            self.all_strands.append(strand)

    def get_max_strands(self) -> str:
        """
        Returns a string containing chains of maximum length

        Returns:
               str: A string with unique chains of maximum length,
               sorted in alphabetical order.
               otherwise, it returns an empty string.
        """
        if not self.all_strands:
            return ""

        max_len = max(len(strand) for strand in self.all_strands)
        result = sorted(set(strand for strand in self.all_strands if len(strand) == max_len))
        return " ".join(result)

    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        Returns:
            str: All DNA chains separated by spaces.
        """
        return " ".join(self.all_strands)

    def __repr__(self) -> str:
        """
        Returns a string that allows you to recreate the object.
        """
        return f"StrandsDNA('{' '.join(self.all_strands)}')"


covid_19 = StrandsDNA()
covid_19.add_strands('GAAT ACCGTT TTGAC TGGGAC')
print(covid_19)
covid_19.add_strands('ACCT AGGCT TGGGAC')
covid_19.add_strands('CATTTT TAATTC')
print(covid_19)
print(covid_19.get_max_strands())
