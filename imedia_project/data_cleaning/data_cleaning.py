import pandas as pd
import ast
import os
from transformers import AutoTokenizer

class DataProcessor:
    def __init__(self, base_path):
        self.base_path = base_path
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.processed_path = os.path.join(base_path, 'data', 'processed')
        os.makedirs(self.processed_path, exist_ok=True)

    def safe_tokenize(self, text):
        """Tokeniza texto de manera segura, manejando casos no strings."""
        if isinstance(text, str):
            return self.tokenizer.encode(text, add_special_tokens=True)
        return []

    def process_comments(self):
        """Procesa los datos de comentarios."""
        path = os.path.join(self.base_path, 'data', 'interim', 'comments_data.csv')
        comments = pd.read_csv(path)
        
        # Limpieza y conversión a minúsculas
        for col in ['author', 'body', 'subreddit']:
            comments[col] = comments[col].str.lower()
        
        # Procesamiento de suscripciones
        comments["user_subscriptions"] = comments["user_subscriptions"].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        comments["is_subscribed"] = comments.apply(
            lambda row: row["subreddit"] in row["user_subscriptions"], axis=1)
        
        # Tokenización
        comments['body_tokenized'] = comments['body'].apply(self.safe_tokenize)
        comments['subreddit_tokenized'] = comments['subreddit'].apply(self.safe_tokenize)
        comments['user_subscriptions_tokenized'] = comments['user_subscriptions'].apply(
            lambda subs: [self.safe_tokenize(sub) for sub in subs] if isinstance(subs, list) else [])
        
        # Guardar
        save_path = os.path.join(self.processed_path, 'comments_processed.csv')
        comments.to_csv(save_path, index=False)
        print(f"Comentarios procesados guardados en: {save_path}")
        return comments

    def process_posts(self, file_name, output_name):
        """Procesa datos de posts (genérico para diferentes tipos de posts)."""
        path = os.path.join(self.base_path, 'data', 'interim', file_name)
        posts = pd.read_csv(path)
        
        # Limpieza y conversión a minúsculas
        for col in posts.columns:
            if posts[col].dtype == 'object':
                posts[col] = posts[col].str.lower()
        
        # Tokenización (columnas específicas)
        if 'title' in posts.columns:
            posts['title_tokenized'] = posts['title'].apply(self.safe_tokenize)
        if 'subreddit' in posts.columns:
            posts['subreddit_tokenized'] = posts['subreddit'].apply(self.safe_tokenize)
        
        # Guardar
        save_path = os.path.join(self.processed_path, output_name)
        posts.to_csv(save_path, index=False)
        print(f"Posts procesados ({output_name}) guardados en: {save_path}")
        return posts

    def process_all(self):
        """Ejecuta todo el pipeline de procesamiento."""
        self.process_comments()
        self.process_posts('posts_relacionados_data.csv', 'posts_processed.csv')
        self.process_posts('subreddit_info_data.csv', 'subreddit_info_processed.csv')
        self.process_posts('top_posts_data.csv', 'top_posts_processed.csv')
        self.process_posts('ultimos_posts_data.csv', 'ultimos_posts_processed.csv')

# Uso
if __name__ == "__main__":
    base_path = '/Users/isavalladolid/Documents/Documentos - MacBook Air de Isabel/IMEDIA_Project'
    processor = DataProcessor(base_path)
    processor.process_all()