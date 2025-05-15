# from pipeline import Pipeline
from data_extraction.extrac_from_reddit.create_reddit_raw_data import CreateRawRedditData
from data_extraction.extrac_from_reddit.Reddit_extract import Reddit_extraction
from data_procesing.Reddit_pre_procesing import RedditPreProcessing
from data_cleaning.data_cleaning import DataProcessor
import os

class RedditPipeline:
    def __init__(self, base_path, post_limit=100, comment_limit=100, subreddits=None):
        self.base_path = base_path
        self.post_limit = post_limit
        self.comment_limit = comment_limit
        self.subreddits = subreddits if subreddits else []

    def extract_data(self):
        """Fase de extracción de datos"""
        reddit_extraction = Reddit_extraction()
        trending_subreddits = reddit_extraction.get_trending_subreddits(1000*4)
        trending_subreddits = set(trending_subreddits)
        print(f'-------------------------Tenemos {len(trending_subreddits)} subreddits que son {trending_subreddits}-------------------------')

        reddit_data = CreateRawRedditData(trending_subreddits, post_limit=self.post_limit, comment_limit=self.comment_limit)
        print("Recopilando datos de Reddit...")
        reddit_data.fetch_data()

        reddit_data.save_to_json(os.path.join(self.base_path, "data/raw/raw_reddit_data.json"))

    def preprocess_data(self):
        """Fase de preprocesamiento de datos"""
        processor = RedditPreProcessing(self.base_path)
        processor.process()

    def clean_data(self):
        """Fase de limpieza de datos"""
        processor = DataProcessor(self.base_path)
        processor.process_all()

    def run(self):
        """Ejecuta el pipeline completo"""
        self.extract_data()
        self.preprocess_data()
        self.clean_data()

# Ejecutar el pipeline
if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pipeline = RedditPipeline(base_path)
    pipeline.run()
