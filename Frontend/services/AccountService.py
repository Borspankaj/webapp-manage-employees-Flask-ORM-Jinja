from flask import session
import requests
class AccountService :
    @staticmethod
    def logout() :
        user_email = session['user']
        api_url = 'http://127.0.0.1:4000/api/login/' + user_email
        headers = {'Authorization':session['token']}
        response = requests.get(api_url , headers= headers)
        if response.status_code == 200 : 
            session.clear()
            return True
        return False