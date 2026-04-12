# 💼 nomina-prima

Aplicación web desarrollada en Django para la **gestión de nómina y timbrado CFDI 4.0 en México**.

---

## 🎯 Propósito

`nomina-prima` tiene como objetivo ofrecer una solución integral para:

Sistema integral de gestión de nómina diseñado para PyMEs en México que permite:

- **Gestión completa de empleados** y estructura organizacional
- **Captura de incidencias** (faltas, horas extras, bonos, préstamos)
- **Cálculo de nómina** con toda la complejidad fiscal mexicana (ISR, IMSS, Infonavit)
- **Timbrado de CFDI 4.0** con complemento de nómina
- **Reportes gerenciales** personalizados y análisis de costos
- **Acceso web/móvil** para consultas desde cualquier dispositivo

---

## 🧱 Stack Tecnológico

### Backend
- **Python 3.11+**
- **Django 5.0+** - Framework web principal
- **Django REST Framework** - API para frontend y futuras integraciones
- **Celery** - Tareas asíncronas (cálculos pesados, envío de emails)
- **Redis** - Cache y broker para Celery

### Base de Datos
- **PostgreSQL 15+** - Base de datos principal
  - Soporte JSON nativo para flexibilidad en percepciones/deducciones
  - Transacciones ACID para integridad de datos
  - Excelente performance para reportes complejos
  - 
### Frontend
- **Django Templates** + **Tailwind CSS** - UI responsive desde día 1
- **Alpine.js** - Interactividad sin complejidad de SPA
- **HTMX** - Actualizaciones dinámicas sin escribir JavaScript
- 
### Infraestructura
- Desarrollo: Windows
- Producción: Linux (Ubuntu)

### Servidor Web
- Apache + mod_wsgi
- 
### Integraciones Fiscales
- **API PAC (Proveedor Autorizado de Certificación)**
  - Opciones:  Finkok
  - Timbrado de CFDI de nómina
  - Cancelación de CFDIs
  - 
### Herramientas de Desarrollo
- **Git** - Control de versiones
- **pytest** - Testing
- **Black** + **Flake8** - Code formatting y linting
- **pre-commit** - Hooks para mantener calidad de código
- 
### Otros
- OpenSSL (sellado CFDI)
- XML (lxml)
- SOAP (zeep)


## 📦 Arquitectura del Sistema

### Módulos Principales

#### 1. **Empleados** (`employees`)
- Catálogo de empleados
- Estructura organizacional (departamentos, puestos)
- Contratos y registros patronales
- Datos fiscales (RFC, CURP, NSS)
- Historial de cambios de salario

#### 2. **Nómina** (`payroll`)
- Periodos de nómina (semanal, quincenal, mensual)
- Cálculo de percepciones y deducciones
- Motor de cálculo fiscal:
  - ISR según tablas del SAT
  - Cuotas IMSS (obrero-patronales)
  - Retención Infonavit
  - Subsidio al empleo
- Conceptos especiales (aguinaldo, PTU, finiquitos)
- Pre-nómina y validaciones

#### 3. **Incidencias** (`incidents`)
- Faltas y retardos
- Horas extras
- Bonos y comisiones
- Préstamos y descuentos
- Vacaciones e incapacidades
- Sistema de aprobación workflow

#### 4. **Timbrado** (`cfdi`)
- Generación de XML según estándar SAT
- Integración con PAC
- Validación de CFDI
- Almacenamiento de XML/PDF
- Cancelación de comprobantes
- Re-envío de recibos por email

#### 5. **Reportes** (`reports`)
- Papel de trabajo de nómina
- Dispersión bancaria
- Archivos IDSE/SUA para IMSS
- Provisiones contables
- Análisis de costo de nómina
- Exportación a Excel/PDF

#### 6. **Configuración** (`settings`)
- Empresa(s) y registros patronales
- Catálogos del SAT
- Percepciones y deducciones personalizadas
- Fórmulas de cálculo
- Certificados digitales (CSD)

## 🔐 Seguridad y Cumplimiento

- **Autenticación robusta** - Django auth + 2FA opcional
- **Permisos granulares** - Control de acceso por rol
- **Auditoría completa** - Log de todas las operaciones sensibles
- **Encriptación de datos sensibles** - Salarios, RFC, NSS
- **Backups automáticos** - PostgreSQL + archivos XML/PDF
- **Cumplimiento fiscal** - Actualización constante de tablas SAT

## 🚀 Modelo de Datos (Simplificado)

---Employee
├── personal_data (nombre, RFC, CURP, NSS, etc.)
├── contract (salario, puesto, departamento, registro patronal)
├── bank_account (dispersión)
└── fiscal_regime (clave SAT)
PayrollPeriod
├── period_type (semanal/quincenal/mensual)
├── date_range (inicio, fin)
├── status (draft/calculated/paid/stamped)
└── employees → PayrollEntry
PayrollEntry
├── employee
├── perceptions → Perception[]
├── deductions → Deduction[]
├── net_pay
├── cfdi → CFDI
└── calculations (JSON con desglose)
CFDI
├── uuid (folio fiscal)
├── xml_file
├── pdf_file
├── status (active/cancelled)
└── pac_response (JSON)
Incident
├── employee
├── type (absence/overtime/bonus/loan)
├── amount/hours
├── period
└── approved_by

## 🎨 Principios de Diseño

### Simplicidad Primero
- UI intuitiva sin curva de aprendizaje
- Flujos de trabajo claros
- Mobile-first design

### Transparencia Total
- Usuario ve exactamente cómo se calculó cada concepto
- Trazabilidad completa de cambios
- Reportes explicativos

### Flexibilidad Controlada
- Percepciones/deducciones personalizables
- Fórmulas de cálculo editables
- Pero con validaciones fuertes para evitar errores

### Performance
- Cálculo de 100 empleados < 30 segundos
- Reportes con cache
- Queries optimizadas

## 📋 Roadmap

### Fase 1: MVP (Meses 1-3)
- [x] Modelo de datos core
- [ ] Catálogo de empleados
- [ ] Cálculo básico de nómina ordinaria
- [ ] Integración con PAC para timbrado
- [ ] Reportes básicos (papel de trabajo, dispersión)

### Fase 2: Funcionalidad Completa (Meses 4-6)
- [ ] Gestión de incidencias
- [ ] Cálculos especiales (aguinaldo, PTU, finiquitos)
- [ ] Portal de empleados (consulta de recibos)
- [ ] Reportes avanzados
- [ ] Workflow de aprobaciones

### Fase 3: Optimización (Meses 7-9)
- [ ] Dashboard analytics
- [ ] Exportación contable (pólizas)
- [ ] Integración bancaria (confirmación de dispersión)
- [ ] App móvil nativa (opcional)
- [ ] Multi-empresa mejorada

## 🧪 Testing

- **Unit tests** - Lógica de cálculo fiscal (>90% coverage obligatorio)
- **Integration tests** - Flujos completos de nómina
- **E2E tests** - Casos de uso críticos
- **Load testing** - Verificar performance con 500+ empleados

## 📚 Dependencias Clave

```python
# Core
Django==5.0+
djangorestframework==3.14+
psycopg2-binary==2.9+

# Async tasks
celery==5.3+
redis==5.0+

# Cálculos
python-dateutil==2.8+
pandas==2.1+  # Para reportes complejos

# XML/CFDI
lxml==4.9+
cryptography==41.0+  # Para firmado digital

# PDF
reportlab==4.0+  # Generación de PDFs
weasyprint==60.0+  # HTML to PDF (recibos)

# Excel
openpyxl==3.1+  # Para reportes Excel

# HTTP/API
requests==2.31+

# Desarrollo
pytest-django==4.5+
black==23.0+
flake8==6.0+
```

## 📖 Convenciones

### Código
- PEP 8 estricto
- Type hints obligatorios en funciones públicas
- Docstrings en español para lógica de negocio
- Commits en inglés (conventional commits)

### Git Flow
- `main` - Producción estable
- `develop` - Desarrollo activo
- `feature/*` - Nuevas funcionalidades
- `hotfix/*` - Correcciones urgentes

### Naming
- Modelos: Singular en inglés (`Employee`, `Payroll`)
- Apps: Plural en inglés (`employees`, `payrolls`)
- Campos fiscales: Nombre oficial SAT en comentarios

## 🤝 Contribución

Este es un proyecto privado para uso interno. 

Para mejoras o bugs:
1. Crear issue describiendo el problema
2. Branch desde `develop`
3. PR con tests que cubran el cambio
4. Code review requerido antes de merge

## ⚠️ Disclaimer Legal

Este software es una herramienta de gestión. La responsabilidad del cumplimiento fiscal recae en el usuario final. Se recomienda validación con contador certificado.

Las tablas y fórmulas fiscales se actualizan conforme a publicaciones del SAT, pero el usuario debe verificar su vigencia.

## 📞 Soporte

Para dudas sobre implementación o configuración fiscal, consultar con el equipo de desarrollo.

---

**Versión:** 0.1.0-alpha  
**Última actualización:** Abril 2026  
**Licencia:** Propietario - Uso interno



# INSTALACION

## Componentes
 


**Para Windows** **Utiliza python 3.10.0**



https://www.python.org/downloads/release/python-3100/

https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe



**Para Linux ubuntu** **Utiliza python 3.10.0**



https://www.python.org/downloads/release/python-3100/

ajustar url si la hay para bajar instalador

https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe


```bash
pip install Django==4.1.7
pip install openpyxl==3.1.1
pip install django-bootstrap4==22.3
pip install aiohttp== 3.8.4
pip install mod_wsgi== 4.9.4
```

Puedes crear el archivo de requirementes asi

**requirements.txt**

```bash
Django==4.1.7
openpyxl==3.1.1
django-bootstrap4==22.3
aiohttp== 3.8.4
mod_wsgi== 4.9.4
```




## 🚀 Inicio del Proyecto (Setup básico)
ir al directorio  donde se tiene el proyecto
patht \\nomina-prima\src
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

pip install -r requirements.txt

# Instalar Django
pip install django
pip install Django==5.2.13

pip install psycopg2-binary
psycopg2-binary   2.9.11
psycopg           3.3.3

cryptography==42.0.5
pyOpenSSL==24.1.0

pip install Django==5.2.13
pip install django-bootstrap5==26.1
pip install djangorestframework==3.17.1
pip install django-environ==0.13.0
pip install django-extensions==4.1
pip install zeep==4.3.2
pip install requests==2.33.1
pip install urllib3==2.6.3
pip install openpyxl==3.1.5
pip install xlsxwriter==3.2.9
pip install reportlab==4.4.10
pip install weasyprint==68.1
pip install PyPDF2==3.0.1
pip install celery==5.6.3
pip install redis==7.4.0
pip install python-dateutil==2.9.0.post0
pip install pytz==2026.1.post1
pip install Pillow==12.2.0
pip install python-stdnum==2.2
pip install mod_wsgi==5.0.2
pip install psycopg==3.3.3
pip install cryptography==46.0.7
pip install pyOpenSSL==26.0.0
pip install lxml==6.0.3


# Crear proyecto
django-admin startproject nomina_prima

cd nomina_prima

# Crear app principal
python manage.py startapp primus

python manage.py runserver

navegar a

http://127.0.0.1:8000/

para matar proceso

ctrl+c

```



## 🧪 Desarrollo en Windows

### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```


### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```


### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```


### 4. Configurar variables de entorno

```bash
DEBUG=True
SECRET_KEY=tu_clave_secreta
DB_NAME=nomina
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```


### 5. Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```


### 1. 6. Ejecutar servidor

```bash
python manage.py runserver
```

👉 Acceder: http://127.0.0.1:8000

## 🐘 Configuración PostgreSQL (Windows)
Instalar PostgreSQL
Crear base de datos:

### 1. Clonar repositorio

```bash
CREATE DATABASE nomina_prima;
```



## 🧪 Desarrollo en Linux Ubuntu

### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```


### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```


### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```


### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```


### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```


### 1. Clonar repositorio

```bash
git clone https://github.com/tuusuario/nomina-prima.git
cd nomina-prima
```
