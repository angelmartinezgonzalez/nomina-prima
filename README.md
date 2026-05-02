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
pip install requests==2.33.1
pip install pycurl==7.45.7
pip install qrcode[pil] pillow
pip install qrcode==8.2
pip install weasyprint==68.1
pip install reportbro-lib==3.12.1
pip install hidash==0.2.29
pip install bokeh==3.9.0
        


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



## 🧪 Desarrollo en Windows con Apache2

### 1. Ir a el directorio donde tienes apache
```bash
C:\Apache24
```

### 2. Clonar repositorio

```bash
git clone https://github.com/angelmartinezgonzalez/nomina-prima.git htdocs
cd htdocs\src
```


### 3. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```


### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```


Paso 3.1: Configurar mod_wsgi

Después de instalar mod_wsgi, ejecuta:
bash
```bash
mod_wsgi-express module-config
```
da algo asi

```bash
LoadFile "C:/Python310/python310.dll"
LoadModule wsgi_module "C:/Python310/lib/site-packages/mod_wsgi/server/mod_wsgi.cp310-win_amd64.pyd"
WSGIPythonHome "C:/Python310"
```



Para windows. crear archvivo wsgi_windows.py

en donde se encuantra el archivo que es para linux
wsgi.py 

Ajustando el contenido deacuerdo a tu instalacion 

```bash

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Python310/Lib/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Apache24/htdocs/src/nomina_prima/')
sys.path.append('C:/Apache24/htdocs/src/nomina_prima/nomina_prima/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'nomina_prima.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nomina_prima.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()



```



### 4. Configurar servidor apache

Para usar un nombre de dominio localmente modiciar el archivo de hosts.
por ejemplo
www.nomina-prima.com.mx

C:\Windows\System32\drivers\etc\hosts

```bash
127.0.0.2 www.nomina-prima.com.mx nomina-prima.com.mx
```

Apache modificar el archivo **httpd.conf**

Al final del archivo **httpd.conf**
```bash

LoadFile "C:/Python310/python310.dll"
LoadModule wsgi_module "C:/Python310/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp310-win_amd64.pyd"
WSGIPythonHome "C:/Python10"
WSGIPythonPath "C:\Python10\Lib\site-packages"
```

Modificar Virtual host


```bash
#poner el puerto que uses
Listen 8095

## para que funcione el virtual host seria en el mismo puerto 
<VirtualHost *:8095>
ServerAlias www.nomina-prima.com.mx
ServerName nomina-prima.com.mx
ServerAdmin info@nomina-prima.com.mx
WSGIScriptAlias / "C:/Apache24NominaPrima/htdocs/src/nomina_prima/nomina_prima/wsgi_windows.py"
  <Directory "C:/Apache24NominaPrima/htdocs/src/nomina_prima/nomina_prima/">
    <Files wsgi_windows.py>
		Require all granted
    </Files>
		Require all granted
  </Directory>

Alias /static/ "C:/Apache24NominaPrima/htdocs/src/nomina_prima/content/static/"
  <Directory "C:/Apache24NominaPrima/htdocs/src/nomina_prima/content/static/">
    Require all granted
  </Directory>

ErrorLog "C:/Apache24NominaPrima/htdocs/src/nomina_prima/logs/apache.error.log"
CustomLog "C:/Apache24NominaPrima/htdocs/src/nomina_prima/logs/apache.custom.log" common
</VirtualHost>


```


Sin virtualhost

```bash
#poner el puerto que uses
Listen 8095


LoadFile "C:/Python310/python310.dll"
LoadModule wsgi_module "C:/Python310/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp310-win_amd64.pyd"
WSGIPythonHome "C:/Python310"
WSGIPythonPath "C:\Python310\Lib\site-packages"

# Configuración directa (SIN VirtualHost)
WSGIScriptAlias / "C:/Apache24NominaPrima/htdocs/src/nomina_prima/nomina_prima/wsgi_windows.py"

<Directory "C:/Apache24NominaPrima/htdocs/src/nomina_prima/nomina_prima/">
    Require all granted
</Directory>

Alias /static/ "C:/Apache24NominaPrima/htdocs/src/nomina_prima/content/static/"
<Directory "C:/Apache24NominaPrima/htdocs/src/nomina_prima/content/static/">
    Require all granted
</Directory>

ErrorLog "C:/Apache24NominaPrima/htdocs/src/nomina_prima/logs/apache.error.log"
CustomLog "C:/Apache24NominaPrima/htdocs/src/nomina_prima/logs/apache.custom.log" common



```



en el archivo
```bash
nomina-prima\src\nomina_prima\nomina_prima\settings.py
```

 permitir el acceso a los ips
```bash
#ALLOWED_HOSTS = []

ALLOWED_HOSTS = [
    'www.nomina-prima.com.mx',
    'nomina-prima.com.mx',
    'localhost',
    '127.0.0.1',
]

```


## Ejecutar localmente
ir al directorio donde se tienen la aplicacion

ejecutar entorno virtual si se tiene o si no se tiene una instalacion de python global
```bash
venv\Scripts\activate
```
debe de mostrar que esta activo

```bash
(venv) C:\nomina-prima\src\nomina_prima>
```


Ejecutar coleccion de staticos
```bash
\nomina_prima\manage.py collectstatic
```


Hacer la migracion

```bash
<Directorio>\nomina_prima\python manage.py makemigrations

```

Migrar 

```bash
<Directorio>\nomina_prima\python manage.py migrate
```
Ejecutar el projecto:

```bash
<Directorio>nomina_prima\python manage.py runserver
```



Navegar al sitio web del projecto:

```bash
www.nomina-prima.com.mx
```



para cerrar la aplicacion
```bash
Ctrl+C
```

### 1. 6. Ejecutar servidor

```bash
python manage.py runserver
```

👉 Acceder: http://127.0.0.1:8000

si es instalacion inicial se debe de ver el django 
```bash
The install worked successfully! Congratulations!
View release notes for Django 5.2

You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.

Django
```
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
