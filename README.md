# Predicción de Demanda del Proyecto Organizador de Inventario

## Descripción General

Este proyecto tiene como objetivo predecir la demanda del stock de empresas para mejorar la organización y reducir costos. El modelo, desarrollado con Random Forest, es capaz de prever la demanda futura basada en datos estructurados provenientes del Data Mining Cup 2020 (21ª edición). El dataset utilizado se titula "Forecasting Demand for Optimized Inventory Planning" y ayuda a optimizar la planificación del inventario.

## Características del Proyecto

- Predicción de la demanda (variable dependiente "y").
- Modelo entrenado con Random Forest.
- Optimización del inventario para reducir costos y mejorar la planificación.

## Tecnologías Utilizadas

- **Lenguaje**: Python
- **Bibliotecas**:
  - pandas
  - scikit-learn
  - joblib

## Requisitos del Entorno

Asegúrate de tener las siguientes herramientas instaladas (en sus versiones más recientes):
- Python
- pandas
- scikit-learn
- joblib

## Instrucciones de Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <url-del-repositorio>
2. Instala las dependencias necesarias:
    ```bash
   pip install -r requirements.txt

## Dataset

El dataset utilizado para entrenar el modelo es público y puede descargarse desde la Data Mining Cup 2020.

## Evaluación del Modelo
El modelo se evaluó utilizando las siguientes métricas:

- Mean Squared Error (MSE): 164.95
- R² Score: 0.9999

## Uso del Proyecto
Actualmente, el proyecto solo contiene el modelo entrenado. En los próximos días se implementará una API para poder realizar predicciones de manera más accesible. Las instrucciones sobre cómo desplegar el modelo estarán disponibles una vez que se implemente.

## Autor
- GitHub: AlexisSchiavon

## Licencia
Este proyecto no cuenta con una licencia pública en este momento.