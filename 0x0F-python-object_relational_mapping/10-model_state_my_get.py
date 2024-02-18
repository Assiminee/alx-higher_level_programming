#!/usr/bin/python3
"""Fetches data from states table
"""
from model_state import Base, State
from sqlalchemy import asc, func
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.sql import bindparam
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    con = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2],
                                                      sys.argv[3])
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    user_input = sys.argv[4]

    with engine.connect() as conn:
        query = select(State.id).where(State.name == user_input)
        state_id = conn.execute(query).fetchone()[0]
        print(state_id) if state_id else print("Not found")

    engine.dispose()
