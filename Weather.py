import matplotlib.pyplot as plt


class Weather:
    """
    Class to save and update the temperatures of a weather object
    === Attributes ===
    times:
        The list of all the times the temperature is recorded for.
    temperatures:
        The list of temperatures that are being recorded.
    name:
        The name of the place the temperature is being recorded of.
    msgId:
        The message Id of the current plot
        This is used to access the previous message and remove it when updating the plot
    """
    times: list[str]
    temperatures: list[float]
    name: str
    nsgId: int

    def __init__(self, times: list[str], temperatures: list[float], name: str):
        """Initializes a new weather object with times, temperatures and name.
           Sets default msgId
           Creates the plot
        """
        self.times = times
        self.temperatures = temperatures
        self.name = name

        # By default its 0 but after the message is sent its set to the id
        self.msgId = 0

        self.create_plot()

    def create_plot(self):
        """
        Creates and saves an image of the plot
        The image is then sent to the channel through main
        """

        # Creates the plot
        line = plt.plot(self.times, self.temperatures)
        plt.title(f"Temperature in {self.name}")
        plt.ylabel("Temperature (C)")
        plt.xlabel("Time")

        # Saves the plot
        plt.savefig(f"{self.name}.png")

        # Removes the line from the plot so that when the plot is updated one 1 line is shown
        line = line.pop(0)
        line.remove()

    def update_plot(self, time: str, temperature: float):
        """
        Updates the plot by adding in a new time and temperature
        """
        self.times.append(time)
        self.temperatures.append(temperature)

        # Creates a new plot for the updated temperature
        self.create_plot()

    def set_msg_id(self, new_id):
        """
        Sets the message id to the new message id
        """
        self.msgId = new_id
