class Game:
    """
    A class representing a basketball game, tracking the score of two teams.
    """
    def __init__(self, commands_info: dict) -> None:
        """
        Initializes a new Game object.
        Creates a basketball game between two teams with initial scores set to 0.

        Args:
            commands_info (dict): A dictionary containing information about the teams.
            It must contain the keys 'command1' and 'command2' with the team
            names as values.
        """
        self.command1_name = commands_info['command1']
        self.command2_name = commands_info['command2']
        self.score_command1 = 0
        self.score_command2 = 0

    def ball_thrown(self, command: int, points: int) -> None:
        """
        Adds the number of points to the given team.

        Args:
            command (int): The team number to add points to.
            points (int): The number of points to add
        """
        if command == 1:
            self.score_command1 += points
        elif command ==2:
            self.score_command2 += points

    def get_score(self) -> tuple:
        """
        Returns the current score of the game.

        Returns:
            tuple: A tuple containing the score of the first team and
            the score of the second team
        """
        return (self.score_command1, self.score_command2)

    def get_winner(self) -> str:
        """
        Determines the winner of the game based on the current score.
        Returns:
            str: The name of the winning team if one team has more points,
                or the string 'Ничья' if the scores are equal.
        """
        if self.score_command1 > self.score_command2:
            return self.command1_name
        elif self.score_command2 > self.score_command1:
            return self.command2_name
        else:
            return "Ничья"

game_one = Game({'command1' : 'Юта Джаз', 'command2' : 'Майами Хит'})
game_one.ball_thrown(1, 2)
game_one.ball_thrown(1, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 1)
print(game_one.get_score())
game_one.ball_thrown(2, 3)
game_one.ball_thrown(2, 2)
game_one.ball_thrown(1, 2)
print(game_one.get_score())
print(game_one.get_winner())
