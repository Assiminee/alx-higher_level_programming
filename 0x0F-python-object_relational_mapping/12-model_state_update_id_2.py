#!/usr/bin/python3
"""Fetches data from states table
"""
from model_state import Base, State
from sqlalchemy import create_engine, update
import sys

if __name__ == "__main__":
    db_connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )

    engine = create_engine(db_connection, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = update(State).where(State.id == 2).values(name='New Mexico')
        conn.execute(query)
        conn.commit()  # Must commit after an update statement

    engine.dispose()
