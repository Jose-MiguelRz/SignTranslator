import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import os

print("=== ENTRENAMIENTO DEL MODELO ===\n")

# Cargar datos
data_path = 'data/sign_data.csv'
if not os.path.exists(data_path):
    print(f"❌ Error: No se encuentra {data_path}")
    exit()

df = pd.read_csv(data_path)
print(f"✅ Datos cargados: {len(df)} muestras")
print(f"📊 Distribución:")
print(df['label'].value_counts())
print()

# Preparar datos
X = df.drop('label', axis=1).values  # Características (coordenadas)
y = df['label'].values                # Etiquetas (señas)

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"📊 Entrenamiento: {len(X_train)} muestras")
print(f"📊 Prueba: {len(X_test)} muestras\n")

# Crear y entrenar modelo
print("🤖 Entrenando Random Forest...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Evaluar modelo
accuracy = model.score(X_test, y_test)
print(f"✅ Precisión: {accuracy:.2%}\n")

# Mostrar reporte detallado
y_pred = model.predict(X_test)
print("📋 Reporte por seña:")
print(classification_report(y_test, y_pred))

# Mostrar matriz de confusión
print("📊 Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# Guardar modelo
print("\n💾 Guardando modelo...")
if not os.path.exists('../models'):
    os.makedirs('../models')

model_path = '../models/sign_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

# Guardar información del modelo
model_info = {
    'classes': list(model.classes_),
    'accuracy': accuracy,
    'features': list(df.drop('label', axis=1).columns)
}

info_path = '../models/model_info.pkl'
with open(info_path, 'wb') as f:
    pickle.dump(model_info, f)

print(f"✅ Modelo guardado en: {model_path}")
print(f"✅ Información guardada en: {info_path}")

print("\n🎉 ¡ENTRENAMIENTO COMPLETADO!")
