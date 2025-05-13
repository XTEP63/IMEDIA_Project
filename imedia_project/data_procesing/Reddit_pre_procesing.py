import json
import pandas as pd

class RedditPreProcessing:
    def __init__(self, base_path):
        self.base_path = base_path
        self.reddit_data = self.load_data()

    def load_data(self):
        """Carga los datos del archivo JSON"""
        with open(f"{self.base_path}/data/raw/raw_reddit_data.json", "r") as file:
            return json.load(file)

    def process(self):
        """Procesa los datos de Reddit y los convierte a DataFrame"""
        # Crear DataFrames vacíos para cada tipo de información
        comments_df = pd.DataFrame(columns=['author', 'body', 'user_subscriptions', 'subreddit'])
        ultimos_posts_df = pd.DataFrame(columns=['title', 'score', 'url', 'subreddit'])
        top_posts_df = pd.DataFrame(columns=['title', 'score', 'url', 'subreddit'])
        posts_relacionados_df = pd.DataFrame(columns=['title', 'score', 'url', 'subreddit'])
        subreddit_info_df = pd.DataFrame(columns=['name', 'subscribers', 'description', 'subreddit'])

        # Listas temporales para almacenar los datos
        comments_data = []
        ultimos_posts_data = []
        top_posts_data = []
        posts_relacionados_data = []
        subreddit_info_data = []

        # Recorrer cada subreddit y sus datos
        for subreddit, data in self.reddit_data.items():
            # Procesar comentarios
            for comment in data.get('comentarios_mas_recientes', []):
                comment_data = {
                    'author': comment.get('author'),
                    'body': comment.get('body'),
                    'user_subscriptions': comment.get('user_subscriptions'),
                    'subreddit': subreddit
                }
                comments_data.append(comment_data)

            # Procesar últimos posts
            for post in data.get('ultimos_posts', []):
                post_data = {
                    'title': post.get('title'),
                    'score': post.get('score'),
                    'url': post.get('url'),
                    'subreddit': subreddit
                }
                ultimos_posts_data.append(post_data)

            # Procesar top posts
            for post in data.get('top_posts', []):
                post_data = {
                    'title': post.get('title'),
                    'score': post.get('score'),
                    'url': post.get('url'),
                    'subreddit': subreddit
                }
                top_posts_data.append(post_data)

            # Procesar posts relacionados
            for post in data.get('posts_relacionados', []):
                post_data = {
                    'title': post.get('title'),
                    'score': post.get('score'),
                    'url': post.get('url'),
                    'subreddit': subreddit
                }
                posts_relacionados_data.append(post_data)

            # Procesar información del subreddit
            subreddit_info = data.get('subreddit_info', {})
            subreddit_info_data.append({
                'name': subreddit_info.get('name'),
                'subscribers': subreddit_info.get('subscribers'),
                'description': subreddit_info.get('description'),
                'subreddit': subreddit
            })

        # Crear los DataFrames usando pd.concat()
        comments_df = pd.concat([comments_df, pd.DataFrame(comments_data)], ignore_index=True)
        ultimos_posts_df = pd.concat([ultimos_posts_df, pd.DataFrame(ultimos_posts_data)], ignore_index=True)
        top_posts_df = pd.concat([top_posts_df, pd.DataFrame(top_posts_data)], ignore_index=True)
        posts_relacionados_df = pd.concat([posts_relacionados_df, pd.DataFrame(posts_relacionados_data)], ignore_index=True)
        subreddit_info_df = pd.concat([subreddit_info_df, pd.DataFrame(subreddit_info_data)], ignore_index=True)

        # Guardar los DataFrames como archivos CSV
        comments_df.to_csv(f'{self.base_path}/data/interim/comments_data.csv', index=False)
        ultimos_posts_df.to_csv(f'{self.base_path}/data/interim/ultimos_posts_data.csv', index=False)
        top_posts_df.to_csv(f'{self.base_path}/data/interim/top_posts_data.csv', index=False)
        posts_relacionados_df.to_csv(f'{self.base_path}/data/interim/posts_relacionados_data.csv', index=False)
        subreddit_info_df.to_csv(f'{self.base_path}/data/interim/subreddit_info_data.csv', index=False)

        print("Datos procesados y guardados con éxito.")
