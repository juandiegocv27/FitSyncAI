# FitSyncAI


**FitSyncAI or Ejercitandose con IA** is a Python-based application designed to generate personalized exercise plans tailored to each user's fitness goals, skill level, and available time. By leveraging AI-powered recommendation models and optimization algorithms, FitForgeAI helps users achieve their fitness objectives with customized workout routines.

## 🚀 Features

- **Personalized Exercise Plans**: Get workout routines tailored to your specific fitness goals, experience level, and daily schedule.
- **AI-Powered Recommendations**: Utilize advanced machine learning models to recommend the best exercises for you.
- **Routine Optimization**: Optimize your exercise plan based on time constraints and available equipment.
- **User Feedback Loop**: Provide feedback on your workouts to continuously improve and refine your exercise recommendations.

Algunos de los siguientes comandos inician con python o llevan python, pero en realidad el comando se utiliza py, no python


Paso 1: Verificar Instalación de Python y pip
Abrir el Símbolo del Sistema

Presiona Win + R, escribe cmd y presiona Enter.
Verificar Python

En el símbolo del sistema, escribe:
bash
Copiar código
python --version
Si recibes un mensaje que muestra la versión de Python, significa que Python está instalado. Si no se muestra la versión, continúa con el siguiente paso para instalar Python.
Verificar pip

En el símbolo del sistema, escribe:
bash
Copiar código
python -m pip --version
Si ves la versión de pip, significa que está instalado. Si no, sigue los pasos para instalar pip.
Paso 2: Instalar Python (Si No Está Instalado)
Descargar Python

Ve al sitio web oficial de Python: python.org/downloads.
Descarga el instalador de Python para Windows (elige la versión recomendada).
Ejecutar el Instalador

Abre el archivo descargado para iniciar el instalador.
Importante: Marca la casilla "Add Python to PATH" en la primera pantalla.
Haz clic en "Install Now" para proceder con la instalación.
Verificar Instalación

Después de la instalación, repite el paso 1 para verificar Python y pip.
Paso 3: Instalar pip (Si No Está Instalado)
Descargar get-pip.py

Abre tu navegador y ve a get-pip.py.
Guarda el archivo en una ubicación accesible, por ejemplo, tu escritorio.
Ejecutar get-pip.py

Abre el símbolo del sistema.
Navega a la ubicación donde guardaste get-pip.py. Si está en tu escritorio, usa:
bash
Copiar código
cd %USERPROFILE%\Desktop
Ejecuta el script con:
bash
Copiar código
py get-pip.py
Paso 4: Agregar Python y pip al PATH (Si Es Necesario)
Abrir Propiedades del Sistema

Presiona Win + R, escribe sysdm.cpl y presiona Enter.
Abrir Variables de Entorno

En la ventana de Propiedades del sistema, ve a la pestaña "Opciones avanzadas".
Haz clic en el botón "Variables de entorno".
Editar la Variable Path

En la sección "Variables del sistema", busca la variable Path y selecciónala.
Haz clic en "Editar".
Agregar Rutas

Haz clic en "Nuevo" y agrega las rutas a los directorios de Python y Scripts. Normalmente, estas rutas son:
C:\PythonXX (donde XX es la versión de Python, como C:\Python39)
C:\PythonXX\Scripts
Puedes encontrar estas rutas buscando el directorio de instalación de Python en tu sistema.
Guardar Cambios

Haz clic en "Aceptar" en todas las ventanas para guardar los cambios.
Paso 5: Reiniciar la Terminal
Cierra y vuelve a abrir el símbolo del sistema para que los cambios surtan efecto.

Paso 6: Instalar python-dotenv
Abrir el Símbolo del Sistema

Presiona Win + R, escribe cmd y presiona Enter.
Instalar python-dotenv

Ejecuta el siguiente comando:
bash
Copiar código
pip install python-dotenv
Ahora python-dotenv debería instalarse correctamente y estar listo para usar en tu proyecto Flask.