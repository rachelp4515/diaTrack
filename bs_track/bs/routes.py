from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from forms import BloodsugarForm
from bs_track.models import Bloodsugar, Action

from bs_track.extensions import app, db

routes = Blueprint("bs", __name__)

# --------------------------------- /


@routes.route('/bs')
def index():
    all_bs = Bloodsugar.query.all()
    acts = Action.query.all()
    return render_template('all_bs.html', all_bs=all_bs, acts=acts)

# --------------------------------- / new


@routes.route('/bs/new', methods=["GET", "POST"])
@login_required
def new_bs():
    form = BloodsugarForm()
    if form.validate_on_submit():
        new_bs = Bloodsugar(
            bs=form.bs.data, time=form.time.data, act=form.action.data, created_by=current_user
        )
        db.session.add(new_bs)
        db.session.commit()
        return redirect(url_for('bs.index', bs_id=new_bs.id))
    return render_template('bs_new.html', form=form)

# --------------------------------- / detail + edit form


@routes.route('/bs/<bs_id>', methods=['GET', 'POST'])
@login_required
def detail(bs_id):
    bs = Bloodsugar.query.get(bs_id)
    form = BloodsugarForm(obj=bs)
    if form.validate_on_submit():
        form.populate_obj(bs)
        db.session.commit()
        return redirect(url_for('bs.index', bs=bs, form=form, bs_id=bs_id))

    return render_template('bs_detail.html', bs=bs, form=form)


# --------------------------------- / delete
@routes.route('/bs/delete/<bs_id>', methods=['POST'])
@login_required
def delete(bs_id):
    bs = Bloodsugar.query.get(bs_id)
    '''
    actions = Action.query.filter_by(bs=bs)
    for action in bs:
        db.session.delete(action) --> maybe keep the actions and just get rid of the bs?
    '''
    db.session.delete(bs)
    db.session.commit()
    return redirect(url_for('bs.index', bs_id=bs_id))
