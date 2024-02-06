from models.user import User
from extensions import db
from dto.user import UserDto as ud

class UserService :
    def get_employees() :
        try:
            users = User.query.all()
            user_data_list = [ud.get_user_data(user) for user in users if user.role == 'EMP']
            return user_data_list
        except Exception as e:
            print(f"Error: {e}")
            return []
       
    def search_employees(keyword) :
        try :
            users = User.query.all() 
            user_data_list = [ud.get_user_data(user) for user in users if user.role == 'EMP' and 
            ( user.first_name == keyword or 
             user.last_name == keyword or
             keyword in user.address ) ]
            return user_data_list
        except Exception as e :
            print(e)
            return []
        
    def get_user(user_email) :
        try :
            user = User.query.filter_by(email = user_email).first()
            return ud.get_user_data(user)
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def create_user(request_data) :
        new_user = User(
            first_name = request_data["first_name"] ,
            last_name=request_data['last_name'],
            email=request_data['email'],
            phone_number=request_data['phone_number'],
            # dob=datetime.strptime(args['dob'], '%Y-%m-%d').date(),
            address=request_data['address'],
            role = request_data['role'] if request_data['role'] == 'ADMIN' else 'EMP', 
        )
        new_user.set_password(request_data['password'])
        try :
            db.session.add(new_user)
            db.session.commit()
        except :
            print("---------")
            db.session.rollback()
            raise
        return ud.get_user_data(new_user)

    def update_user(request_data , user_email):
        
        user = User.query.filter_by(email = user_email).first()
        if user == None:
            return None
        
        user.first_name = request_data['first_name']
        user.last_name = request_data['last_name']
        user.email = user_email
        user.phone_number = request_data['phone_number']
        # employee.dob = datetime.strptime(args['dob'], '%Y-%m-%d').date()
        user.address = request_data['address']
        user.role = request_data['role']
        try :
            db.session.commit()
        except :
            db.session.rollback()
            raise
        return ud.get_user_data(user)
    
    def delete_user(user_email) :
        user = User.query.filter_by(email = user_email).first()
        if user:
            user_data = ud.get_user_data(user)
            try :
                db.session.delete(user)
                db.session.commit()
            except :
                db.session.rollback() 
                raise
            return user_data
        return None