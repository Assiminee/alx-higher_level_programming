#!/usr/bin/python3
"""Fetches data from states table
"""
from model_state import Base, State
from sqlalchemy import create_engine, select
import sys

if __name__ == "__main__":
    db_connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )

    engine = create_engine(db_connection, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    user_input = sys.argv[4]

    with engine.connect() as conn:
        query = select(State).where(State.name == user_input)
        state = conn.execute(query).first()
        print(state.id) if state else print("Not found")

    engine.dispose()
