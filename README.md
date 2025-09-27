# HamroDokan — Direct Vendor-Customer E-commerce Platform

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)

HamroDokan is a Django-based e-commerce platform that connects vendors and customers directly. It uses **Jinja templating**, **HTML**, **CSS**,**JS** and Django under the hood to provide a clean, modular, and extensible architecture.

This repository is a part of the **SYP** (Second Year Project) initiative.  

---

## Table of Contents

1. [Features](#features)  
2. [Architecture & Technologies](#architecture--technologies)  
3. [Getting Started](#getting-started)  
   - Prerequisites  
   - Installation  
   - Running the development server  
4. [Usage](#usage)  
   - Vendor workflows  
   - Customer workflows  
   - Admin / staff  

---

## Features

- Vendors can create accounts, manage products (CRUD), view orders, etc.  
- Customers can browse products, place orders, review orders, manage profile.  
- Admin panel (via Django admin) for site oversight.  
- Clean UI using Jinja templates + custom CSS.  
- Modular Django app structure to allow scaling and extension.  
- User authentication, sessions, security basics (CSRF, login required for certain pages).  
- Friendly URLs and basic routing (e.g. product pages, vendor dashboard, etc.).

---

## Architecture & Technologies

- **Backend**: Django (Python)  
- **Templating**: Jinja templates
- **Frontend**: HTML, CSS,JS ( Can be extended by frontend frameworks later)  
- **Database**: MySQL( for easier integration)
- **Static & media files**: handled via Django’s static / media settings.  
- **Routing & URLs**: clean URL paths for products, vendors, accounts.  

The idea is to keep separation of concerns—views, templates, models, forms—and make it easier to plug in extra features later (e.g. payments, search, APIs).

---

## Getting Started

### Prerequisites

- Python ≥ 3.8  
- pip / virtualenv (or venv)  
- (Optional but recommended) PostgreSQL / MySQL

### Installation Steps

###  1. Clone the repo
- git clone https://github.com/prameshk7/HamroDokan.git
- cd HamroDokan

###  2. Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

###  3. Install dependencies
pip install -r requirements.txt

###  4. Apply migrations
python manage.py migrate

###  5. Create superuser
python manage.py createsuperuser

###  6. Collect static files (optional)
python manage.py collectstatic

## Usage

### **Vendor Workflow**
- **Register / Login** as a vendor  
- Access **Dashboard** to add, edit, or delete products  
- **View orders** placed by customers  
- **Manage vendor profile**  

### **Customer Workflow**
- **Register / Login** as a customer  
- **Browse product catalog** and view product details  
- **Add items to cart** and place orders  
- **View order history**  
- **Manage customer profile**  

### **Admin / Staff**
- Use **Django Admin** to manage users, products, and orders  
- **Monitor vendor activities** and site content  

