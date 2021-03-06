#!/usr/bin/python3
''' script that def state'''

if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy.orm import Session
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from model_city import City

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city, state in session.query(
            City, State).filter(
                City.state_id == State.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name,))
    session.close()
