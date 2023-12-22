from app.database import LocalSession
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

session = LocalSession()

try:
    result = session.execute(text("SELECT version();"))
    for row in result:
        print(f"Database connected {row}")
except SQLAlchemyError as e:
    print(f"Error occurred: {e}")
finally:
    session.close()