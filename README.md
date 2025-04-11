# 📘 Proyecto de Pruebas Automatizadas con Selenium - AutomationExercise

Este proyecto contiene pruebas automatizadas desarrolladas en **C#** utilizando **Selenium WebDriver**, ejecutadas sobre el sitio [automationexercise.com](https://automationexercise.com/), como parte de una entrega académica.

## 🧪 Historias de Usuario Automatizadas

1. ✅ Como usuario, quiero iniciar sesión para acceder a mi cuenta.
2. ❌ Como usuario, quiero buscar productos para visualizar resultados relacionados. *(falla por timeout de búsqueda)*
3. ❌ Como usuario, quiero agregar un producto al carrito para comprarlo después. *(falla al esperar el botón "Continue Shopping")*
4. ❌ Como usuario, quiero ver los productos en oferta para aprovechar descuentos. *(prueba no incluida o con errores)*
5. ❌ Como usuario, quiero acceder al detalle de un producto para ver más información. *(prueba no incluida o con errores)*

## ⚙️ Tecnologías Utilizadas

- Lenguaje: **C#**
- Framework: **NUnit**
- Automatización: **Selenium WebDriver**
- Navegador: **Google Chrome**
- Librerías extra:
  - `Selenium.Support` (para WebDriverWait y ExpectedConditions)
  - `ExtentReports` (para generación de reportes en HTML)

## 📸 Funcionalidades del Proyecto

- Capturas automáticas de pantalla en cada prueba.
- Reporte HTML detallado generado tras la ejecución.
- Pruebas diseñadas con `WebDriverWait` y `ExpectedConditions`.

## 🗂 Estructura del Proyecto

