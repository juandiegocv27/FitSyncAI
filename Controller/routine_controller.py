from routine_model import RoutineModel

class RoutineController:
    def __init__(self, tools, location, exercise_type, api_key):
        self.model = RoutineModel(tools, location, exercise_type, api_key)

    def create_routine(self):

        return self.model.generate_routine()
