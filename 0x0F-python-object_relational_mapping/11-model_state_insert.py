#!/usr/bin/python3
"""Fetches data from states table
"""
from model_state import Base, State
from sqlalchemy import create_engine, select, insert
import sys

if __name__ == "__main__":
    db_connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )

    engine = create_engine(db_connection, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = insert(State).values(name='Louisiana')
        conn.execute(query)
        conn.commit()  # Must commit after an insert

        query = select(State.id).where(State.name == 'Louisiana')
        state_id = conn.execute(query).first()[0]
        print(state_id)

    engine.dispose()
