#!/usr/bin/python3
"""Fetches data from states table
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select
import sys

if __name__ == "__main__":
    db_connection = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )

    engine = create_engine(db_connection, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = select(State.name, City.id, City.name)\
                .where(State.id == City.state_id)\
                .order_by(City.id)
        results = conn.execute(query).fetchall()

        for result in results:
            print(f"{result[0]}: ({result[1]}) {result[2]}")

    engine.dispose()
