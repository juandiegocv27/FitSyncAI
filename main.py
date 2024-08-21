import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from controller.routine_controller import RoutineController

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('routine_view.html')

@app.route('/generate', methods=['POST'])
def generate_routine():
    tools = request.form.get('tools')
    location = request.form.get('location')
    exercise_type = request.form.get('exercise_type')
    
    # Leer la clave API desde las variables de entorno
    api_key = os.getenv('OPENAI_API_KEY')
    
    # Crear una instancia del controlador con la clave API
    controller = RoutineController(tools, location, exercise_type, api_key)
    result = controller.create_routine()
    return jsonify({'routine': result})

if __name__ == '__main__':
    app.run(debug=True)
