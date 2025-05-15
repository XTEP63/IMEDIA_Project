
---
output: github_document
---

# IMEDIA Proyect

## Descripción General

Este proyecto implementa un pipeline de análisis de datos basado en publicaciones y comentarios obtenidos desde Reddit. El objetivo es automatizar la recolección, transformación, análisis semántico y visualización de información publicada por usuarios, permitiendo así generar reportes e insights relevantes a través de Power BI.

La arquitectura del pipeline sigue una estructura modular, permitiendo una fácil escalabilidad y mantenimiento. Las etapas cubren desde la extracción de datos hasta el análisis visual de sentimientos y temas frecuentes mediante herramientas de inteligencia artificial y business intelligence.

## Objetivos

- Automatizar la recopilación de contenido desde Reddit usando su API.
- Estandarizar y limpiar los datos para su análisis.
- Aplicar modelos de NLP para clasificar publicaciones según sentimiento o temática.
- Visualizar resultados clave a través de dashboards interactivos.

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
│   └── reddit_insights_dashboard.pbix
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

2. Configurar `.env`:

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
- Datos clasificados en `data/classified/`
- Visualización con Power BI

## Licencia

Este proyecto se distribuye bajo licencia MIT.
