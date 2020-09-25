from flask import Blueprint, Flask, redirect, render_template, request

from models.instructor import Instructor
import repo.booking_repo as booking_repo
import repo.instructor_repo as instructor_repo
import repo.member_repo as member_repo
import repo.session_repo as session_repo

instructors_blueprint = Blueprint("instructors", __name__)