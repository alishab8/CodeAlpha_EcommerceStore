# CodeAlpha_EcommerceStore

A basic e-commerce store built with **Django** (backend) and **HTML/CSS/JS** (frontend), created for the CodeAlpha Full Stack Development internship — **Task 1**.

## Features
- Product listing with category filtering
- Product detail pages
- Session-based shopping cart (add, update quantity, remove)
- User registration & login (Django auth)
- Checkout / order processing (creates real `Order` + `OrderItem` records, decrements stock)
- Order history for logged-in users
- Django admin panel for managing products, categories, and orders

## Tech Stack
- Python 3 / Django 6
- SQLite (default, swappable to Postgres/MySQL)
- Django templates + vanilla CSS/JS

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py seed_data      # loads sample categories & products
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the store and `http://127.0.0.1:8000/admin/` for the admin panel.

## Project Structure
```
ecommerce_project/   # Django project settings & root urls
store/                # Main app: models, views, forms, cart logic, templates
static/css/           # Stylesheet
```

## Notes
- Cart is stored in the session, so it persists across pages without a DB write until checkout.
- On checkout, stock is decremented and the cart is cleared.
- Product images are optional (upload via admin panel); a placeholder shows if none is set.
