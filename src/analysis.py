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

