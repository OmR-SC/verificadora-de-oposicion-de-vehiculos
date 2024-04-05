[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# Verificadora de oposición de vehículos.

## Descripción

Aplicación Web que permite validar el estatus de vehiculos a fin de determinar están aptos para ser garantia de prendado en un banco o entidad financiera.

La aplicacion captara los datos, ya sea suministrados por el usuario, o directamente desde la base de datos. Con los datos ya obtenidos, el sistema de forma automática verificará el estado del/los vehículos en la DGII y procederá a actualizar la base de datos con la información obtenida.

#### Tecnologias utilizadas:

- Python
- Flask
- Jinja2
- Selemium
- Openpyxl
- JavaScript
- HTML
- CSS
- Excel

## Retos

- Se tuvo que aprender Python
- Se tuvo que aprender Flask
- Se tuvo que repasar el funcionaiento de Selenium
- Se tuvo que adaptar el uso de selenium con la página de la DGII, dado que esta utiliza iframes.
- Se tuvo que gestionar el como guardar los datos en el excel, sin utilizar muchos recursos.

## Razón

Realizado a fin de aumentar mis conocimientos en programación y como reto del curso de desarrollo de apps web del INFOTEP.

## Instalación

1-Clonar el repositorio

2-Inicializar en el entorno virtual

3-Instalar las dependencias

4-Iniciar la aplicación

```sh
cd verificadora-de-oposicion-de-vehiculos
python -m venv venv
venv\Scripts\activate
pip install Flask
pip install selenium
pip install webdriver-manager
pip install openpyxl
python app.py
```

> Nota: En caso de querer utilizar otro archivo excel diferente al del repositorio, la hoja o (Sheet) de este _(o en su defecto el archivo WorkSheet)_ este debe de ser creado utilizando la dependencia Openpyxl, por motivos de compatibilidad al utilizar la propiedad **max_row** y **max_column.**

## Como usar la aplicación:

La aplicacion consta de 2 paginas web:

- Una pagina del **formulario**
- Una pagina para **reporte**

#### Página del formulario:

- Dentro de la pagina de formulario el usuario puede insertar los datos necesarios para validar un vehiculo el cual previamente esté registrado en la base de datos (Excel), para ello debe de completar el formulario y hacer click en "Buscar".

- Otra funcion en la página es validar todos los vehiculos registrados en la base de datos, para ello el usuario debe de hacer click en el botón "Verificar todos".

- El usuario puede accedaer a la página de reportes haciendo click en el botón "Ver reporte"

#### Página del reporte:

Es una página web que permite ver los registros de vehículos almacenados en la base de datos.

### Rutas o Endpoints

Formulario para validar un vehículo: **_/_ [GET]**

Ruta que escucha los datos del formulario: **_/validar-datos_ [POST]**

Ruta para validar todos los vehículos: **_/validar-datos/todos_ [GET]**

Reporte de la base de datos: **_/reporte_ [GET]**

## Funcionamiento

Al momento de iniciar el proceso de validacion, el sistema llenará el formulario de la DGII a partir de los datos captados, ya sea a partir del usuario o de la base de datos.

Una vez que el sitio web de respuesta ante la solicitud, estos datos de la repsuesta son captados. Con los mismos el sistema buscará el respectivo vehiculo en la base de datos. De encontrarlo actualizará 2 campos; **Estado** e **Importante**.

#### Ejemplo:

| Estado   | Importante |
| -------- | ---------- |
| ACTIVO   | HALLAZGO   |
| &nbsp;   | ERROR      |
| INACTIVO | REVISION   |

En estado se le asignará el valor que ha sido dado por parte del respectivo campo en la tabla de respuesta dada por el sitio web de la DGII, campo con el mismo nombre; Estado.

En cambio "Importante" es basicamente un campo para detrerminaar que hacer en respuesta al ya mencionado campo "Estado", si el "Estado" es "ACTIVO", entonces en el campo "Importante" se registrará "HALLAZGO" como valor; si es "Error" se registrará "ERROR" haciendo referencia de que a este registro se le debe de dar especial atención, dado que el error puede ser por parte de la pagina de la DGII o de que no se encuentra el vehículo.

En caso de que el resultado de "Estado" no sea uno de estos, el valor del campo "Importante" será "REVISION" que hace referencia a que este vehiculo no está activo y por lo cual el prestamo probablement no procedería, a excepcion de que se realice una revisión manual que dictamine lo contrario.

> Importante: **El archivo excel debe de estar cerrado** al momento de realizar las operaciones, dado que para poder actualizar/guardar los datos en él es necesario que este no esté siendo ejecutado por una aplicacion, como por ejemplo Microsoft Excel.

---

## Licencia

MIT License

Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
