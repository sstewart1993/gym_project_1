import pdb

from models.booking import Booking
import repo.booking_repo as booking_repo

from models.instructor import Instructor
import repo.instructor_repo as instructor_repo

from models.member import Member
import repo.member_repo as member_repo

from models.session import Session
import repo.session_repo as session_repo


# member_repo.delete_all()
# session_repo.delete_all()
# booking_repo.delete_all()
# instructor_repo.delete_all()



member1 = Member("Joe", 19, "male")
member_repo.save(member1)
member2 = Member("Sally", 67, "female")
member_repo.save(member2)
member3 = Member("Jamie", 37, "female")
member_repo.save(member3)

session1 = Session("spin", "18:45", "Monday", 45, 12)
session_repo.save(session1)
session2 = Session("core", "12:15", "Wednesday", 30, 9)
session_repo.save(session2)

booking1 = Booking(member1, session1)
# booking_repo.save(booking1)
booking2 = Booking(member3, session2)
# booking_repo.save(booking2)

instructor1 = Instructor("Peter La Fleur", session1, member1)
# instructor_repo.save(instructor1)
instructor2 = Instructor("White Goodman", session2, member2)
# instructor_repo.save(instructor2)

# print (booking2)
# print(member1)
# print(instructor1)
# print(session1)
# john = member_repo.select_all()
# print (john)



# pdb.set_trace()