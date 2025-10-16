import hashlib

db = {
    "icecream": {
        "username": "icecream",
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "first_name":"tony",
        "last_name":"stark"
    }
}


while True:
    user_name = input("Username:")
    password =input("Password")

    user = db.get(user_name, None)

    if not user:
        print("Username and password do not match")
    else:
        internal_pass_hash = user["password"]
        external_pass_hash = hashlib.sha256(password.encode()).hexdigest()
        if internal_pass_hash == external_pass_hash:
            print(f"Welcome {user['first_name']} {user['last_name']}")
        else:
            print("Username and password do not match")
