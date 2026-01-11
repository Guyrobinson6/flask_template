# Flask Project Boilerplate

A starter template for Flask applications. This boilerplate is set up using the **Application Factory Pattern**, **Blueprints**, **SQLAlchemy**, and **Bootstrap 5**.

## Features
- **Scalable Structure:** Uses Blueprints and Application Factory (`create_app`).
- **Database Ready:** Pre-configured with SQLite and SQLAlchemy.
- **UI Ready:** Bootstrap 5 via `bootstrap-flask`.
- **Configuration:** Clean separation of config settings via `.env`.

---

## 🚀 How to Start a New Project

Do not work directly inside this folder. Instead, follow these steps to create a new project based on this template.

### 1. Copy the Template
Open your terminal and duplicate this folder, renaming it to your new project name.

**Linux / macOS (WSL)**
```bash
cp -r flask_template my_new_project
cd my_new_project
rm -rf .git
git init
git add .
git commit -m "Initial commit"
```

**Windows (Powershell)**
```Powershell
Copy-Item -Path flask_template -Destination my_new_project -Recurse
cd my_new_project
```
---

### 2. Set Up Virtual Environment
You must create a fresh virtual environment for every new project.

**Linux / macOS (WSL)**
```bash
# Create the environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

**Windows (Powershell)**
```Powershell
# Create the environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

---

### 3. Install Dependencies
Install the required packages listed in requirements.txt.

```Bash
pip install -r requirements.txt
```
---

### 4. Set Up Local Environment Variables (.env)
This project supports environment variables via a local `.env` file. Create a file named `.env` in the root of your project (same level as `run.py`).

See the example `.env.example` file for more info.

**Crucial:** Do not commit your .env file to version control. It is already added to .gitignore.

## 🐘 Creating a Dedicated PostgreSQL User (SQLAlchemy‑Friendly)

1. Create the PostgreSQL user and database

Inside the PostgreSQL shell:
```
sudo -i -u postgres
psql
```
Then:
```
CREATE USER flaskuser WITH PASSWORD 'strongpassword';
CREATE DATABASE flaskdb OWNER flaskuser;
GRANT ALL PRIVILEGES ON DATABASE flaskdb TO flaskuser;
```
Exit:
```
\q
exit
```
## 🧩 2. Use the correct SQLAlchemy connection string

SQLAlchemy uses the standard PostgreSQL URI format:

```postgresql://username:password@host:port/databasename```

For your dedicated user:

```postgresql://flaskuser:strongpassword@localhost:5432/flaskdb```

If you’re using environment variables (recommended):

```DATABASE_URL="postgresql://flaskuser:strongpassword@localhost:5432/flaskdb"```

## 🏗️ 3. Configure SQLAlchemy in your Flask project

Inside config.py:

```import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
Inside __init__.py:
```
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models  # ensure models are imported

    return app
```
## 🧱 4. Define your models normally

SQLAlchemy doesn’t care which PostgreSQL user owns the database — it only cares that the user has permission to create tables.

Example:
```
from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
```
## 🔧 5. Run migrations with Flask‑Migrate
```
flask db init      # only once
flask db migrate -m "Initial migration"
flask db upgrade
```
These commands will create tables inside flaskdb using the permissions of flaskuser.

---

### 5. Configuration Setup

This project uses a robust configuration system defined in `config.py`. It supports multiple environments (Development, Production) and loads secrets from your `.env` file.

**Available Environments**
The `config_map` in `config.py` defines:
- **`development`**: Debug mode enabled (`DEBUG=True`).
- **`production`**: Optimized for deployment (`DEBUG=False`).

**How to Switch Environments**
By default, `run.py` starts the app in **development** mode. To change this, you can modify the `create_app` call in `run.py`:

```python
# run.py
app = create_app('production')
```
---

### 6. Run the Application
Start the Flask development server.

**Linux / macOS**

```Bash
python3 run.py
```
**Windows**

```Bash
python run.py
```
Open your browser and navigate to: http://127.0.0.1:5000/

---

### 📂 Project Structure

```Text
my_new_project/
│
├── app/
│   ├── __init__.py         # App Factory & Extension Initialization
│   ├── extensions.py       # DB & Bootstrap Instances
│   ├── models.py           # Database Models
│   ├── static/             # CSS, JS, Images
│   ├── templates/          # Global Templates (base.html)
│   │
│   └── main/               # Main Blueprint
│       ├── __init__.py
│       └── routes.py       # Routes for the main section
│
├── instance/               # SQLite database appears here after running
├── .env                    # Environment variables (Secret keys, DB URL)
├── config.py               # Settings (Loads values from .env)
├── run.py                  # Entry point script
└── requirements.txt        # Python dependencies
```
---

### 🛡️ Git & Security (`.gitignore`)
To keep your repository clean and secure, the `.gitignore` file is pre-configured to exclude sensitive and temporary files:

```Text
# Python internals
__pycache__/
*.pyc

# Virtual Environment
venv/

# Environment Variables (SECRETS)
.env

# Database & Instance folder
instance/
*.sqlite
*.db

# OS metadata
.DS_Store
```

---

### 🛠 Customization Guide
Once your new project is running, here are the first things you should do:

* Configure Environment (`.env`): Ensure your `.env` file exists and has a unique SECRET_KEY.
* `app/templates/base.html`: Change the <title> and Navbar brand name to match your new project.
* `app/models.py`: Define your database tables (SQLAlchemy Classes).
* `app/main/routes.py`: Start building your views and routes.

### Database Management
The database file (e.g., `app.db`) is automatically created in the `instance/` folder the first time you run the app (thanks to `db.create_all()` in the app factory).

To reset the database during development:
* Stop the Flask server.
* Delete the .db or .sqlite file inside the instance/ folder.
* Restart the application. The app factory will automatically recreate the tables defined in your models.
