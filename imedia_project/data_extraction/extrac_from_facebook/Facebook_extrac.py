# extrac_from_facebook/Facebook_extract.py
import requests
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

class FacebookExtract:
    def __init__(self):
        """Inicializa la clase con las credenciales de la API de Facebook"""
        self.ACCESS_TOKEN = os.getenv('FACEBOOK_TOKEN_CLIENT')
        self.API_URL = 'https://graph.facebook.com/v12.0/'

    def get_page_data(self, page_id, fields='id,name,posts'):
        """Obtiene datos de una página de Facebook"""
        url = f"{self.API_URL}{page_id}"
        params = {
            'access_token': self.ACCESS_TOKEN,
            'fields': fields
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la página: {e}")
            return {}

    def get_post_comments(self, post_id):
        """Obtiene los comentarios de un post específico"""
        url = f"{self.API_URL}{post_id}/comments"
        params = {
            'access_token': self.ACCESS_TOKEN,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los comentarios del post: {e}")
            return {}

    def get_user_posts(self, user_id, limit=5):
        """Obtiene los posts recientes de un usuario"""
        url = f"{self.API_URL}{user_id}/posts"
        params = {
            'access_token': self.ACCESS_TOKEN,
            'limit': limit
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los posts del usuario: {e}")
            return {}

    def get_user_info(self, user_id):
        """Obtiene la información básica de un usuario"""
        url = f"{self.API_URL}{user_id}"
        params = {
            'access_token': self.ACCESS_TOKEN,
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener la información del usuario: {e}")
            return {}

if __name__ == "__main__":
    # Instancia de la clase FacebookExtract
    facebook_extractor = FacebookExtract()

    # Reemplaza con un page_id real de una página de Facebook
    page_id = 'facebook'  # ID de la página de Facebook a consultar, por ejemplo 'facebook' para la página oficial de Facebook

    # Obtener datos de la página
    print("Probando la conexión a la API de Facebook...")
    page_data = facebook_extractor.get_page_data(page_id)
    print("Datos de la página:", page_data)

    # Reemplaza con un user_id real de un usuario de Facebook
    user_id = '4'  # ID de un usuario de prueba, por ejemplo '4' corresponde a Mark Zuckerberg

    # Obtener datos del usuario
    user_info = facebook_extractor.get_user_info(user_id)
    print("Información del usuario:", user_info)
