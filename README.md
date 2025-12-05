# Proyecto 3: Clasificador de Orientación de Objetos

Este proyecto implementa un sistema de visión por computadora para el control de calidad en líneas de ensamblaje. Utiliza un enfoque híbrido combinando *Deep Learning (YOLOv8)* para la detección de objetos y *Algoritmos Geométricos (PCA)* para determinar la orientación precisa de las piezas.

## 📋 Descripción General

El sistema detecta objetos en tiempo real mediante una webcam, aisla la región de interés (ROI) y calcula el ángulo de rotación del objeto utilizando Análisis de Componentes Principales (PCA). Finalmente, clasifica la posición del objeto en tres categorías:
* *Horizontal* (Verde)
* *Vertical* (Rojo)
* *Inclinado* (Amarillo)

## 🚀 Instalación y Requisitos

1. Clonar el repositorio.
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt

# 📐 Clasificador de Orientación con YOLOv8

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![YOLOv8](https://img.shields.io/badge/YOLO-v8-green) ![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)

## 📌 Descripción del proyecto

Este proyecto implementa un sistema de visión artificial en tiempo real capaz de detectar objetos y clasificar su orientación basándose en la geometría de su caja delimitadora (*bounding box*).

El sistema utiliza **YOLOv8** (Ultralytics) para la detección y **OpenCV** para el procesamiento de imagen y visualización.

### Funcionalidades principales:
* **Detección de objetos:** Utiliza el modelo `yolov8n.pt` para inferencia rápida.
* **Clasificación geométrica:** Determina si el objeto está:
    * Horizontal
    * Vertical
    * Inclinado / Cuadrado
* **Filtro inteligente:** Excluye automáticamente la detección de personas para centrarse en objetos.
* **Feedback visual:** Muestra nombre, confianza, orientación y guías visuales (flechas o cruces) en pantalla.

---

## 🧠 ¿Cómo funciona?

### 1. Detección con YOLOv8
El modelo escanea el frame y devuelve las coordenadas `xyxy` (esquinas de la caja), la clase detectada y el nivel de confianza. Se utiliza el modelo **Nano** para garantizar fluidez en tiempo real.

### 2. Cálculo de Orientación
El algoritmo analiza la **Razón de Aspecto** ($Ratio = Width / Height$) de la caja detectada:

| Condición | Clasificación |
| :--- | :--- |
| `Ancho (w) >> Alto (h)` | **Horizontal** |
| `Alto (h) >> Ancho (w)` | **Vertical** |
| `Ancho ≈ Alto` | **Inclinado / Cuadrado** |

### 3. Visualización
El sistema dibuja indicadores sobre la imagen original:

* 🟩 **Horizontal:** Color Verde + Flecha Izquierda-Derecha (`↔`)
* 🟥 **Vertical:** Color Rojo + Flecha Arriba-Abajo (`↕`)
* 🟨 **Inclinado:** Color Amarillo + Cruz Diagonal (`❌`)

> **🚫 Nota:** El sistema ignora la clase "person" para evitar interferencias del usuario frente a la cámara.

---

## 📦 Requisitos e Instalación

Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias:

```bash
pip install opencv-python ultralytics numpy
