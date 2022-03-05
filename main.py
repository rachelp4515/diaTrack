from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms import BloodsugarForm
from bs_track.models import Bloodsugar, Action

from bs_track.extensions import app, db

routes = Blueprint("main", __name__)


@routes.route("/")
def index():
    all_bs = Bloodsugar.query.all()
    acts = Action.query.all()
    
    times = []
    nums = []
    acts = []
    for sugar in all_bs:
        times.append(float(sugar.time))
        nums.append(int(sugar.bs))
        acts.append(sugar.act)

    return render_template("index.html", all_bs=all_bs, times=times, nums=nums, last=nums[-1], lasttime=times[-1], lastact=acts[-1] )