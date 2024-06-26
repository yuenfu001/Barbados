Trucking Management System

Trucking Management System is a web application built using Django that helps manage trucking operations, driver profiles, trips, orders, and more.
Features

    Truck Management: Add and update truck information, including BL number and plate number.

    Driver Profiles: Create and manage driver profiles with personal information, identification, and assigned truck details.

    Trips: Track individual and company trips, including trip names, initials, dates, and proposal files.

    Order Management: Manage both individual and company orders, including client details, driver info, trip numbers, weights, and more.

    User Authentication: User registration, login, and management with customizable permissions.

Installation

    Clone the repository:

    cmd/powershell

git clone https://github.com/yuenfu001/Barbados
cd Barbados

Create a virtual environment (optional but recommended):

cmd/powershell

python3 -m venv venv
activate your virtual Environment

Install dependencies:

cmd/powershell

pip install -r requirements.txt

Run migrations:

cmd/powershell

python manage.py migrate

Create a superuser:

cmd/powershell

python manage.py createsuperuser

Run the development server:

cmd/powershell

    python manage.py runserver

    Access the application at http://localhost:8000 and the admin interface at http://localhost:8000/admin/.

Usage

    Home Page: The home page displays summary information about trucks, drivers, orders, and trips.

    Adding Truck and Driver: Use the "Add Truck" and "Add Driver" options to input truck and driver details.

    Trips and Orders: Manage trips and orders through respective forms. You can also update and delete existing entries.

    User Management: Register new users and manage their permissions via the admin interface.

Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to create issues or pull requests.
License

This project is licensed under the MIT License.
