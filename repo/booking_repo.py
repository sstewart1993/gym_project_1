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
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = member_repo.select(result["member_id"])
        session = session_repo.select(result["session_id"])
        booking = Booking(member, session, result["id"])
    return booking 

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results: 
        member = member_repo.select(result["member_id"])
        session = session_repo.select(result["session_id"])
        booking = Booking(member, session, result["id"])
        bookings.append(booking)
    return bookings


def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s,%s) returning *"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id
    return booking

def update(booking):
    sql = "UPDATE bookings SET (member_id, session_id) = (%s,%s) WHERE id = %s"
    values = [booking.member.id, booking.session.id, booking.id]
    run_sql(sql, values)

# return all the sessions the member has booked



