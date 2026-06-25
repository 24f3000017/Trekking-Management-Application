from flask import Flask,render_template,url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trek.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create DB + default data
with app.app_context():
    db.create_all()

    # Check karo pehle se admin hai ya nahi
    admin = Admin.query.filter_by(email="admin@gmail.com").first()

    if not admin:
        default_admin = Admin(
            email="admin@gmail.com",
            password="1234"
        )
        db.session.add(default_admin)
        db.session.commit()
        print("Default admin created!")
    else:
        print("Admin already exists!")



@app.route('/admin_login', methods=['POST'])
def admin_login():
    email = request.form.get('email')
    password = request.form.get('password')

    admin = Admin.query.filter_by(email=email, password=password).first()

    if admin:
        return redirect(url_for('admin_dashboard'))   # ✅ success → dashboard
    else:
        return "Invalid email or password"

@app.route('/')
def dashboard():
     return render_template('dashboard.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('./admin/admin_dash.html')

if __name__ == "__main__":
    app.run(debug=True)






