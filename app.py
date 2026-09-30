from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Event

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lutan.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    events = Event.query.order_by(Event.date.asc()).limit(6).all()
    return render_template("index.html", events=events)

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/signals")
def signals():
    return render_template("signals.html")

@app.route("/events")
def events():
    all_events = Event.query.order_by(Event.date.asc()).all()
    return render_template("events.html", events=all_events)

@app.route("/events/<int:event_id>")
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event_detail.html", event=event)

@app.route("/admin/events")
def admin_events():
    all_events = Event.query.order_by(Event.date.desc()).all()
    return render_template("admin/events.html", events=all_events)

@app.route("/admin/events/new", methods=["GET", "POST"])
def new_event():
    if request.method == "POST":
        event = Event(
            title=request.form["title"],
            description=request.form.get("description", ""),
            date=request.form["date"],
            venue=request.form.get("venue", ""),
            image_url=request.form.get("image_url", ""),
            price=request.form.get("price", "")
        )
        db.session.add(event)
        db.session.commit()
        flash("Event created.", "success")
        return redirect(url_for("admin_events"))
    return render_template("admin/event_form.html", event=None)

@app.route("/admin/events/<int:event_id>/edit", methods=["GET", "POST"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == "POST":
        event.title = request.form["title"]
        event.description = request.form.get("description", "")
        event.date = request.form["date"]
        event.venue = request.form.get("venue", "")
        event.image_url = request.form.get("image_url", "")
        event.price = request.form.get("price", "")
        db.session.commit()
        flash("Event updated.", "success")
        return redirect(url_for("admin_events"))
    return render_template("admin/event_form.html", event=event)

@app.route("/admin/events/<int:event_id>/delete", methods=["POST"])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted.", "success")
    return redirect(url_for("admin_events"))

if __name__ == "__main__":
    app.run(debug=True)
