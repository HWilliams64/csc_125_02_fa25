import hashlib

def hash_secret(secret:str) -> str:
    # convert to bytes 1 and 0
    secret_bytes = secret.encode()
    # hash the bytes
    hash_value = hashlib.sha256(secret_bytes)
    # convert the hash bytes to a string
    return hash_value.hexdigest()

def test_password(new_password:str, existing_hash:str):
    new_hash = hash_secret(new_password)
    return new_hash == existing_hash


org_secret="ernnfkjdnkf kdfhb "
username="username"
password="apple"
password_hash = hash_secret(f"{org_secret}:{username}:{password}")
print(password_hash)

while True:
    ui= input("Please type your password:")
    if test_password(ui, password_hash):
        print("Sign success")
    else:
        print("wrong password")
