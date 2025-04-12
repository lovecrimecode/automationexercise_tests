# Criterios de Aceptación

## PA-01: Registro de Usuario

**Criterios de aceptación Funcionales:**
- El sistema debe permitir el registro con nombre, correo electrónico, contraseña, dirección y número de móvil.
- Al registrar correctamente, se debe mostrar el mensaje “ACCOUNT CREATED!”.
- El sistema debe almacenar los datos ingresados de forma segura.

**Criterios de aceptación No funcionales:**
- El tiempo de carga del formulario no debe superar los 2 segundos.
- El formulario debe ser accesible desde navegadores modernos (Chrome, Firefox, Edge).

**De rechazo:**
- Si los campos obligatorios están vacíos, se debe impedir el registro.
- Si el correo ya está registrado, se debe mostrar un mensaje de error.

---

## PA-02: Iniciar sesión

**Criterios de aceptación Funcionales:**
- El usuario debe poder iniciar sesión con correo y contraseña válidos.
- Al iniciar sesión, debe aparecer el texto “Logged in as”.
- Al cerrar sesión, se debe redirigir a la página de inicio.

**Criterios de aceptación No funcionales:**
- La autenticación debe completarse en menos de 2 segundos.
- El formulario debe estar protegido contra ataques de fuerza bruta.

**De rechazo:**
- Si el correo o la contraseña son incorrectos, se debe impedir el acceso y mostrar un mensaje de error.
- Si falta algún campo, el botón de login debe estar deshabilitado.

---

## PA-03: Búsqueda de productos

**Criterios de aceptación Funcionales:**
- El sistema debe permitir ingresar texto en el campo de búsqueda.
- Al buscar "shirt", debe mostrarse la sección "Searched Products".

**Criterios de aceptación No funcionales:**
- La respuesta a la búsqueda debe cargarse en menos de 2 segundos.
- El sistema debe poder manejar búsquedas frecuentes sin errores.

**De rechazo:**
- Si se busca un término inexistente, debe mostrarse un mensaje como “No se encontraron resultados”.
- Si se intenta buscar sin escribir nada, no se debe ejecutar la búsqueda.

---

## PA-04: Agregar producto al carrito

**Criterios de aceptación Funcionales:**
- El sistema debe mostrar un botón “Add to cart” en cada producto.
- Al hacer clic, debe mostrarse un modal de confirmación.
- El carrito debe reflejar el producto añadido correctamente.

**Criterios de aceptación No funcionales:**
- El modal debe abrirse en menos de 1 segundo tras hacer clic.
- El sistema debe seguir siendo funcional si se agregan múltiples productos rápidamente.

**De rechazo:**
- Si el producto ya está en el carrito, se debe evitar el duplicado o notificarlo.
- Si el botón falla, debe mostrarse un mensaje de error amigable.

---

## PA-05: Ver detalle del producto

**Criterios de aceptación Funcionales:**
- El usuario debe poder acceder al detalle de un producto desde la lista.
- El detalle debe mostrar nombre, categoría y demás información clave.

**Criterios de aceptación No funcionales:**
- El detalle del producto debe cargarse en menos de 2 segundos.
- Debe ser legible y adaptarse a distintos tamaños de pantalla.

**De rechazo:**
- Si el producto no existe, debe mostrarse un mensaje de error o redirección.
- Si hay un error en la carga, se debe mostrar una alerta clara al usuario.
