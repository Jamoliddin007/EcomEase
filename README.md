# 🛒 EcomEase — Scalable & Modular E-commerce Platform

## 🔍 Overview

**EcomEase** is a powerful e-commerce backend built with Django and Django REST Framework.  
It is designed with a modular architecture, multilingual support, and scalability in mind.  
The project offers a clean admin panel, organized API endpoints, and a solid foundation for real-world e-commerce solutions.

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

🎯 Future Improvements
Add GraphQL support

Frontend integration with React or Vue

Dockerize the project for production

Add payment gateway integrations

🛍️ EcomEase — Masshtablanuvchi va Modulyar E-commerce Platforma
🔍 Umumiy Ko‘rinish
EcomEase bu Django va Django REST Framework asosida yaratilgan kuchli e-commerce backend bo‘lib,
modulyar tuzilma, ko‘p tillilik va kengayuvchanlikka yo‘naltirilgan.
Loyihada toza admin panel, aniq API endpointlar va real e-commerce tizimlar uchun mustahkam poydevor mavjud.

⚙️ Asosiy Xususiyatlar
Modulga bo‘lingan API endpointlar: Product, Category, Brand, Size, Color, Media, Review, Comment

Ko‘p tillilik: django-modeltranslation orqali name va description maydonlari uz, ru, en tillarida

JWT autentifikatsiya: djangorestframework-simplejwt orqali xavfsiz kirish va refresh tokenlar

Admin paneli: Maxsus admin klasslar bilan barcha ma’lumotlarni boshqarish qulay

Swagger & Redoc: drf_yasg yordamida hujjatlashtirilgan API

Media fayllarni boshqarish: MEDIA_URL, MEDIA_ROOT sozlamalari orqali

BaseModel: Barcha modellarda created_at, updated_at kabi umumiy maydonlar

Toza loyiha strukturasi: api_endpoints/<Model>/<Operation>/views.py formatida tashkil etilgan

🧰 Texnologiyalar
Qavat	Texnologiyalar
Backend Framework	Django, Django REST Framework
Avtorizatsiya	djangorestframework-simplejwt
Tarjima	django-modeltranslation
API Hujjatlari	drf_yasg (Swagger/OpenAPI, Redoc)
Admin Panel	Django Admin (Jazzmin qo‘llab-quvvatlanadi)
Ma’lumotlar ombori	PostgreSQL / SQLite

🚀 Ishga tushirish
bash
Copy
Edit
git clone https://github.com/Jamoliddin007/EcomEase.git
cd EcomEase
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Swagger: http://localhost:8000/swagger/

Admin panel: http://localhost:8000/admin/

🎯 Kelajakdagi Yo‘nalishlar
GraphQL qo‘llab-quvvatlash

React yoki Vue bilan frontend integratsiyasi

Docker orqali deploy qilish

To‘lov tizimlari integratsiyasi

yaml
Copy
Edit

---

## ✅ Endi nima qilish kerak?

1. `README.md` faylni VS Code’da oching  
2. `<<<<<<<`, `=======`, `>>>>>>>` kabi conflict belgilari bor bloklarni **tozalang**  
3. Yuqoridagi **toza versiyani** joylashtiring  
4. Terminalda quyidagini bering:

```bash
git add README.md
git commit -m "fix: resolve merge conflict in README.md"
git push origin refactor/profile-endpoints
