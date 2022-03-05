from bs_track.extensions import app, db

from bs_track.bs.routes import routes as bs
from main import routes as main_routes
from bs_track.login.routes import auth
from bs_track.acts.routes import routes as acts_routes



app.register_blueprint(acts_routes)
app.register_blueprint(bs)
app.register_blueprint(main_routes)
app.register_blueprint(auth)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)