# ED.01.02.-Git
# Análisis del Rendimiento Académico de los Estudiantes

Proyecto desarrollado para la asignatura de Manejo Masivo de Datos. Aplica un flujo de trabajo reproducible en Python utilizando Git y GitHub para la exploración, procesamiento y visualización del desempeño académico.

## Dataset

* **Nombre del dataset:** Students Performance in Exams
* **Fuente:** Kaggle (spscientist/students-performance-in-exams)
* **Descripción breve:** Registro de 1,000 estudiantes que incluye puntajes en tres exámenes (matemáticas, lectura y escritura) junto con variables demográficas y socioeconómicas como género, nivel educativo de los padres, tipo de almuerzo y preparación previa.

## Objetivo

Realizar un análisis exploratorio de datos (EDA) para identificar patrones clave, diferencias por asignatura, el impacto de la preparación previa y la influencia del nivel educativo de los padres en los resultados académicos.

## Requisitos

El proyecto requiere **Python 3.x** y las librerías indicadas en el archivo `requirements.txt` (`pandas`, `matplotlib`).

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/valentinalmaraz401-dot/ED.01.02.-Git.git
2. **entrar al proyecto**
    cd ED.01.02.-Git
3. **crear el entorno virtual**
    python -m venv .venv
4. **activarlo e instalar dependencias**
    .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

5. **estructura del proyecto**

ED.01.02.-Git/
├── data/
│   └── StudentsPerformance.csv
├── src/
│   └── analysis.py
├── outputs/
│   ├── distribucion_rendimiento.png
│   ├── promedio_por_materia.png
│   └── impacto_curso_preparacion.png
├── .gitignore
├── README.md
└── requirements.txt

## ejecusion
python src/analysis.py