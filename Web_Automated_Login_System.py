from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Link ke website yang ingin diotomatisasi login
website_link = "...."
# Username dan password untuk login
username = "...."
password = "...."

# Elemen untuk input username, password, dan tombol submit
element_for_username = "username"
element_for_password = "password"
element_for_submit = "btn btn-primary btn-block mt-3"

# Inisialisasi browser
browser = webdriver.Chrome()  # Pastikan Anda memiliki ChromeDriver yang sesuai
browser.get(website_link)

try: #Silahkan custom elementnya bedasarkan website yang akan digunakan
    # Tunggu hingga elemen username tersedia dan masukkan username
    username_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, element_for_username))
    )
    username_element.send_keys(username)

    # Tunggu hingga elemen password tersedia dan masukkan password
    password_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, element_for_password))
    )
    password_element.send_keys(password)

    # Tunggu hingga tombol submit tersedia dan klik
    signInButton = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f"button.{element_for_submit.replace(' ', '.')}"))
    )
    signInButton.click()

    # Menunggu input dari pengguna untuk menutup browser
    input("Tekan Enter untuk menutup browser...")

except Exception as e:
    print(f"Some error occurred: {e}")

# Browser akan tetap terbuka sampai pengguna menekan Enter
