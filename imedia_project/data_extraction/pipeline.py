# pipeline.py

from extrac_from_reddit.create_reddit_raw_data import CreateRawRedditData
from extrac_from_reddit.Reddit_extract  import Reddit_extraction
# Si tienes otras clases para extracción de datos de X (Twitter o Facebook), también las importamos
# from data_extraction.extrac_from_x.some_other_extraction_class import SomeOtherExtractionClass

def main():
    reddit_extraction = Reddit_extraction()
    trending_subreddits = reddit_extraction.get_trending_subreddits(100)
    # Subreddits a los que se desea acceder
    
    # Crear una instancia de la clase CreateRawRedditData
    reddit_data = CreateRawRedditData(trending_subreddits, post_limit=100, comment_limit=10000)
    
    # Recopilar los datos de Reddit
    print("Recopilando datos de Reddit...")
    reddit_data.fetch_data()

    # Guardar los datos de Reddit en un archivo JSON
    reddit_data.save_to_json("../../data/raw/raw_reddit_data.json")
    
    # Si tienes otros extractores para diferentes plataformas (por ejemplo, X o Facebook), ejecutarlos aquí
    # print("Recopilando datos de X (Twitter/Facebook)...")
    # other_data = SomeOtherExtractionClass()
    # other_data.fetch_data()
    # other_data.save_to_json("raw_other_data.json")

if __name__ == "__main__":
    main()
