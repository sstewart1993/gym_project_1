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