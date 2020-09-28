from db.run_sql import run_sql
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.session import Session
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

def delete_all():
    sql = "DELETE from bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = ["id"]
    result = run_sql(sql, values)[0]
    booking = Booking(result["member_id"], result["session_id"])
    return booking 

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results: 
        booking = Booking(result["member_id"], result["session_id"])
        bookings.append(booking)
    return bookings


def save(booking):
    sql = "INSERT INTO bookings (members_id, sessions_id) VALUES (%s,%s) returning id"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id

def update(booking):
    sql = "UPDATE bookings SET (member_id, session_id, id) = (%s,%s,%s) WHERE id = %s"
    values = [booking.member.id, booking.seesion.id, booking.id]
    run_sql(sql, values)

# return all the sessions the member has booked

# def sessions(member):
#     sessions = []

#     sql = "SELECT sessions.* FROM sessions INNER JOIN members ON members.session_id = session.id WHERE member_id = %s"
#     values = [member.id]
#     results = run_sql(sql, values)

#     for row in results:
#         session = Session(row["name"], row["time"], row["date"], row["duration"], row["capacity"])
#         sessions.append(session)
#     return sessions
