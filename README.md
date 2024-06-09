# Restaurant Website

Welcome to the Restaurant Website project! This repository contains the source code for a full-featured restaurant website built using Django. The website allows users to browse the menu, make reservations, read reviews, and contact the restaurant.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Browse menu items with detailed descriptions and prices
- Order desired menu items and pay using multiple payment methods
- Make online reservations for Tables
- Read and submit reviews and testimonials
- Write and Read Blogs
- Easy to Use Search Bar for menu items
- Admin interface for managing menu items, reservations, reviews, staff and orders

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap5, TailwindCSS
- **Database:** MySQL (default, can be configured to use PostgreSQL, MySQL, etc.)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/UzitheI/ResCaf.git
    cd mysite
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The website will be available at `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel:** Access the admin panel at `http://127.0.0.1:8000/admin/dashboard` to manage menu items, reservations, and reviews.
-Note: The dashboard only opens if the user is a superuser.
- **Homepage:** Visit `http://127.0.0.1:8000/` to view the homepage.

## Project Structure
|-mysite
|--customadmin #dashboard and auth 
|--home #Table Booking, Chef Details, Blog Details, Review
|--menu #Dish, Cart
|--mysite
|--static
||--assets #contains dependencies for index and base
||--assets2 #contains dependecies for admin dashboard
|--templates
||--home_folder
|--theme #contains files for tailwindcss



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request