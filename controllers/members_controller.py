from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repo.booking_repo as booking_repo
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/new")
def new_members():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    level = request.form["level"]
    new_member = Member(name, age, level, gender)
    member_repo.save(new_member)
    return redirect("/members")


# EDIT
@members_blueprint.route("/members/<id>/edit", methods = ["GET"])
def edit_member(id):
    member = member_repo.select(id)
    return render_template('members/edit.html', member=member)


# UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    level = request.form["level"]
    member = Member(name, age, gender, level, id)
    member_repo.update(member)
    return redirect("/members")


# DELETE
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repo.delete(id)
    return redirect("/members")