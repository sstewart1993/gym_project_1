from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.booking_repo as booking_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

def delete_all():
    sql = "DELETE from booking"
    run_sql(sql)

def save(instructor):
    sql = "INSERT INTO instructors (name, sessions_id, members_id) VALUES (%s,%s,%s) returning id"
    values = [instructor.name, instructor.session.id, instructor.member.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    instructor.id = id