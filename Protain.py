class Protain:
    def __init__(self):
        self.constant_1 = 1.5
        self.constant_2 = 0.8

    def calc_protain(self, weight, y):
        """
        This method to calculate the needed protain per person weight
        :param weight: the person weight
        :param y: the needed protain according to the persons goal
        :return: the needed protain per weight
        """
        protain_you_need = 0
        if y == 1:
            protain_you_need += (weight * self.constant_1)
        elif y == 2:
            protain_you_need += (weight * self.constant_2)

        return protain_you_need
