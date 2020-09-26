from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repo.booking_repo as booking_repo
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repo.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/new")
def new_bookings():
    return render_template("/bookings/new.html")

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member = member_repo.select(id)
    session = session_repo.select(id)
    new_booking = Booking(member, session)
    booking_repo.save(new_booking)
    return redirect("/bookings")


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repo.select(id)
    return render_template('bookings/edit.html', booking=booking)


# # UPDATE
# @bookings_blueprint.route("/bookings/<id>", methods=["POST"])
# def update_booking(id):
#     member = member_repo.select(id)
#     session = session_repo.select(id)
#     booking = Booking(member, session)
#     booking_repo.update(booking)
#     return redirect("/bookings")


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repo.delete(id)
    return redirect("/bookings")