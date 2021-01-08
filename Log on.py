import requests


login_url = 'https://api.login.wheniwork.com/login'
auth_creds = {
    "email": "cool@gmail.com",
    "password": "nicePasssowrd"
}
clock_in_url = 'https://app.wheniwork.com/rest/times/clockin'
get_info_url = 'https://api.wheniwork.com/2/login?show_pending=true'

##This is what a login payload looks like
##{"id":35926763,"accuracy":false,"coordinates":false,"notes":"lol","location_id":4580589}
### i need the ID from the login request


s = requests.Session()

clockin_creds = s.post(login_url,json=auth_creds).text
clockin_creds = clockin_creds.replace('[','')
clockin_creds = clockin_creds.replace('{','')
clockin_creds = clockin_creds.replace(',',' ')
clockin_creds = clockin_creds.replace(':',' ')


user_id = clockin_creds.split()
user_id = user_id[2]
user_id = user_id.replace('"','')
print(user_id)

Token_finder = len(user_id)
Token_finder =- 1
token = clockin_creds.split()
token = token[Token_finder]
token = token.replace('"','')
token = token.replace('}','')
print(token)


clock_in_data = {"id":user_id,
                 "accuracy":'false',
                 "coordinates":'false',
                 "location_id":'4580589'}

Header = {'Authorization':token,'W-Token':token,'W-UserId': 'undefined'}
s.post(login_url,json=auth_creds).text
print(s.cookies)
print(s.get(get_info_url,headers=Header).text)
print(s.cookies.get_dict())
s.get('https://app.wheniwork.com/')
print(s.cookies.get_dict())
print(s.post(clock_in_url,json=clock_in_data).text)
print(s.cookies.get_dict())
