# Flask Project Boilerplate

A starter template for Flask applications. This boilerplate is set up using the **Application Factory Pattern**, **Blueprints**, **SQLAlchemy**, and **Bootstrap 5**.

## Features
- **Scalable Structure:** Uses Blueprints and Application Factory (`create_app`).
- **Database Ready:** Pre-configured with SQLite and SQLAlchemy.
- **UI Ready:** Bootstrap 5 via `bootstrap-flask`.
- **Configuration:** Clean separation of config settings.

---

## 🚀 How to Start a New Project

Do not work directly inside this folder. Instead, follow these steps to create a new project based on this template.

### 1. Copy the Template
Open your terminal and duplicate this folder, renaming it to your new project name.

**Linux / macOS (WSL)**
```bash
cp -r flask_template my_new_project
cd my_new_project
```

**Windows (PowerShell)**
```powershell
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

**Windows (Command Prompt / PowerShell)**
```powershell
# Create the environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

*(You should see `(venv)` appear at the start of your command line).*

---

### 3. Install Dependencies

Install the required packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

Start the Flask development server.

**Linux / macOS**
```bash
python3 run.py
```

**Windows**
```bash
python run.py
```

Open your browser and navigate to: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📂 Project Structure

```text
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
├── config.py               # Settings (Secret Keys, DB URI)
├── run.py                  # Entry point script
└── requirements.txt        # Python dependencies
```

## 🛠 Customization Guide

Once your new project is running, here are the first things you should change:

1.  **`app/templates/base.html`**: Change the `<title>` and Navbar brand name.
2.  **`config.py`**: Update the `SECRET_KEY` for security.
3.  **`app/models.py`**: Define your database tables (Classes).
4.  **`app/main/routes.py`**: Start building your views.

## Database Management
The database (`app.db`) is automatically created in the `instance/` folder the first time you run the app.

To reset the database during development:
1. Delete the `instance/app.db` file.
2. Restart the application (the `create_app` function will recreate empty tables).