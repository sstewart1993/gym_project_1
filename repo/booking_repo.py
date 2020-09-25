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

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s,%s) returning id"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id
