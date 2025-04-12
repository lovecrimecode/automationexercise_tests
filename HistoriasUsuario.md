# Proyecto: Automatización de pruebas funcionales con Selenium

## Pruebas automatizadas con Selenium en Python sobre la web [https://automationexercise.com](https://automationexercise.com) para validar funcionalidades comunes como navegación, registro, inicio de sesión, búsqueda y carrito de compras.

---

## Puntos de Automatización (PA) con criterios de aceptación y rechazo

### PA 1: Registro de usuario

**Criterios de aceptación funcionales:**

- Se debe mostrar correctamente el formulario de registro.
- Al ingresar datos válidos, la cuenta debe crearse exitosamente.
- El mensaje de confirmación debe decir “Account Created!”.

**Criterios de aceptación no funcionales:**

- El proceso no debe tardar más de 5 segundos.
- Debe funcionar correctamente en los navegadores modernos.

**Criterios de rechazo:**

- Si no se completan los campos obligatorios, no debe permitir el envío.
- Si el correo ya existe, debe mostrarse un mensaje de error.
- Si el formato del correo no es válido, el formulario no debe enviarse.

---

### PA 2: Inicio de sesión

**Criterios de aceptación funcionales:**

- Se deben poder ingresar las credenciales registradas.
- Al autenticarse correctamente, debe mostrarse “Logged in as [nombre]”.
- Si los datos son incorrectos, debe mostrarse un mensaje de error.

**Criterios de aceptación no funcionales:**

- La respuesta debe darse en menos de 3 segundos.
- Debe ser accesible mediante teclado.

**Criterios de rechazo:**

- No debe iniciar sesión si algún campo está vacío.
- No debe permitir caracteres inválidos.
- Si las credenciales son incorrectas, debe rechazarlas claramente.

---

### PA 3: Búsqueda de productos

**Criterios de aceptación funcionales:**

- Al escribir en la barra de búsqueda, deben mostrarse productos relacionados.
- Si no hay coincidencias, debe aparecer un mensaje como “Product not found”.

**Criterios de aceptación no funcionales:**

- La búsqueda debe responder en menos de 3 segundos.
- Debe aceptar tanto palabras completas como parciales.

**Criterios de rechazo:**

- Si se busca usando símbolos extraños, el sitio no debe romperse.
- Si no se escribe nada, no debe recargarse la página.
- Si no hay resultados, debe mostrarse un mensaje claro.

---

### PA 4: Agregar productos al carrito

**Criterios de aceptación funcionales:**

- Al hacer clic en “Add to cart”, debe mostrarse una confirmación.
- Los productos agregados deben aparecer correctamente en el carrito.
- Debe ser posible eliminar productos del carrito.

**Criterios de aceptación no funcionales:**

- El botón debe poder activarse con el teclado.
- El contenido del carrito debe mantenerse mientras se navega por el sitio.

**Criterios de rechazo:**

- No debe permitirse agregar productos sin seleccionar cantidad.
- No debe aceptar cantidades negativas.
- Si el producto está agotado, no debe permitirse su adición.

---

### PA 5: Ver detalle de un producto

**Criterios de aceptación funcionales:**

- Al hacer clic en un producto, debe cargarse la vista detallada.
- Debe mostrarse el nombre, precio, disponibilidad y descripción del producto.
- Desde esa vista, debe poder seleccionarse la cantidad y agregar al carrito.

**Criterios de aceptación no funcionales:**

- La página debe cargar en menos de 2 segundos.
- Debe visualizarse correctamente en dispositivos móviles.

**Criterios de rechazo:**

- Si se accede a un producto inexistente, debe mostrarse una página de error.
- Si no carga la información, debe mostrarse un mensaje de advertencia.
- No debe permitirse agregar al carrito sin indicar una cantidad.
