# 🛒 Shop API

A RESTful API backend for an e-commerce platform built with **Django** and **Django REST Framework**. It supports full product management, vendor relationships, and product reviews — using a mix of APIView, Generic Views, and ViewSets to demonstrate multiple DRF patterns.

---

## 🚀 Features

- Full CRUD for **Products**, **Vendors**, and **Reviews**
- Many-to-Many relationship between Vendors and Products
- Reviews linked to both Products and Vendors via ForeignKey
- Mix of DRF patterns: `APIView`, `generics`, and `ModelViewSet`
- Auto-generated router URLs for Reviews
- Django Admin panel integration

---

## 🧱 Tech Stack

| Layer        | Technology                    |
|--------------|-------------------------------|
| Language     | Python 3.x                    |
| Framework    | Django                        |
| API Layer    | Django REST Framework (DRF)   |
| Database     | SQLite (default) / PostgreSQL |
| Admin        | Django Admin                  |

---

## 📁 Project Structure

```
shop/
├── models.py         # Product, Vendor, Review models
├── serializers.py    # ModelSerializers for all models
├── views.py          # APIView, Generic Views, and ViewSet
├── urls.py           # URL routing including DRF router
└── admin.py          # Admin registration
```

---

## 📦 Models

### Product
| Field         | Type          |
|---------------|---------------|
| `name`        | CharField     |
| `price`       | DecimalField  |
| `description` | TextField     |
| `stock`       | IntegerField  |

### Vendor
| Field      | Type                          |
|------------|-------------------------------|
| `name`     | CharField (unique)            |
| `products` | ManyToManyField → Product     |
| `bio`      | TextField                     |

### Review
| Field     | Type                    |
|-----------|-------------------------|
| `product` | ForeignKey → Product    |
| `vendor`  | ForeignKey → Vendor     |
| `rating`  | IntegerField            |
| `comment` | TextField               |

---

## 🔌 API Endpoints

### Products
| Method   | Endpoint               | Description            |
|----------|------------------------|------------------------|
| `GET`    | `/products/`           | List all products      |
| `POST`   | `/products/`           | Create a product       |
| `GET`    | `/products/<id>/`      | Retrieve a product     |
| `PUT`    | `/products/<id>/`      | Update a product       |
| `DELETE` | `/products/<id>/`      | Delete a product       |

### Vendors
| Method   | Endpoint               | Description            |
|----------|------------------------|------------------------|
| `GET`    | `/vendors/`            | List all vendors       |
| `POST`   | `/vendors/`            | Create a vendor        |
| `GET`    | `/vendors/<id>/`       | Retrieve a vendor      |
| `PUT`    | `/vendors/<id>/`       | Update a vendor        |
| `DELETE` | `/vendors/<id>/`       | Delete a vendor        |

### Reviews *(Router-generated)*
| Method   | Endpoint               | Description            |
|----------|------------------------|------------------------|
| `GET`    | `/reviews/`            | List all reviews       |
| `POST`   | `/reviews/`            | Create a review        |
| `GET`    | `/reviews/<id>/`       | Retrieve a review      |
| `PUT`    | `/reviews/<id>/`       | Update a review        |
| `DELETE` | `/reviews/<id>/`       | Delete a review        |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/omartamer002/shop.git
cd shop
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for Admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

---

## 🛠️ Admin Panel

Access the Django Admin dashboard at:
```
http://127.0.0.1:8000/admin/
```
All three models — **Product**, **Vendor**, and **Review** — are registered and manageable from the admin interface.

---

## 📐 DRF Patterns Used

| Resource | Pattern              | Why                                       |
|----------|----------------------|-------------------------------------------|
| Product  | `APIView`            | Manual control over request handling      |
| Vendor   | `Generic Views`      | Concise list/create and retrieve/update/delete |
| Review   | `ModelViewSet`       | Full CRUD with auto-router URL generation |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
