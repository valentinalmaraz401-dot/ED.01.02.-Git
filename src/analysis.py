import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = pd.read_csv('data/StudentsPerformance.csv')

# 2. Exploración inicial
print("=== EXPLORACIÓN INICIAL ===")
print(f"Número de registros (filas): {df.shape[0]}")
print(f"Número de columnas: {df.shape[1]}")
print("\nNombre de las variables:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores faltantes por columna:")
print(df.isnull().sum())

print(f"\nRegistros duplicados: {df.duplicated().sum()}")

print("\nEstadísticas descriptivas:")
print(df.describe())

# Limpieza
df = df.drop_duplicates()

# Crear variable average_score
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Clasificación de rendimiento
def clasificar_rendimiento(prom):
    if prom < 60:
        return 'Bajo'
    elif prom < 80:
        return 'Medio'
    else:
        return 'Alto'

df['rendimiento_categoria'] = df['average_score'].apply(clasificar_rendimiento)

# Análisis de preguntas
print("\n=== PROMEDIO POR ÁREA ===")
print(f"Matemáticas: {df['math score'].mean():.2f}")
print(f"Lectura: {df['reading score'].mean():.2f}")
print(f"Escritura: {df['writing score'].mean():.2f}")

print("\n=== IMPACTO CURSO DE PREPARACIÓN ===")
print(df.groupby('test preparation course')['average_score'].mean())

print("\n=== NIVEL EDUCATIVO DE PADRES ===")
print(df.groupby('parental level of education')['average_score'].mean().sort_values(ascending=False))

print("\n=== PORCENTAJE POR CATEGORÍA ===")
print(df['rendimiento_categoria'].value_counts(normalize=True) * 100)

# ==========================================
# VISUALIZACIÓN 1: DISTRIBUCIÓN DE RENDIMIENTO
# ==========================================
plt.figure(figsize=(8, 5))
df['rendimiento_categoria'].value_counts().reindex(['Bajo', 'Medio', 'Alto']).plot(kind='bar', color=['#e74c3c', '#f1c40f', '#2ecc71'])
plt.title('Distribución de Estudiantes por Categoría de Rendimiento')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de Estudiantes')
plt.tight_layout()
plt.savefig('outputs/distribucion_rendimiento.png')
plt.close()
print("Gráfico 1 guardado en outputs/distribucion_rendimiento.png")

# ==========================================
# VISUALIZACIÓN 2: PROMEDIO POR MATERIA
# ==========================================
promedios_materias = df[['math score', 'reading score', 'writing score']].mean()

plt.figure(figsize=(8, 5))
promedios_materias.plot(kind='bar', color=['#3498db', '#9b59b6', '#1abc9c'])
plt.title('Promedio General por Materia')
plt.xlabel('Materia')
plt.ylabel('Promedio')
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig('outputs/promedio_por_materia.png')
plt.close()
print("Gráfico 2 guardado en outputs/promedio_por_materia.png")
