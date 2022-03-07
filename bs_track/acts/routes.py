from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms import ActionForm, BloodsugarForm
from bs_track.models import Bloodsugar, Action

from bs_track.extensions import app, db

routes = Blueprint("acts", __name__)

#--------------------------------- /

@routes.route('/acts')
def index():
    bs = Bloodsugar.query.all()
    actions = Action.query.all()
    return render_template('all_act.html', bs=bs, actions=actions)

#--------------------------------- / new

@routes.route('/acts/new', methods=["GET", "POST"])
@login_required
def new_act():
    form =ActionForm()
    if form.validate_on_submit():
        new_act = Action(
            act_type=form.act_type.data,
             time=form.time.data, 
             notes= form.notes.data,
             created_by=current_user
        )
        db.session.add(new_act)
        db.session.commit()
        return redirect(url_for('acts.index', act_id=new_act.id))
    return render_template('act_new.html', form=form)

#--------------------------------- / detail + edit form
@routes.route('/acts/<act_id>', methods=['GET', 'POST'])
@login_required
def detail(act_id):
    act = Action.query.get(act_id)
    form = ActionForm(obj=act)
    if form.validate_on_submit():
        form.populate_obj(act)
        db.session.commit()
        return redirect(url_for('acts.index', act=act, form=form, act_id=act_id))
    return render_template('act_detail.html', act=act, form=form)



#--------------------------------- / delete
@routes.route('/acts/delete/<act_id>', methods=['POST'])
@login_required
def delete(act_id):
    act = Action.query.get(act_id)
    '''
    actions = Action.query.filter_by(bs=bs)
    for action in bs:
        db.session.delete(action) --> maybe keep the actions and just get rid of the bs?
    '''
    db.session.delete(act)
    db.session.commit()
    return redirect(url_for('acts.index', act_id=act_id))