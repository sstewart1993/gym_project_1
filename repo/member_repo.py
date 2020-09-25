from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.instructor_repo as instructor_repo
import repo.booking_repo as booking_repo
import repo.session_repo as session_repo

def delete_all():
    sql = "DELETE from booking"
    run_sql(sql)

def save(member):
    sql = "INSERT INTO members (name, age, gender, level) VALUES (%s,%s,%s,%s) returning id"
    values = [member.name, member.age, member.gender, member.level]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id