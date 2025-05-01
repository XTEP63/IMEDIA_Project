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
            # Obtener los posts más populares del subreddit (últimos 24 horas por defecto)
            top_posts = self.reddit.subreddit(subreddit).top(limit=limit, time_filter='day')
            
            top_posts_list = []
            for post in top_posts:
                top_posts_list.append({
                    'title': post.title,
                    'score': post.score,
                    'url': post.url
                })
                print(f"Title: {post.title}")
                print(f"Score: {post.score}")
                print(f"URL: {post.url}\n")

            return top_posts_list  # Devolvemos la lista de posts
        except Exception as e:
            print(f"Error al obtener los posts recientes: {e}")
            return []  # Retornamos una lista vacía en caso de error
 
    def get_top_posts_all_time(self, subreddit, limit=10):
        """Obtener los posts más destacados de todos los tiempos de un subreddit"""
        try:
            # Usamos el filtro "all" para obtener los posts de todos los tiempos
            top_posts = self.reddit.subreddit(subreddit).top(limit=limit, time_filter='all')
            
            top_posts_list = []
            for post in top_posts:
                top_posts_list.append({
                    'title': post.title,
                    'score': post.score,
                    'url': post.url
                })
                print(f"Title: {post.title}")
                print(f"Score: {post.score}")
                print(f"URL: {post.url}\n")

            return top_posts_list  # Devolvemos la lista de posts
        except Exception as e:
            print(f"Error al obtener los posts top: {e}")
            return []  # Retornamos una lista vacía en caso de error
 
    def get_comments(self, post_id):
        """Obtener los comentarios de un post específico"""
        
        if not post_id:
            print("Post ID no válido.")
            return []

        try:
            # Obtener un post usando su ID
            post = self.reddit.submission(id=post_id)
            post.comments.replace_more(limit=0)  # Eliminar comentarios "More" cargados dinámicamente

            # Verificar si el post tiene comentarios antes de iterar
            if not post.comments:
                print(f"No hay comentarios en el post {post_id}.")
                return []
            
            return [{'author': comment.author.name, 'body': comment.body} for comment in post.comments.list()]
        except Exception as e:
            print(f"Error al obtener los comentarios: {e}")
            return []
 
    def search_reddit(self, query, limit=10):
        """Buscar publicaciones en Reddit por un término específico"""
        try:
            # Mejorar la búsqueda para que busque dentro de un subreddit específico, si es necesario
            results = self.reddit.subreddit('all').search(query, limit=limit)
            
            # Verificar que se encontraron resultados
            if results:
                return [{'title': post.title, 'score': post.score, 'url': post.url} for post in results]
            else:
                print(f"No se encontraron posts relacionados con '{query}'.")
                return []
        except Exception as e:
            print(f"Error al buscar en Reddit: {e}")
            return []
 
    def get_user_subscriptions(self, username, limit=10):
        """Obtener los subreddits a los que un usuario ha publicado en los últimos 'limit' posts"""
        try:
            user = self.reddit.redditor(username)
            print(f"Obteniendo los subreddits a los que {username} ha publicado en sus últimos {limit} posts:")

            # Obtener las publicaciones recientes del usuario
            user_subreddits = set()  # Usamos un set para evitar duplicados
            for submission in user.submissions.new(limit=limit):
                subreddit_name = submission.subreddit.display_name
                user_subreddits.add(subreddit_name)  # Agregar el subreddit al set
                print(f"Subreddit: {subreddit_name}")

            # Convertir el set a lista antes de devolverlo
            return list(user_subreddits)

        except Exception as e:
            print(f"Error al obtener las suscripciones del usuario: {e}")
            return []
 
    def get_recent_comments(self, subreddit, limit=10):
        """Obtener los comentarios más recientes de un subreddit"""
        try:
            comments = self.reddit.subreddit(subreddit).comments(limit=limit)
            comments_list = []
            print(f"Últimos {limit} comentarios de r/{subreddit}:")
            for comment in comments:
                comments_list.append({'author': comment.author.name, 'body': comment.body})
                print(f"Author: {comment.author}")
                print(f"Comment: {comment.body}\n")
            return comments_list  # Devolver los comentarios como lista
        except Exception as e:
            print(f"Error al obtener los comentarios recientes: {e}")
            return []  # Retornar una lista vacía si ocurre un error
 
    def get_subreddit_info(self, subreddit):
        """Obtener detalles de un subreddit"""
        try:
            sub = self.reddit.subreddit(subreddit)
            subreddit_info = {
                'name': sub.display_name,
                'subscribers': sub.subscribers,
                'description': sub.public_description
            }
            print(f"Información de r/{subreddit}:")
            print(f"Name: {subreddit_info['name']}")
            print(f"Subscribers: {subreddit_info['subscribers']}")
            print(f"Description: {subreddit_info['description']}")
            return subreddit_info  # Devolver los detalles del subreddit como un diccionario
        except Exception as e:
            print(f"Error al obtener la información del subreddit: {e}")
            return {}  # Retornar un diccionario vacío si ocurre un error
 
    def get_trending_subreddits(self, limit):
        """Obtiene una lista de los subreddits más populares actualmente"""
        trending_subreddits = []
        for submission in self.reddit.subreddit('all').top(limit=limit):
            trending_subreddits.append(submission.subreddit.display_name)
        return trending_subreddits
 
# Uso de la clase
if __name__ == "__main__":
    reddit_extraction = Reddit_extraction()
    
    # # Obtener los 10 posts más populares de un subreddit
    # reddit_extraction.get_top_posts('python', limit=10)
    # print('---------------------------------------------------------------')
    # # Ejemplo de uso para buscar posts relacionados con "python" en Reddit
    # reddit_extraction.search_reddit('python', limit=10)
    # print('---------------------------------------------------------------')
    # # Ejemplo de uso para obtener los 5 posts más destacados de todos los tiempos de un subreddit
    # reddit_extraction.get_top_posts_all_time('python', limit=5)
    # print('---------------------------------------------------------------')
    # # Ejemplo de uso para obtener las suscripciones de un usuario
    # reddit_extraction.get_user_subscriptions('ManvilleJ')  # Reemplaza con el nombre de usuario real
    # print('---------------------------------------------------------------')
    # # Ejemplo de uso para obtener los 5 comentarios más recientes de un subreddit
    # reddit_extraction.get_recent_comments('python', limit=5)
    # print('---------------------------------------------------------------')
    # # Ejemplo de uso para obtener la información de un subreddit específico
    # reddit_extraction.get_subreddit_info('python')
    # print('---------------------------------------------------------------')
    # # Obtener los comentarios de un post específico (reemplaza 'post_id_here' por un ID real)
    # reddit_extraction.get_comments('hoolsm')
    
    trending_subreddits = reddit_extraction.get_trending_subreddits(1000*4)
    trending_subreddits = set(trending_subreddits)
    print(len(trending_subreddits))
    print(f"Subreddits en tendencia: {trending_subreddits}")
