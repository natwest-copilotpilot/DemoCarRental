class Criteria:
    def __init__(self):
        self.__cost_criteria = None

    def cost_criteria(self, cost):
        self.__cost_criteria = cost

    def get_cost_criteria(self):
        return self.__cost_criteria

    def __str__(self):
        return "cost_criteria: " + str(self.__cost_criteria) + "\n"