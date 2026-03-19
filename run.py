from app import create_app, db
import time

app = create_app()

# attendre MySQL
time.sleep(10)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)