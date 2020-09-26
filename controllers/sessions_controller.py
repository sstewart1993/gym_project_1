from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repo.booking_repo as booking_repo
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repo.select_all()
    return render_template("sessions/index.html", sessions=sessions)

@sessions_blueprint.route("/sessions/new")
def new_session():
    return render_template("/sessions/new.html")


@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    time = request.form["time"]
    date = request.form["date"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    new_session = Session(name, time, date, duration, capacity)
    session_repo.save(new_session)
    return redirect("/sessions")

# EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repo.select(id)
    return render_template('sessions/edit.html', session=session)


# UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    time = request.form["time"]
    date = request.form["date"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    session = Session(name, time, date, duration, capacity, id)
    session_repo.update(session)
    return redirect("/session")


# DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repo.delete(id)
    return redirect("/sessions")