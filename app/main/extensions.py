from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID as db_UUID

db = SQLAlchemy(session_options=dict(expire_on_commit=False))
bcrypt = Bcrypt()
Column = db.Column
