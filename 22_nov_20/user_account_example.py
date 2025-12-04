# DB Schema
#  {
#    "users": {
#      <user email - string>: {
#        "password": <hashed password - string>,
#        "email": <user email - string>,
#        "first_name": <user firstname - string>,
#        "last_name": <user lastname - string>,
#        "failed_sign_in_attempts": [<timestamp - int>, ...]
#      }
#    }
# }

from ast import Tuple
import json, time
import os
from typing import Any
import hashlib


def save_db(db: dict[str, Any], filename="db.json"):
    with open(filename, "w") as f:
        json.dump(db, f, indent=4, sort_keys=True)


def load_db(filename="db.json") -> dict[str, Any]:
    # Check if file exists if it doesn't, return empty dict
    if not os.path.exists(filename):
        return {"users": {}}

    with open(filename, "r") as f:
        return json.load(f)

def hash_password(password: str) -> str:
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(
    email: str,
    password: str,
    first_name: str,
    last_name: str,
    db_filename="db.json",
) -> tuple[bool, str]:
    db = load_db(db_filename)

    if email in db["users"]:
        return False, "Email already exists"  # User already exists

    hash_password_value = hash_password(password)

    db["users"][email] = {
        "password": hash_password_value,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "failed_sign_in_attempts": [],
    }

    save_db(db, db_filename)
    return True, ""


def sign_in_user(email: str, password: str, db_filename="db.json") -> tuple[bool, str, dict]:
    db = load_db(db_filename)
    hash_password_value = hash_password(password)

    user = db["users"].get(email)

    # Check if user exists
    if not user:
        return False, "User name and password do not match", {}  # User not found

    # in last 30 second there were 3 or more failed attempts, block sign in
    right_now = int(time.time())
    fail_attempts_within_30_seconds = 0
    for last_attempt in user["failed_sign_in_attempts"]:
        if right_now - last_attempt <= 30:
            fail_attempts_within_30_seconds += 1

    if fail_attempts_within_30_seconds >= 3:
        # Too many failed attempts, block sign in
        return False, "Your account has been temporarily locked out. Please try again later.", {}

    # Check password hash matches, If not, log failed attempt and record timestamp
    if user["password"] != hash_password_value:
        user["failed_sign_in_attempts"].append(right_now)
        save_db(db, db_filename)
        return False, "User name and password do not match", {}

    return True, "", user

while True:
    db_filename = "db.json"
    ui = input("Please type a command\nc - Create Account\ns - Sign in\nq - Quit\nCommand: ").strip().lower()

    if ui.lower().strip() in ("c", "s", "q"):
        if ui == "c":
            email = input("Email: ")
            password = input("Password: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            is_success, error_message = create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                db_filename=db_filename,
            )

            if not is_success:
                print(f"Failed to create account. {error_message}")
        elif ui == "s":
            email = input("Email: ")
            password = input("Password: ")
            is_success, error_message, user = sign_in_user(
                email=email,
                password=password,
                db_filename=db_filename,
            )

            if not is_success:
                print(f"Failed to signin. {error_message}")
            else:
                print(f"Welcome {user.get('first_name')}!")

        else:
            break
    else:
        print(f"The option \"{ui}\" is not recognized")
