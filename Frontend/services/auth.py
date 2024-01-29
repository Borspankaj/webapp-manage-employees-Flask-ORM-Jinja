import requests

class AuthService:
    @staticmethod
    def authenticate(email, password):
       
        api_url = "https://your-authentication-api.com/authenticate"
        payload = {"email": email, "password": password}

        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.RequestException as e:
            print(f"Error during authentication API request: {e}")
            return False