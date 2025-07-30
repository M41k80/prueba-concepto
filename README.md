# 🧪 Prueba de Concepto - FastAPI + Supabase + JWT Auth

Este proyecto es una prueba de concepto de backend utilizando **FastAPI**, **SQLAlchemy**, **Supabase (PostgreSQL)** y autenticación con **JWT**. Incluye registro, login, y acceso a un endpoint protegido.

---

## 🚀 Tecnologías utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL (Supabase)
- JWT (Json Web Tokens)
- Bcrypt
- Uvicorn
- Pydantic
- Passlib
- dotenv

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

```python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

```
pip install -r requirements.txt
```


```
SUPABASE_URL=postgresql+psycopg2://usuario:contraseña@host:puerto/base_de_datos
SECRET_KEY=una_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

```
uvicorn main:app --reload

```
🔐 Endpoints

/register – Registro de usuario
POST
```
Body JSON:
{
  "email": "correo@example.com",
  "password": "tu_contraseña"
}
```


/login – Login de usuario
POST
```
Body JSON:
{
  "email": "correo@example.com",
  "password": "tu_contraseña"
}
Respuesta:
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```


/me – Usuario actual (requiere token)
GET
```
Header:
Authorization: Bearer TU_TOKEN
Respuesta:
{
  "email": "correo@example.com",
  "id": 1
}
```
