from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.booking_repo as booking_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

def delete_all():
    sql = "DELETE from instructors"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM instructors WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql ="SELECT * FROM instructors WHERE id =%s"
    values = ["id"]
    result = run_sql(sql, values)[0]
    instructor = Instructor(result["name"], result["member_id"], result["session_id"])
    return instructor

def select_all():
    instructors = []
    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    for result in results:
        instructor = Instructor(result["name"], result["member_id"], result["session_id"])
        instructors.append(instructor)
    return instructors

def save(instructor):
    sql = "INSERT INTO instructors (name, member_id, session_id) VALUES (%s,%s,%s) RETURNING id"
    values = [instructor.name, instructor.member.id, instructor.session.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    instructor.id = id

def update(instructor):
    sql = "UPDATE instructors SET (name, member_id, session_id, id) = (%s,%s,%s,%s) WHERE id = %s"
    values = [instructor.name, instructor.member.id, instructor.session.id, instructor.id]
    run_sql(sql, values)

# return all the instructors that share members and sessions
# come back and work this out later

# def instructors(member):
#     instructors = []

#     sql = "SELECT sessions.* FROM sessions INNER JOIN members ON members.session_id = session.id WHERE member_id = %s"
#     values = [member.id]
#     results = run_sql(sql, values)

#     for row in results:
#         session = Session(row["name"], row["time"], row["date"], row["duration"], row["capacity"])
#         sessions.append(session)
#     return sessions










