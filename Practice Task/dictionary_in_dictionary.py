users = {
    'anik':{
    'first' : 'anik',
    'last' : 'sen',
    'location' : 'badda',
    },
    'alok':{
    'first' : 'alok',
    'last' : 'sen',
    'location' : 'sreemangol',
    },
}
for username, user_info in users.items():
    print(f"\n User Name : {username}")
    fullName = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\nFull Name : {fullName.title()}")
    print(f"\nLocation : {location.title()}")