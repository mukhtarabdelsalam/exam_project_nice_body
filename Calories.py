class Calories:
    def __init__(self):
        self.lightly_active = 1.3
        self.moderately_active = 1.4
        self.very_active = 1.5
        self.day_hours = 24

    def calc_calories(self, weight, x):
        """
        This method to calculate the needed calories per person weight
        :param weight: the person weight
        :param x: the person calories according to his activity
        :return: the needed calories per weight
        """
        calculate_calories = 0

        if x == 1:
            calculate_calories += (weight * self.day_hours * self.lightly_active)

        elif x == 2:
            calculate_calories += (weight * self.day_hours * self.moderately_active)

        elif x == 3:
            calculate_calories += (weight * self.day_hours * self.very_active)

        return calculate_calories


