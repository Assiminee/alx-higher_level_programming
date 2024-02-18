#!/usr/bin/python3
"""Fetches data from states table
"""
from model_state import Base, State
from sqlalchemy import create_engine, delete
import sys

if __name__ == "__main__":
    db_connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )

    engine = create_engine(db_connection, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = delete(State).where(State.name.contains('a'))
        conn.execute(query)
        conn.commit()  # Must commit after an update statement

    engine.dispose()
