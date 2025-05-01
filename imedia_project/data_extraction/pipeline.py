# pipeline.py

from extrac_from_reddit.create_reddit_raw_data import CreateRawRedditData
from extrac_from_reddit.Reddit_extract  import Reddit_extraction

def main():
    reddit_extraction = Reddit_extraction()
    # Subreddits a los que se desea acceder
    trending_subreddits = reddit_extraction.get_trending_subreddits(100)
    
    # Crear una instancia de la clase CreateRawRedditData
    reddit_data = CreateRawRedditData(trending_subreddits, post_limit=100, comment_limit=100)
    
    # Recopilar los datos de Reddit
    print("Recopilando datos de Reddit...")
    reddit_data.fetch_data()

    # Guardar los datos de Reddit en un archivo JSON
    reddit_data.save_to_json("../../data/raw/raw_reddit_data.json")


if __name__ == "__main__":
    main()
