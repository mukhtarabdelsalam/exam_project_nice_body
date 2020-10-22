from Calories import Calories


class Fat:
    def __init__(self):
        self.x1 = 0.3
        self.x2 = 9

    def calc_fat(self, weight, x):
        """
        This method to calculate the needed fat per person weight
        :param weight: the person weight
        :param x: the person calories according to his activity
        :return: the needed fat per weight
        """
        obj = Calories()
        current_calories = obj.calc_calories(weight, x)
        fat = current_calories * self.x1 / self.x2
        return fat
