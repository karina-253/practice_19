class TrafficLight:
    """
    A class representing a traffic light.
    Traffic light signals change in the following order:
    green, yellow, red, yellow, green, yellow etc.

    Attributes:
        permissible_values (list): List of valid traffic light signals.
        current_signal (str): Current traffic light signal.
    """
    permissible_values = ["зеленый", "желтый", "красный", "желтый"]

    def __init__(self) -> None:
        """
        Initializes an instance of the traffic light.
        """
        self.current_signal = 'зеленый'
        self.signal_ind = 0

    def next_signal(self) -> None:
        """
        Changes the current traffic light signal to the next one
        """
        self.signal_ind += 1
        self.current_signal = self.permissible_values[self.signal_ind % len(self.permissible_values)]


seven_roads = TrafficLight()
print(seven_roads.current_signal)
for _ in range(5):
    seven_roads.next_signal()
print(seven_roads.current_signal)
