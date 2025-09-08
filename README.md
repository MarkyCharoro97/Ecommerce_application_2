***Django eCommerce Platform****

A full-stack eCommerce web application built with Django and Django REST Framework, featuring vendor store management, product listings, reviews, shopping cart, and Twitter API integration to automatically share new stores and products.


***purposes****

 User Authentication – Vendors & Buyers with registration and login

 Vendor Stores – Vendors can create and manage their stores

Products – Add, edit, delete, and manage inventory

Shopping Cart – Buyers can add products and checkout

Reviews – Buyers can leave product reviews

Dashboard – Vendor statistics on products and sales

***REST API (via Django REST Framework)***

Stores API

GET /api/stores/ → List all stores

POST /api/stores/ → Create a new store (vendors only)

Products API

GET /api/stores/<id>/products/ → List products for a store

POST /api/stores/<id>/products/ → Add product to store (vendors only)

Reviews API

GET /api/products/<id>/reviews/ → List reviews for a product

Clone the repo

git clone https://github.com/YOUR-USERNAME/ecommerce_project.git
cd ecommerce_project

2.** Creation of virtual enviroment*
python -m venv venv source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows 
3. Install dependencies 
pip install -r requirements.txt
4. Apply migrations 
python manage.py migrate 
5. Create superuser* 
python manage.py createsuperuser
6. Run server* 
python manage.py runserver
**Configure Twitter API**
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret
