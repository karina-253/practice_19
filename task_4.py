class User:
    """
    This class represents the site user with his id, nickname,
    first name, last name, middle name and gender.
    It provides functionality to update user data
    and string representations.
    """

    def __init__(self, id: int, nick_name: str, first_name: str,
                 last_name: str = '', middle_name: str = '', gender: str = '') -> None:
        """
        Initializes a new User object.

        Args:
            id (int): A unique user number
            nick_name (str): user's alias
            first_name (str): User's first name
            last_name (str):User's last name. Defaults to empty string.
            middle_name (str):  User's middle name. Defaults to empty string.
            gender(str): User's gender(male or female). Defaults to empty string.
        """
        self.id =id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, id: int = 0, nick_name: str = '', first_name: str = '',
                 last_name: str = '', middle_name: str = '', gender: str = '') -> None:
        """
        Updates user attributes. If the parameter is empty or equal to 0,
        the corresponding attribute is not changed.

        Args:
            id (int): New user ID.
            nick_name (str): New nickname.
            first_name (str): New first name.
            last_name (str): New last name.
            middle_name (str): New middle name.
            gender (str): New gender.
        """

        if id != 0:
            self.id = id
        if nick_name:
            self.nick_name = nick_name
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if middle_name:
            self.middle_name = middle_name
        if gender:
            self.gender = gender

    def __str__(self) -> str:
        """
        Returns a string representation of the User object.

        Returns:
            str: A formatted string containing user information.
        """
        full_name = []
        if self.last_name:
            full_name.append(self.last_name)
        full_name.append(self.first_name)
        if self.middle_name:
            full_name.append(self.middle_name)

        full = " ".join(full_name)

        gender_str = f" GENDER: {self.gender}" if self.gender else ""

        return f"ID: {self.id} LOGIN: {self.nick_name} NAME: {full}{gender_str}"

    def __repr__(self) -> str:
        """
        Return a string representation of the user for debugging.

        To display a list of users in the desired format, return only nick_name.

        Returns:
            str: User's nickname.
        """

        return self.nick_name


user_1 = User(12, 'alex', 'Алексей')
print(user_1)
user_2 = User(44, 'andru', 'Андрей', 'Петров')
print(user_2)
user_3 = User(25, 'nik', 'Николай', 'Иванов', 'Федорович')
print(user_3)
user_4 = User(61, 'ivan', 'Денис', 'Сидоров', 'Алексеевич', 'M')
print(user_4)
user_5 = User(47, 'ann', 'Анна', gender='F')
print(user_5)
user_4.update(0, '', 'Ваня')
print(user_4)
user_3.update(15, '', 'Никита', '', 'Петрович')
print(user_3)
users = []
users.append(user_2)
users.append(user_4)
users.append(user_5)
users.append(user_1)
users.append(user_3)
print(users)
