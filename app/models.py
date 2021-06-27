import datetime
import uuid
from hashlib import sha512

from . import app, db


class LogPost(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    creation_ts = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.datetime.now())
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    is_markdown = db.Column(db.Boolean, nullable=True)

    def __init__(self, title, content, is_markdown=True):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
        self.is_markdown = is_markdown


class User:
    @classmethod
    def authenticate(cls, password):
        cred_file = app.config['CRED_FILE']
        try:
            f = open(cred_file)
            f.close()
        except FileNotFoundError:
            cls.change_password('password')

        with open(cred_file) as f:
            password_r = f.read()
            password_i = sha512(password.encode()).hexdigest()
            if password_r == password_i:
                return True
        return False

    @staticmethod
    def change_password(new_password):
        cred_file = app.config['CRED_FILE']
        with open(cred_file, 'w') as f:
            f.write(sha512(new_password.encode()).hexdigest())
        return True


db.create_all()