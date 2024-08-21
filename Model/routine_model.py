import openai

class RoutineModel:
    def __init__(self, tools, location, exercise_type, api_key):
        self.tools = tools
        self.location = location
        self.exercise_type = exercise_type
        self.api_key = api_key

    def generate_routine(self):
        openai.api_key = self.api_key
        
        # Crear una solicitud a la API de OpenAI
        response = openai.Completion.create(
            engine="davinci",  
            prompt=f"Create an exercise routine with the following tools: {self.tools}, location: {self.location}, and exercise type: {self.exercise_type}.",
            max_tokens=100
        )
        
        return response.choices[0].text.strip()
