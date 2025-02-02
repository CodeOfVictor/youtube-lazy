# youtube-lazy

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Technologies Used](#technologies-used)
5. [Advanced Configuration](#advanced-configuration)

## Description
**youtube-lazy** is an automated tool that allows downloading YouTube subtitles, cleaning them, and generating a summary using a local AI model via **GPT4All**. This project runs entirely locally without relying on external APIs.

---

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/CodeOfVictor/youtube-lazy
cd youtube-lazy
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage
### Run the main script:
```bash
python main.py
```

### Example Execution:
```
Loading AI model...
🎥 Enter YouTube video URL: https://youtu.be/ZhvIio21eeU
Getting subtitles from the video...
🔹 Processing subtitles for summary...
🔹 Summarizing part 1/4...
🔹 Summarizing part 2/4...
🔹 Summarizing part 3/4...
🔹 Summarizing part 4/4...
--- FINAL SUMMARY ---

Summary: 
The author criticizes Red Bull Racing for not adequately preparing for 2026 and worries about the possibility of losing drivers if they do not win. However, he also admits that the team might be able to solve its problems if managed well and believes he will see how the situation unfolds.

The author highlights that Red Bull Racing has a lot of money but will have nothing to gain if they lose drivers, which could be disastrous for everyone. The team needs a competitive engine in 2026 to win.

In summary, the author is concerned about Red Bull Racing's current situation and believes they may be able to solve their problems if they adjust properly. However, he also acknowledges that there are many uncertainties.
```


## Technologies Used
- **Python**: Main language of the project.
- **yt-dlp**: Library for downloading YouTube subtitles.
- **GPT4All**: AI model for generating summaries locally.
- **CUDA (Optional)**: To improve performance on NVIDIA GPUs.

---

## Advanced Configuration
If you want to use a different AI model, make sure it is downloaded in the GPT4All models folder and modify it in `main.py`:
```python
model = GPT4All("Model_Name.gguf", device="gpu")  # Or "cpu" if you do not have a GPU
```

To check available models:
```python
from gpt4all import GPT4All
print(GPT4All.list_models())
```

# youtube-lazy

## Índice
1. [Descripción](#descripción)
2. [Instalación](#instalación)
3. [Uso](#uso)
4. [Tecnologías Utilizadas](#tecnologías-utilizadas)
5. [Configuración Avanzada](#configuración-avanzada)

## Descripción
**youtube-lazy** es una herramienta automatizada que permite descargar los subtítulos de un video de YouTube, limpiarlos y generar un resumen utilizando un modelo de inteligencia artificial local a través de **GPT4All**. Este proyecto se ejecuta completamente en local, sin depender de APIs externas.

---

## Instalación
### 1. Clonar el repositorio
```bash
git clone https://github.com/CodeOfVictor/youtube-lazy
cd youtube-lazy
```
### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## Uso
### Ejecutar el script principal:
```bash
python main.py
```

### Ejemplo de ejecución:
```
Cargando modelo de IA...
🎥 Introduce la URL del video de YouTube: https://youtu.be/ZhvIio21eeU
Obteniendo subtítulos del video...
🔹 Procesando subtítulos para el resumen...
🔹 Resumiendo parte 1/4...
🔹 Resumiendo parte 2/4...
🔹 Resumiendo parte 3/4...
🔹 Resumiendo parte 4/4...
--- RESUMEN FINAL ---

Resumen: 
El autor critica a Red Bull Racing por no haber preparado adecuadamente para 2026 y le preocupa la posibilidad de perder pilotos en caso de no ganar. Sin embargo, también admite que el equipo puede ser capaz de solucionar sus problemas si lo hace bien y cree que podrá ver cómo va a salir la situación.

El autor destaca que Red Bull Racing tiene una gran cantidad de dinero en el bolsillo pero no tendrá nada que ganar si pierde pilotos, lo que podría generar un desastre para todo el mundo. El equipo necesita tener un buen motor competitivo en 2026 para poder ganar.

En resumen, el autor está preocupado por la situación actual de Red Bull Racing y cree que puede ser capaz de solucionar sus problemas si se ajusta adecuadamente. Sin embargo, también reconoce que hay muchas incertidumbres.
```


## Tecnologías Utilizadas
- **Python**: Lenguaje principal del proyecto.
- **yt-dlp**: Biblioteca para la descarga de subtítulos de YouTube.
- **GPT4All**: Modelo de inteligencia artificial para generar resúmenes en local.
- **CUDA (Opcional)**: Para mejorar el rendimiento en GPUs NVIDIA.

---

## Configuración Avanzada
Si quieres utilizar un modelo de IA diferente, asegúrate de que esté descargado en la carpeta de modelos de GPT4All y modifícalo en `main.py`:
```python
model = GPT4All("Nombre_del_modelo.gguf", device="gpu")  # O "cpu" si no tienes GPU
```

Para verificar los modelos disponibles:
```python
from gpt4all import GPT4All
print(GPT4All.list_models())
```

---
