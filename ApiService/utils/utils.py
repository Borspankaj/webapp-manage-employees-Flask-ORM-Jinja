def get_emp_args(parser) :
    parser.add_argument('first_name', type=str, required=True, help='First name cannot be blank')
    parser.add_argument('last_name', type=str, required=True, help='Last name cannot be blank')
    parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
    parser.add_argument('phone_number', type=str, required=True, help='Phone number cannot be blank')
    # parser.add_argument('dob', type=str, required=True, help='Date of birth cannot be blank')
    parser.add_argument('address', type=str, required=True, help='Address cannot be blank')
    args = parser.parse_args()
    return args

