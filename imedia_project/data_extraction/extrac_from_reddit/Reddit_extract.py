import praw
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class Reddit_extraction:
    
    def __init__(self):
        """Inicializa la clase con las credenciales de la API de Reddit."""
        
        # Cargar las credenciales desde el archivo .env
        self.CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
        self.CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
        self.USER_AGENT = os.getenv('REDDIT_USER_AGENT')
        
        # Autenticación con Reddit
        self.reddit = praw.Reddit(client_id=self.CLIENT_ID,
                                  client_secret=self.CLIENT_SECRET,
                                  user_agent=self.USER_AGENT)

    def get_top_posts(self, subreddit, limit=10):
        """Obtener los posts más recientes de un subreddit"""
        
        try:
            # Obtener los 10 posts más recientes del subreddit
            top_posts = self.reddit.subreddit(subreddit).top(limit=limit)
            print(f"Top {limit} posts de r/{subreddit}:")
            for post in top_posts:
                print(f"Title: {post.title}")
                print(f"Score: {post.score}")
                print(f"URL: {post.url}\n")
        except Exception as e:
            print(f"Error al obtener los posts de Reddit: {e}")
    
    def get_comments(self, post_id):
        """Obtener los comentarios de un post específico"""
        
        try:
            # Obtener un post usando su ID y luego los comentarios
            post = self.reddit.submission(id=post_id)
            post.comments.replace_more(limit=0)  # Eliminar comentarios "More" cargados dinámicamente
            print(f"Comentarios del post {post.title}:")
            for comment in post.comments.list():
                print(f"{comment.author}: {comment.body}\n")
        except Exception as e:
            print(f"Error al obtener los comentarios: {e}")

# Uso de la clase
if __name__ == "__main__":
    reddit_extraction = Reddit_extraction()
    
    # Obtener los 10 posts más populares de un subreddit
    reddit_extraction.get_top_posts('python', limit=100000)
    
    # Obtener los comentarios de un post específico (reemplaza 'post_id_here' por un ID real)
    # reddit_extraction.get_comments('post_id_here')
