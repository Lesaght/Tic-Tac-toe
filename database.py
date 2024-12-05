import sqlite3
import hashlib
import os
from typing import Optional, Tuple

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.create_tables()
        
    def create_tables(self):
        cursor = self.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0,
                ties INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()
        
    def cursor(self):
        return self.conn.cursor()
        
    def hash_password(self, password: str) -> str:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        return salt.hex() + ':' + key.hex()
        
    def verify_password(self, stored_password: str, provided_password: str) -> bool:
        salt_hex, key_hex = stored_password.split(':')
        salt = bytes.fromhex(salt_hex)
        stored_key = bytes.fromhex(key_hex)
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            provided_password.encode('utf-8'),
            salt,
            100000
        )
        return stored_key == new_key
        
    def register_user(self, username: str, password: str) -> Tuple[bool, str]:
        try:
            cursor = self.cursor()
            hashed_password = self.hash_password(password)
            cursor.execute(
                'INSERT INTO users (username, password) VALUES (?, ?)',
                (username, hashed_password)
            )
            self.conn.commit()
            return True, "Registration successful!"
        except sqlite3.IntegrityError:
            return False, "Username already exists!"
        except Exception as e:
            return False, f"Registration failed: {str(e)}"
            
    def login_user(self, username: str, password: str) -> Tuple[bool, str]:
        cursor = self.cursor()
        cursor.execute(
            'SELECT password FROM users WHERE username = ?',
            (username,)
        )
        result = cursor.fetchone()
        
        if not result:
            return False, "User not found!"
            
        stored_password = result[0]
        if self.verify_password(stored_password, password):
            return True, "Login successful!"
        return False, "Incorrect password!"
        
    def update_stats(self, username: str, result: str):
        cursor = self.cursor()
        if result == "win":
            cursor.execute(
                'UPDATE users SET wins = wins + 1 WHERE username = ?',
                (username,)
            )
        elif result == "loss":
            cursor.execute(
                'UPDATE users SET losses = losses + 1 WHERE username = ?',
                (username,)
            )
        else:
            cursor.execute(
                'UPDATE users SET ties = ties + 1 WHERE username = ?',
                (username,)
            )
        self.conn.commit()
        
    def get_stats(self, username: str) -> Optional[Tuple[int, int, int]]:
        cursor = self.cursor()
        cursor.execute(
            'SELECT wins, losses, ties FROM users WHERE username = ?',
            (username,)
        )
        result = cursor.fetchone()
        return result if result else None