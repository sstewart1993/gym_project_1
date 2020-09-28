from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.booking_repo as booking_repo

def delete_all():
    sql = "DELETE from sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        session = Session(result["name"], result["time"], result["date"], result["duration"], result["capacity"], result["id"])
    return session


def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for result in results:
        session = Session(result["name"], result["time"], result["date"], result["duration"], result["capacity"], result["id"])
        sessions.append(session)
    return sessions


def save(session):
    sql = "INSERT INTO sessions (name, time, date, duration, capacity) VALUES (%s,%s,%s,%s,%s) returning * "
    values = [session.name, session.time, session.date, session.duration, session.capacity]
    results = run_sql(sql, values)
    id = results[0]["id"]
    session.id = id
    return session
    

def update(session):
    sql = "UPDATE sessions SET (name, time, date, duration, capacity) = (%s,%s,%s,%s,%s) WHERE id = %s "
    values = [session.name, session.time, session.date, session.duration, session.capacity, session.id]
    print (values)
    run_sql(sql, values)