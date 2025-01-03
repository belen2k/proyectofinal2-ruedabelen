Sistema de Gestión de Estudiantes, Profesores y Notas
Este proyecto es una aplicación web desarrollada con Django que permite gestionar estudiantes, profesores y notas. Combina un diseño intuitivo con una estructura eficiente para administrar los registros académicos de manera fácil y segura.

Funcionalidades
Gestión de Usuarios
Registro de Usuarios: Permite la creación de cuentas para estudiantes y administradores con validaciones estrictas, como contraseñas seguras y formatos de correo válidos.
Inicio de Sesión: Los usuarios registrados pueden acceder al sistema ingresando sus credenciales.
Roles de Usuarios:
Estudiantes: Acceso a consultar sus notas, información personal y contacto con profesores.
Administradores: Gestión completa de registros (agregar, editar, eliminar) de estudiantes, profesores y notas.
Edición de Cuenta: Los usuarios pueden actualizar su correo electrónico y contraseña desde un menú de configuración personal.
Gestión Académica
Profesores:
Visualización de una lista completa con nombre, apellido y correo electrónico.
Posibilidad de agregar nuevos profesores al sistema.
Edición y eliminación de registros existentes.
Estudiantes:
Visualización de todos los estudiantes registrados con sus datos personales.
Agregar nuevos estudiantes al sistema y asignarles notas.
Edición y eliminación de registros existentes.
Notas:
Lista de todas las notas disponibles, incluyendo asignatura, código y profesor asignado.
Creación de nuevas notas y asociación a profesores específicos.
Edición y eliminación de notas existentes.
Páginas Informativas
Inicio: Bienvenida al sistema con una vista general de las funcionalidades.
Acerca de: Información sobre el proyecto, su creador y detalles de contacto.
Navegación Intuitiva
Barra de navegación adaptable según el rol del usuario:
Estudiantes: Opciones de "Inicio", "Notas", "Acerca de" y "Editar Cuenta".
Administradores: Opciones adicionales como "Agregar Profesor", "Agregar Estudiante", "Agregar Nota", y herramientas de edición directa.
Seguridad y Sesiones
Inicio/Cierre de Sesión: Fácil acceso para iniciar y cerrar sesiones de manera segura.
Permisos por Rol: Los administradores tienen permisos extendidos, mientras que los estudiantes tienen acceso limitado.
Protección de Datos: Validaciones en todos los formularios para asegurar la integridad y confidencialidad de los registros.
Tecnologías Utilizadas
Python y Django para el desarrollo del backend.
SQLite como base de datos por defecto.
Bootstrap 5 para el diseño responsive de la interfaz.
HTML5 y CSS3 para personalización adicional.


Pasos para Ejecutar el Proyecto
Clonar el repositorio:

bash
Copy code
git clone https://github.com/belen2k/tercera-preentrega-rueda-belen.git
Crear y activar un entorno virtual:

bash
Copy code
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
Instalar las dependencias:

bash
Copy code
pip install -r requirements.txt
Aplicar las migraciones:

bash
Copy code
python manage.py migrate
Iniciar el servidor:

bash
Copy code
python manage.py runserver
Acceder al sistema: Abra un navegador web y navegue a http://127.0.0.1:8000/.
