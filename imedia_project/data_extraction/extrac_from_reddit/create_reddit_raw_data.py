# create_raw_reddit_data.py
import json
from .Reddit_extract import Reddit_extraction  # Importa la clase base

class CreateRawRedditData(Reddit_extraction):
    
    def __init__(self, subreddits, post_limit=10, comment_limit=10):
        """Inicializa la clase con los subreddits y cantidad de posts."""
        super().__init__()  # Inicializa la clase base
        self.subreddits = subreddits
        self.post_limit = post_limit
        self.comment_limit = comment_limit  # Nuevo parámetro para limitar los comentarios
        self.data = {}

    def fetch_data(self):
        """Obtiene todos los datos relevantes de los subreddits."""
        for subreddit in self.subreddits:
            print(f"Fetching data for subreddit: {subreddit}")
            subreddit_data = {}

            # Obtén los posts más recientes (últimos 24 horas por defecto)
            subreddit_data["ultimos_posts"] = self.get_top_posts(subreddit, limit=self.post_limit)
            print(f"Últimos posts: {subreddit_data['ultimos_posts']}")
            print('-------------------------------------------------------------------')
            
            # Obtén los posts más populares de todos los tiempos
            subreddit_data["top_posts"] = self.get_top_posts_all_time(subreddit, limit=self.post_limit)
            print(f"Top posts: {subreddit_data['top_posts']}")
            print('-------------------------------------------------------------------')
            
            # Buscar posts relacionados (usando un término de búsqueda)
            subreddit_data["posts_relacionados"] = self.search_reddit(subreddit, limit=self.post_limit)
            print(f"Posts relacionados: {subreddit_data['posts_relacionados']}")
            print('-------------------------------------------------------------------')
            
            # Obtener comentarios más recientes usando el método correcto
            subreddit_data["comentarios_mas_recientes"] = self.get_recent_comments(subreddit, limit=self.comment_limit)
            print(f"Comentarios más recientes: {subreddit_data['comentarios_mas_recientes']}")
            print('-------------------------------------------------------------------')

            # Obtener información del subreddit
            subreddit_data["subreddit_info"] = self.get_subreddit_info(subreddit)
            print(f"Información del subreddit: {subreddit_data['subreddit_info']}")
            print('-------------------------------------------------------------------')

            # Para cada comentario, obtener las suscripciones del autor
            for comment in subreddit_data.get("comentarios_mas_recientes", []):
                author = comment.get("author")
                if author:
                    print(f"Obteniendo suscripciones para el autor: {author}")
                    user_subscriptions = self.get_user_subscriptions(author)  # Obtener subreddits donde el autor ha publicado
                    comment['user_subscriptions'] = user_subscriptions  # Guardar suscripciones del autor en el comentario

            # Guardar los datos en el diccionario
            self.data[subreddit] = subreddit_data

    def is_video_or_image(self, post):
        """Verifica si un post es un video o una imagen usando su URL"""
        if 'v.redd.it' in post.get('url', '') or 'i.redd.it' in post.get('url', ''):
            return True
        return False

    def save_to_json(self, file_name="reddit_data.json"):
        """Guarda los datos recopilados en un archivo JSON"""
        # Reemplazar None por listas vacías para evitar que se guarde como null en el JSON
        for subreddit, data in self.data.items():
            if data.get('comentarios_mas_recientes') is None:
                data['comentarios_mas_recientes'] = []
            if data.get('subreddit_info') is None:
                data['subreddit_info'] = {}

        with open(file_name, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"Data saved to {file_name}")

# Aquí empieza el bloque para ejecutar la prueba
if __name__ == "__main__":
    # Lista de subreddits para probar
    subreddits = ['programming']

    # Crear una instancia de la clase CreateRawRedditData
    reddit_data = CreateRawRedditData(subreddits, post_limit=5)

    # Recopilar los datos
    reddit_data.fetch_data()

    # Guardar los datos en un archivo JSON
    reddit_data.save_to_json("raw_reddit_data.json")
