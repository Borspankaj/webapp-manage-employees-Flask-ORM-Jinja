from dto.user import UserDto
from models.user import User
class AuthService :
    
    def authenticate(request_data) :
        try :
            user_email = request_data['email']
            user = User.query.filter_by(email = user_email).first()
            return user.check_password(request_data['password']) 
        except Exception as e :
            return  None


        
