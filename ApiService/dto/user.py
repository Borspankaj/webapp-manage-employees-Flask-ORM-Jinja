class UserDto :
    def get_user_data(user) :
        return {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone_number': user.phone_number,
                # 'dob': employee.dob,
                'address': user.address
            }