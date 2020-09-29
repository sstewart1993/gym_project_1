from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.instructor_repo as instructor_repo
import repo.booking_repo as booking_repo
import repo.session_repo as session_repo

def delete_all():
    sql = "DELETE from members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result["name"], result["age"], result["gender"], result["level"], result["id"])
    return member 

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result["age"], result["gender"], result["level"], result["id"])
        members.append(member)
    return members


def save(member):
    sql = "INSERT INTO members (name, age, gender, level) VALUES (%s,%s,%s,%s) returning *"
    values = [member.name, member.age, member.gender, member.level]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id
    return member 


def update(member):
    sql = "UPDATE members SET (name, age, gender, level) = (%s, %s, %s, %s) WHERE id = %s "
    values = [member.name, member.age, member.gender, member.level, member.id]
    run_sql(sql, values)
