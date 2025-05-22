# IMEDIA Proyect

## Introducción

IMEDIA PROJECT surge como una solución ante la creciente necesidad de las personas por mantenerse actualizadas con lo que ocurre en sus redes sociales y el mundo digital en general. En un entorno tan cambiante, donde la información fluye a gran velocidad, contar con herramientas que faciliten la exploración, análisis y comprensión de contenido en línea se vuelve esencial.

Este proyecto tiene como objetivo brindar una plataforma capaz de analizar publicaciones y comentarios de distintas redes sociales como Reddit, Facebook, Threads y Twitter, permitiendo búsquedas temáticas o por tendencias emergentes. Actualmente, el desarrollo se encuentra en una fase temprana, con Reddit como la única red integrada debido a la accesibilidad total de su API gratuita. Sin embargo, se proyecta la integración de nuevas plataformas en el futuro.

## Descripción General

IMEDIA PROJECT implementa un pipeline de análisis de datos centrado en la recolección y procesamiento de contenido proveniente de Reddit. El objetivo es automatizar todo el flujo de trabajo desde la extracción hasta la visualización de información, aplicando técnicas de procesamiento de lenguaje natural (NLP) y herramientas de business intelligence.

La arquitectura del pipeline está diseñada de manera modular, facilitando su mantenimiento, expansión y personalización. Las etapas principales comprenden:

-Extracción: Automatizada mediante la API oficial de Reddit.

-Transformación: Limpieza y estandarización de datos para análisis.

-Análisis de sentimientos: Actualmente con un modelo básico, con planes de integrar clasificadores más avanzados.

-Visualización: Resultados clave mostrados en dashboards interactivos con Power BI.

## Objetivos

-Automatizar la recopilación de contenido desde Reddit mediante su API.

-Estandarizar y transformar los datos para facilitar su análisis.

-Implementar modelos de NLP para clasificación por sentimiento o temática.

-Visualizar resultados mediante dashboards intuitivos y dinámicos.

-A futuro, incorporar LLMs (Large Language Models) que permitan a los usuarios realizar preguntas sobre temas de interés o generar contenido de manera asistida.

## Estado Actual
El proyecto se encuentra en desarrollo. Hasta el momento, se ha implementado exitosamente la parte de recolección y análisis básico de sentimientos desde Reddit. Próximas versiones incluirán:

-Análisis semántico profundo y detección de tópicos emergentes.

-Soporte para múltiples redes sociales.

-Integración de modelos LLM para interacción conversacional y generación de publicaciones.

## Estructura del Proyecto

```
IMEDIA_Project/
├── imedia_project/
│   ├── pipeline.py                        
│   ├── data_extraction/
│   │   └── extrac_from_reddit/
│   │       ├── Reddit_extract.py          
│   │       └── create_reddit_raw_data.py  
│   ├── data_procesing/
│   │   └── Reddit_pre_procesing.py        
│   ├── data_cleaning/
│   │   └── data_cleaning.py               
│   └── classification/
│       └── reddit_classifier.py     
│       
├── data/
│   ├── raw/                           
│   ├── interim/                       
│   ├── processed/                     
│   └── classified/    
│                 
├── .env                                   
├── README.md                              
├── report/                                
    └── reddit_insights_dashboard.pbix
```

## Tecnologías Utilizadas

- **Python 3.10+**
- **PRAW**
- **Pandas**
- **Hugging Face Transformers**
- **Power BI**
- **dotenv**

## Fases del Pipeline

### 1. Extracción de Datos
- Obtención de subreddits populares (tendencias).
- Descarga de posts recientes, destacados, comentarios y metadata del subreddit.
- Enriquecimiento con suscripciones de autores.

### 2. Preprocesamiento
- Conversión del JSON a múltiples CSVs: comentarios, posts, info del subreddit.

### 3. Limpieza y Tokenización
- Limpieza textual.
- Tokenización con `bert-base-uncased`.

### 4. Clasificación Semántica
- Clasificación de sentimientos o categorías usando modelo fine-tuned.
- Exportación de resultados clasificados.

### 5. Visualización con Power BI
- Creación de dashboards:
  - Sentimiento por subreddit
  - Nube de palabras
  - Comparativa por tipo de post
  - Tendencias temporales

## Configuración

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Configurar `.env` dentro de la carpeta extrac_from_reddit:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

## Ejecución

```bash
python imedia_project/pipeline.py
```

## Resultados Esperados

- JSON en `data/raw/`
- CSVs en `data/interim/`
- Archivos limpios en `data/processed/`
- Datos clasificados en `data/analice/`
- Visualización con Power BI

## Licencia

Este proyecto se distribuye bajo licencia MIT.
