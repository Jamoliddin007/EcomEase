# 🛒 EcomEase — Scalable & Modular E-commerce Platform

## 🔍 Overview

**EcomEase** is a powerful e-commerce backend built with Django and Django REST Framework. It is designed with a modular architecture, multilingual support, and scalability in mind. The project offers a clean admin panel, organized API endpoints, and a solid foundation for real-world e-commerce solutions.

---

## ⚙️ Key Features

- **Modular API endpoints** for Products, Categories, Brands, Variants, Colors, Sizes, Media, Reviews, and Comments.
- **Multilingual support** using `django-modeltranslation` for fields like `name` and `description` in `uz`, `ru`, and `en`.
- **JWT Authentication** with `djangorestframework-simplejwt` for secure access and refresh tokens.
- **Structured admin panel** with custom admin classes for full control over product management.
- **Swagger & Redoc API documentation** using `drf_yasg`.
- **Static & media file handling** with customizable `MEDIA_URL` and `MEDIA_ROOT`.
- **Reusable base model** including timestamps (`created_at`, `updated_at`) for all models.
- **Clean project structure** using `api_endpoints/<ModelName>/<Operation>/views.py` pattern.

---

## 🧰 Tech Stack

| Layer            | Tools / Libraries                        |
|------------------|------------------------------------------|
| Backend Framework| Django, Django REST Framework            |
| Auth             | djangorestframework-simplejwt            |
| Translation      | django-modeltranslation                  |
| API Docs         | drf_yasg (Swagger/OpenAPI, Redoc)        |
| Admin UI         | Django Admin (Jazzmin optional)          |
| Database         | PostgreSQL / SQLite                      |

---

## 🚀 Getting Started

```bash
git clone https://github.com/Jamoliddin007/EcomEase.git
cd EcomEase
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Swagger: http://localhost:8000/swagger/

Admin Panel: http://localhost:8000/admin/

## 🎯 Future Improvements

- Add GraphQL support  
- Frontend integration with React or Vue  
- Dockerize the project for production  
- Add payment gateway integrations


