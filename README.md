# Proyecto de Pruebas Automatizadas con Selenium

Este repositorio contiene un conjunto de pruebas automatizadas usando **Selenium con Python** para el sitio [Automation Exercise](https://automationexercise.com/). Las pruebas cubren funcionalidades básicas como registro, login, búsqueda de productos, agregar al carrito y visualización de detalles de producto.

## Estructura del proyecto

```
📁 tests
├── 📁 screenshots       # Capturas automáticas de pruebas (éxito/error)
├── test_automation.py         # Archivo principal con los test cases
```

## Tecnologías y herramientas

- Python 3.10+
- Selenium WebDriver
- pytest
- webdriver-manager

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone (https://github.com/lovecrimecode/automationexercise_tests.git)
   cd tu_repositorio
   ```

2. Crear entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Hacer pruebas, generar reporte en la carpeta `tests/` y screenshots en la carpeta `tests/screenshots/`.
Desde la raíz del proyecto:
```bash
pytest --html=report.html
```

## Casos de prueba implementados

- ✅ Registro de usuario (HU-01)
- ✅ Login con credenciales válidas (HU-02)
- ✅ Búsqueda de productos (HU-03)
- ✅ Agregar producto al carrito (HU-04)
- ✅ Visualizar detalles de producto (HU-05)

## Capturas automáticas
Las capturas de pantalla se generan automáticamente en cada prueba, ya sea exitosa o fallida, con un zoom-out del 50% para mayor visibilidad.

## Notas adicionales
- Se deshabilitan extensiones y notificaciones del navegador para evitar interferencias.
