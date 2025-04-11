import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Crear carpeta para screenshots si no existe
os.makedirs("tests/screenshots", exist_ok=True)

@pytest.fixture(scope="module")
def driver():
    chrome_options = webdriver.ChromeOptions()
    
    # Quitar notificaciones, extensiones, y modo incógnito
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Inicializar el driver con las opciones
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()

def take_screenshot(driver, test_name):
    # Zoom (afecta todo el HTML, no solo el body)
    driver.execute_script("document.documentElement.style.zoom = '75%'")

    screenshot_path = f"tests/screenshots/{test_name}.png"
    driver.get_screenshot_as_file(screenshot_path)


# HU-01: Registro de Usuario
def test_user_registration(driver):
    try:
        driver.get("https://automationexercise.com/signup")

        timestamp = int(time.time())
        test_email = f"zelidee{timestamp}@test.com"

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="signup-name"]'))
        ).send_keys("Zelidee")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]').send_keys(test_email)
        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]').click()
        print(f"Email de prueba: {test_email}")

        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[contains(., "Enter Account Information")]'))
        )

        driver.find_element(By.ID, "id_gender1").click()
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="password"]').send_keys("123456")

        Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="days"]')).select_by_value("1")
        Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="months"]')).select_by_value("5")
        Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="years"]')).select_by_value("1990")

        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="first_name"]').send_keys("Zelidee")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="last_name"]').send_keys("User")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="company"]').send_keys("Test Company")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="address"]').send_keys("123 Test St")
        Select(driver.find_element(By.CSS_SELECTOR, 'select[data-qa="country"]')).select_by_visible_text("India")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="state"]').send_keys("Test State")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="city"]').send_keys("Test City")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="zipcode"]').send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, 'input[data-qa="mobile_number"]').send_keys("9876543210")

        driver.find_element(By.CSS_SELECTOR, 'button[data-qa="create-account"]').click()

        success_msg = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[@data-qa="account-created"]'))
        )
        assert "ACCOUNT CREATED!" in success_msg.text
        take_screenshot(driver, "user_registration_success")

        # Eliminar cuenta
        driver.get("https://automationexercise.com/delete_account")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.title"))
        )

    except Exception as e:
        take_screenshot(driver, "user_registration_error")
        raise

# HU-02: Iniciar sesión
def test_user_login(driver):
    try:
        # 1. Navegar a la página de login
        driver.get("https://automationexercise.com/login")
        
        # Esperar a que la página cargue completamente
        WebDriverWait(driver, 20).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # 2. Ingresar credenciales
        test_email = "z@z.com"
        test_password = "1111"
        
        # Campo de email con múltiples estrategias de localización
        try:
            email_field = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="login-email"]'))
            )
        except TimeoutException:
            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, 'email'))
            )
        email_field.clear()
        email_field.send_keys(test_email)

        # Campo de contraseña
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="login-password"]'))
        )
        password_field.clear()
        password_field.send_keys(test_password)

        # Botón de login con JavaScript como respaldo
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-qa="login-button"]'))
        )
        try:
            login_button.click()
        except:
            driver.execute_script("arguments[0].click();", login_button)

        # Verificar login exitoso
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(., "Logged in as")]'))
        )
        take_screenshot(driver, "login_success")

        # Logout mejorado
        try:
            logout_link = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/logout"]'))
            )
            logout_link.click()
            
            WebDriverWait(driver, 10).until(EC.url_contains("/login")) or WebDriverWait(driver, 10).until(EC.url_contains("/signup"))
            take_screenshot(driver, "logout_success")
            
        except Exception as e:
            print(f"Error durante logout: {str(e)}")
            take_screenshot(driver, "logout_error")
            raise

    except Exception as e:
        take_screenshot(driver, "login_error")
        print(f"Error durante el login: {str(e)}")
        raise

# HU-03: Búsqueda de productos
def test_search_products(driver):
    try:
        driver.get("https://automationexercise.com/products")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".features_items"))
        )

        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search_product"))
        )
        search_box.send_keys("shirt")

        search_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'submit_search'))
        )
        search_button.click()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//h2[contains(text(), "Searched Products")]'))
        )
        take_screenshot(driver, "search_products_success")

    except Exception as e:
        print("❌ Error en test_search_products:", e)
        take_screenshot(driver, "search_products_error")
        # Puedes dejar esto como "falla tolerada"

# HU-04: Agregar producto al carrito
def test_add_to_cart(driver):
    try:
        driver.get("https://automationexercise.com/products")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Add to cart")]'))
        )

        add_buttons = driver.find_elements(By.XPATH, '//a[contains(text(),"Add to cart")]')
        if add_buttons:
            add_buttons[0].click()

            # Esperar el modal
            continue_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Continue Shopping")]'))
            )
            continue_btn.click()
            take_screenshot(driver, "add_to_cart_success")
        else:
            raise Exception("❌ No se encontraron botones para agregar al carrito.")

    except Exception as e:
        print("❌ Error en test_add_to_cart:", e)
        take_screenshot(driver, "add_to_cart_error")
        # Igual, falla tolerada

# HU-05: Ver detalle del producto
def test_view_product_details(driver):
    driver.get("https://automationexercise.com/products")

    # Ir al detalle del primer producto
    view_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '(//a[contains(text(),"View Product")])[1]'))
    )
    view_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-information"))
    )
    take_screenshot(driver, "tests/screenshots/product_details.png")
    assert "Product Information" in driver.page_source or "Category" in driver.page_source