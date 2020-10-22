class Water:
    def __init__(self):
        self.pound = 0.4536
        self.constant_2 = 50

    def calc_water(self, weight):
        """
        This method to calculate the needed water per person weight
        :param weight: the person weight
        :return: the needed water per weight
        """

        water_you_need = weight / self.pound / self.constant_2
        return water_you_need

