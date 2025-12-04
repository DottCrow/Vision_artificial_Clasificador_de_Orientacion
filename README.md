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
