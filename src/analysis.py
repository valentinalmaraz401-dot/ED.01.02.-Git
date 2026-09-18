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