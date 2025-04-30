import tweepy
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

class X_extraction:
    
    def __init__(self):
        """Inicializa la clase con las credenciales de la API V2."""
        
        # Obtener las credenciales desde las variables de entorno
        self.BEARER_TOKEN = os.getenv('BEARER_TOKEN')
        
        # Inicializar el cliente para la API V2
        self.client = tweepy.Client(bearer_token=self.BEARER_TOKEN)

    def search_tweets(self, hashtag, max_results):
        """Buscar tweets por hashtag usando la API V2"""
        
        try:
            # Buscar tweets con un hashtag usando la API V2
            tweets = self.client.search_recent_tweets(query=hashtag, max_results=max_results)  # max_results es el límite de tweets a obtener

            if tweets.data:
                print(f"Resultados para el hashtag '{hashtag}' usando la API V2:")
                for tweet in tweets.data:
                    print(f"{tweet.text}\n")
            else:
                print("No se encontraron tweets con ese hashtag.")
        except Exception as e:
            print(f"Error al acceder a la API de Twitter (V2): {e}")
            
    def search_tweets_from_user(self, username, max_results):
        """Buscar tweets de un usuario específico usando la API V2"""
        
        try:
            # Buscar tweets de un usuario específico
            tweets = self.client.search_recent_tweets(query=f"from:{username}", max_results=max_results)

            if tweets.data:
                print(f"Tweets de {username} usando la API V2:")
                for tweet in tweets.data:
                    print(f"{tweet.text}\n")
            else:
                print(f"No se encontraron tweets de {username}.")
        except Exception as e:
            print(f"Error al acceder a la API de Twitter (V2): {e}")
    
    def get_tweet_details(self, tweet_id):
        """Obtener detalles de un tweet específico usando la API V2"""
        
        try:
            tweet = self.client.get_tweet(tweet_id)
            if tweet.data:
                print(f"Detalles del tweet con ID {tweet_id}:")
                print(f"Texto: {tweet.data['text']}")
                print(f"Creado en: {tweet.data['created_at']}")
            else:
                print(f"No se encontró el tweet con ID {tweet_id}.")
        except Exception as e:
            print(f"Error al obtener detalles del tweet: {e}")

    def get_user_details(self, username):
        """Obtener detalles de un usuario específico usando la API V2"""
        
        try:
            user = self.client.get_user(username=username)
            if user.data:
                print(f"Detalles del usuario {username}:")
                print(f"Nombre: {user.data['name']}")
                print(f"Usuario: {user.data['username']}")
                print(f"Descripción: {user.data['description']}")
                print(f"Ubicación: {user.data['location']}")
                print(f"Seguidores: {user.data['public_metrics']['followers_count']}")
            else:
                print(f"No se encontró el usuario {username}.")
        except Exception as e:
            print(f"Error al obtener detalles del usuario: {e}")

    def get_user_followers(self, user_id, max_results):
        """Obtener la lista de seguidores de un usuario usando la API V2"""
        
        try:
            followers = self.client.get_users_followers(id=user_id, max_results=max_results)
            if followers.data:
                print(f"Seguidores del usuario con ID {user_id}:")
                for follower in followers.data:
                    print(f"{follower.username}")
            else:
                print(f"No se encontraron seguidores para el usuario con ID {user_id}.")
        except Exception as e:
            print(f"Error al obtener los seguidores del usuario: {e}")

    def get_user_following(self, user_id, max_results):
        """Obtener la lista de usuarios que sigue una cuenta usando la API V2"""
        
        try:
            following = self.client.get_users_following(id=user_id, max_results=max_results)
            if following.data:
                print(f"Usuarios que sigue el usuario con ID {user_id}:")
                for person in following.data:
                    print(f"{person.username}")
            else:
                print(f"No se encontraron usuarios que sigue el usuario con ID {user_id}.")
        except Exception as e:
            print(f"Error al obtener las cuentas que sigue el usuario: {e}")

    def get_mentions(self, username, max_results):
        """Obtener las menciones de un usuario usando la API V2"""
        
        try:
            mentions = self.client.search_recent_tweets(query=f"to:{username}", max_results=max_results)
            if mentions.data:
                print(f"Menciones al usuario {username}:")
                for mention in mentions.data:
                    print(f"{mention.text}\n")
            else:
                print(f"No se encontraron menciones para {username}.")
        except Exception as e:
            print(f"Error al obtener las menciones del usuario: {e}")

    def get_media_from_tweet(self, tweet_id):
        """Obtener los medios asociados a un tweet usando la API V2"""
        
        try:
            tweet = self.client.get_tweet(tweet_id, tweet_fields=["attachments"])
            if tweet.data and "attachments" in tweet.data:
                media_keys = tweet.data["attachments"]["media_keys"]
                print(f"Medios asociados al tweet con ID {tweet_id}:")
                print(f"Media keys: {media_keys}")
            else:
                print(f"No se encontraron medios asociados al tweet con ID {tweet_id}.")
        except Exception as e:
            print(f"Error al obtener los medios del tweet: {e}")
        
    
if __name__ == "__main__":
    # Inicializar la clase
    x_extraction = X_extraction()  
    
    hashtag = "#hello"  
    max_results = 100  
    x_extraction.search_tweets(hashtag, max_results)
    
    # Buscar tweets de un usuario específico
    x_extraction.search_tweets_from_user("MarshallFaulk69", 10)

    # Obtener detalles de un tweet específico
    # x_extraction.get_tweet_details("tweet_id_here")
    
    # Obtener detalles de un usuario específico
    x_extraction.get_user_details("MarshallFaulk69")
    
    # Obtener seguidores de un usuario
    # x_extraction.get_user_followers("user_id_here", 5)
    
    # Obtener usuarios que sigue una cuenta
    # x_extraction.get_user_following("user_id_here", 5)
    
    # Obtener menciones de un usuario
    x_extraction.get_mentions("MarshallFaulk69", 10)
    
    # Obtener medios asociados a un tweet
    # x_extraction.get_media_from_tweet("tweet_id_here")

