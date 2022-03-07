from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms import BloodsugarForm
from bs_track.models import Bloodsugar, Action
import math

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
        times.append(sugar.time)
        nums.append(int(sugar.bs))
        acts.append(sugar.act)

    if len(nums == 0):
        num_avg = 0
    else:
        num_avg = math.floor(sum(nums)/len(nums))

    boluses = 0
    carbs = 0
    activities = 0
    others = 0

    for act in acts:
        act = str(act)
        if act == 'bolus':
            boluses += 1
        elif act == 'carb intake':
            carbs += 1
        elif act == 'activity':
            activities += 1
        else:
            others += 1
    
    return render_template("index.html", all_bs=all_bs, times=times, nums=nums, acts=acts, num_avg=num_avg, boluses=boluses, carbs=carbs, activities=activities, others=others  )