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

import json, time
import os
from typing import Any
import hashlib


def save_db(db: dict[str, Any], filename="db.json"):
    with open(filename, "w") as f:
        json.dump(db, f)


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
) -> bool:
    db = load_db(db_filename)

    if email in db["users"]:
        return False  # User already exists

    hash_password_value = hash_password(password)

    db["users"][email] = {
        "password": hash_password_value,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "failed_sign_in_attempts": [],
    }

    save_db(db, db_filename)
    return True

def sign_in_user(email: str, password: str, db_filename="db.json") -> bool:
    db = load_db(db_filename)
    hash_password_value = hash_password(password)

    user = db["users"].get(email)

    # Check if user exists
    if not user:
        return False  # User not found

    # in last 30 second there were 3 or more failed attempts, block sign in
    right_now = int(time.time())
    fail_attempts_within_30_seconds = 0
    for last_attempt in user["failed_sign_in_attempts"]:
        if right_now - last_attempt <= 30:
            fail_attempts_within_30_seconds += 1

    if fail_attempts_within_30_seconds >= 3:
        return False  # Too many failed attempts, block sign in

    # Check password hash matches, If not, log failed attempt and record timestamp
    if user["password"] != hash_password_value:
        user["failed_sign_in_attempts"].append(right_now)
        return False

    return True

while True:
    ui = input("Please type a commandL\nc - Create Account\ns - Sign in\nCommand:").strip().lower()
