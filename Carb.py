from Calories import Calories


class Carb:

    def __init__(self):
        self.y1 = 2
        self.y2 = 4

    def calc_carb(self, weight, x):
        """
        This method to calculate the needed carb per person weight
        :param weight: the person weight
        :param x: the person calories according to his activity
        :return: the needed carb per weight
        """
        obj = Calories()
        current_calories = obj.calc_calories(weight, x)
        carb = current_calories / self.y1 / self.y2
        return carb
