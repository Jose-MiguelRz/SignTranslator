# 🤟 SignTranslator - Intérprete de Lenguaje de Señas en Tiempo Real

![Python](https://img.shields.io/badge/Python-3.10-blue)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.11-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange)

<div align="center">

### ✨ Traduce lenguaje de señas a texto en tiempo real usando Inteligencia Artificial ✨

</div>

---

# 📝 Descripción

**SignTranslator** es una aplicación de inteligencia artificial que traduce lenguaje de señas en tiempo real usando **visión por computadora y machine learning**.

El sistema detecta **21 puntos clave de la mano** mediante **MediaPipe** y clasifica los gestos utilizando un modelo **Random Forest**, logrando una precisión del **100% en pruebas controladas**.

Este proyecto fue desarrollado como parte de mi portafolio para demostrar habilidades en:

- Visión por computadora
- Machine Learning
- Procesamiento en tiempo real
- Desarrollo de aplicaciones con Python
- Sistemas de clasificación de gestos

---

# ✨ Características

- ✅ Traducción de señas en **tiempo real**
- ✅ Procesamiento de video a **30+ FPS**
- ✅ Reconocimiento de **5 señas**
- ✅ Sistema de **confianza del modelo**
- ✅ Interfaz visual con feedback inmediato
- ✅ Modelo fácilmente extensible para agregar más señas
- ✅ Dataset propio con **310 muestras**

Señas soportadas actualmente:

- 🤟 HOLA  
- 🙏 GRACIAS  
- ❤️ TE QUIERO  
- 👍 SI  
- 👎 NO  

---

# 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| Python | Lenguaje principal |
| MediaPipe | Detección de landmarks de la mano |
| OpenCV | Procesamiento de video |
| scikit-learn | Entrenamiento del modelo Random Forest |
| NumPy | Manejo de arrays |
| Pandas | Procesamiento de dataset |

---

# 📋 Requisitos

- Python 3.10 o superior  
- Cámara web  
- Windows / Mac / Linux  

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Jose-MiguelRz/SignTranslator.git
cd SignTranslator
````

## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 💻 Uso

## Opción 1: Usar el modelo ya entrenado

```bash
cd src
python real_time_translator.py
```

Presiona **q** para salir.

---

## Opción 2: Entrenar tu propio modelo

### Paso 1: Recolectar datos

```bash
cd src
python collect_data.py
```

Controles:

* Presiona **1-5** para elegir la seña
* Haz la seña frente a la cámara
* Presiona **ESPACIO** para guardar
* Repite **30+ veces por seña**
* Presiona **q** para salir

### Paso 2: Entrenar el modelo

```bash
python train_model.py
```

### Paso 3: Ejecutar el traductor

```bash
python real_time_translator.py
```

---

# 🎯 Ejemplo de ejecución

```
🎥 TRADUCTOR EN TIEMPO REAL
Presiona 'q' para salir

🤟 SEÑA: HOLA        (Confianza: 98%)
🙏 SEÑA: GRACIAS     (Confianza: 95%)
❤️ SEÑA: TE QUIERO   (Confianza: 97%)
👍 SEÑA: SI          (Confianza: 99%)
👎 SEÑA: NO          (Confianza: 96%)
```

---

# 📊 Resultados del Modelo

| Métrica          | Resultado |
| ---------------- | --------- |
| Muestras totales | 310       |
| Precisión        | 100%      |
| FPS promedio     | 30+       |
| Número de señas  | 5         |

Distribución del dataset:

```
GRACIAS      113
NO           104
HOLA          33
TE_QUIERO     30
SI            30
```

---

# 🗂️ Estructura del Proyecto

```
SignTranslator/

src/
 ├ collect_data.py
 ├ train_model.py
 └ real_time_translator.py

data/
 └ sign_data.csv

models/
 ├ sign_model.pkl
 └ model_info.pkl

requirements.txt
README.md
```

---

# 🔮 Posibles Mejoras

* Interfaz gráfica completa
* Reconocimiento del abecedario completo
* Traducción de frases completas
* Versión móvil
* API para integración web
* Dataset más grande

---

# 👨‍💻 Autor

**José Miguel Rodríguez**

GitHub
[https://github.com/Jose-MiguelRz](https://github.com/Jose-MiguelRz)

Repositorio del proyecto
[https://github.com/Jose-MiguelRz/SignTranslator](https://github.com/Jose-MiguelRz/SignTranslator)

---

<div align="center">

### ⭐ Si te gustó este proyecto, considera darle una estrella ⭐

Hecho con Python y visión por computadora

</div>
```
