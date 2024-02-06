import requests
from flask import session
from flask_jwt_extended import get_jwt_identity
class AuthService:
    @staticmethod
    def authenticate(email, password):
       
        api_url = "http://127.0.0.1:4000/api/login"
        payload = {"email": email, "password": password}

        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                token = response.headers.get('Authorization')
                session['token'] = token
                session['user'] = email 
                print(response_data)
                session['role'] = response_data['user']['role']
                return True
            
            else:
                return False
        except requests.RequestException as e:
            print(f"Error during authentication API request: {e}")
            return False