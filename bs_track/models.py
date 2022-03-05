
from bs_track.extensions import db
from bs_track.utils import FormEnum
from flask_login import UserMixin

col = db.Column
rel = db.relationship

class ACTIONTYPES(FormEnum):
    BOLUS = 'bolus'
    CARBS = 'carb intake'
    ACTIVITY = 'activity'
    OTHER = 'other'




class Bloodsugar(db.Model):
    id = col(db.Integer, primary_key=True)
    bs = col(db.Integer, nullable=False)
    time = col(db.String(6), nullable=False)
    # act = rel('Action', back_populates='actions')
    act = col(db.Enum(ACTIONTYPES), default=ACTIONTYPES.BOLUS)
    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_by = rel("User")

class Action(db.Model):
    id = col(db.Integer, primary_key=True)
    time = col(db.String(6), nullable=False)
    act_type = col(db.Enum(ACTIONTYPES), default=ACTIONTYPES.BOLUS)
    notes = col(db.String(160), nullable=True)
    created_by_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_by = db.relationship("User")


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return f"<User: {self.username}>"

