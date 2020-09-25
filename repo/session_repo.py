from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.booking_repo as booking_repo

def delete_all():
    sql = "DELETE from booking"
    run_sql(sql)

def save(session):
    sql = "INSERT INTO sessions (name, time, date, duration, capacity) VALUES (%s,%s,%s,%s,%s) returning id"
    values = [session.name, session.time, session.date, session.duration, session.capacity]
    results = run_sql(sql, values)
    id = results[0]["id"]
    session.id = id