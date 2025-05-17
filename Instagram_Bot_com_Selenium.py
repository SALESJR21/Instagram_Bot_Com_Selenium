from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random

class InstagramBot:
    def __init__(self, username, password):
        # Inicia Chrome com WebDriver Manager
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.username = username  # Usuário do Instagram
        self.password = password  # Senha do Instagram

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')  # Acessa página principal

        # Aceita cookies se aparecer (botões: "Permitir cookies" ou "Aceitar tudo")
        try:
            cookie_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'cookies') or contains(text(),'Permitir') or contains(text(),'Aceitar')]")
            ))
            cookie_btn.click()
        except NoSuchElementException:
            pass  # Ignora se não aparecer

        # Preenche usuário e senha com espera explícita
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'username'))
        ).send_keys(self.username)
        driver.find_element(By.NAME, 'password').send_keys(self.password)

        # Clica em login e espera próxima página
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//nav"))  # Verifica barra de navegação
        )

        # Fecha pop-up de salvar login
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Agora não') or contains(text(),'Not now')]")
            )).click()
        except NoSuchElementException:
            pass
        sleep(2)

    def follow_followers_of(self, target_user, max_follows=6):
        driver = self.driver
        driver.get(f'https://instagram.com/{target_user}')  # Perfil alvo
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'header'))
        )

        # Clica no link de seguidores
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'seguidores'))
        ).click()
        modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )
        sleep(1)

        follow_count = 0
        last_height = -1
        attempts = 0

        # Rola e clica em seguir até atingir max_follows
        while follow_count < max_follows and attempts < 5:
            buttons = modal.find_elements(By.XPATH, ".//button[text()='Seguir']")
            for btn in buttons[follow_count:max_follows]:
                try:
                    btn.click()
                    follow_count += 1
                    sleep(random.uniform(2, 4))  # Pausa aleatória
                except (ElementClickInterceptedException, NoSuchElementException):
                    continue

            # Rola lista de seguidores
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(random.uniform(1.5, 2.5))

            new_height = driver.execute_script("return arguments[0].scrollTop", modal)
            if new_height == last_height:
                attempts += 1
            last_height = new_height

        print(f"Total de novos seguidores: {follow_count}")

    def close(self):
        # Fecha navegador
        self.driver.quit()

# Exemplo de uso
bot = InstagramBot(username='SEU_USUARIO', password='SUA_SENHA')
bot.login()
bot.follow_followers_of('usuario_alvo', max_follows=6)
bot.close()