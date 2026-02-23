# BarberShop ✂️

BarberShop is a web application built with Python (Django), designed for managing and scheduling barber shop appointments. The application allows users to browse offered services and conveniently book their appointments, while allowing owners to manage their schedules.

## 🚀 Features
- **Service Overview:** A list of offered services (e.g., haircuts, beard trimming, etc.).
- **Bookings:** An appointment scheduling system for clients.
- **User Interface:** An intuitive web design built with HTML and CSS.
- **Admin Panel:** A built-in admin panel for managing services, bookings, and users (via Django Admin).

## 🛠 Technologies Used
- **Back-end:** Python, Django
- **Front-end:** HTML5, CSS3, Django Templates
- **Database:** SQLite (default for Django)

## 📁 Project Structure
- `barber_shop/` - Main configuration directory for the Django project.
- `bookings/` - Application (app) handling the logic for bookings and schedules.
- `services/` - Application (app) for managing barber services and pricing.
- `web/` - Application (app) for the main website pages.
- `templates/` - HTML templates for the views.
- `static/` - Static files (CSS).
- `manage.py` - Main script for managing the Django project.

## 💻 Local Installation and Setup

Follow these steps to run the project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AntonVelev21/BarberShop.git](https://github.com/AntonVelev21/BarberShop.git)
   cd BarberShop
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # For Windows:
   venv\Scripts\activate
   # For Linux/Mac:
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Create `.env` file in the project root based on `.env.example`.**

Example `.env.example`:

```env
SECRET_KEY=your-secret-key
DB_NAME=barbershop_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin) - optional:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the local development server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## 📄 License
This project is licensed under the terms of the [MIT License](LICENSE).