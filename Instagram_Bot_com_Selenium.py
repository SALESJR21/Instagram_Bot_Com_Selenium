from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time

class InstagramBot:
    def __init__(self):
        # Configuração do Chrome
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def simular_delay_humano(self, min_delay=1, max_delay=3):
        """Simula um delay aleatório para parecer mais humano"""
        time.sleep(random.uniform(min_delay, max_delay))

    def login(self, username, password):
        """Realiza o login no Instagram"""
        try:
            # Abre o Instagram
            self.driver.get('https://www.instagram.com')
            self.simular_delay_humano(3, 5)
            
            # Aceita cookies se necessário
            try:
                cookie_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Permitir todos os cookies')]"))
                )
                cookie_button.click()
                self.simular_delay_humano()
            except:
                pass

            # Preenche as credenciais
            username_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

            username_field.send_keys(username)
            self.simular_delay_humano()
            password_field.send_keys(password)
            self.simular_delay_humano()

            # Clica no botão de login
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
            login_button.click()
            self.simular_delay_humano(4, 6)

            # Trata possíveis pop-ups após o login
            try:
                not_now_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))
                )
                not_now_button.click()
                self.simular_delay_humano()
            except:
                pass

            try:
                # Verifica se o login foi bem-sucedido procurando elementos da página inicial
                self.wait.until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/direct/inbox/')]"))
                )
                print("Login realizado com sucesso!")
                return True
            except:
                print("Falha na verificação do login. Verifique suas credenciais.")
                return False

        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return False

    def buscar_perfil(self, username):
        """Busca um perfil específico"""
        try:
            self.driver.get(f'https://www.instagram.com/{username}')
            self.simular_delay_humano(3, 5)
            return True
        except Exception as e:
            print(f"Erro ao buscar perfil: {e}")
            return False

    def abrir_seguidores(self):
        """Abre a lista de seguidores"""
        try:
            seguidores_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/followers')]"))
            )
            seguidores_link.click()
            # Aumenta o tempo de espera para garantir que a lista carregue
            self.simular_delay_humano(5, 7)
            return True
        except Exception as e:
            print(f"Erro ao abrir seguidores: {e}")
            return False

    def seguir_usuarios(self, quantidade):
        """Segue uma quantidade específica de usuários"""
        seguidos = 0
        tentativas = 0
        max_tentativas = quantidade * 2
    
        while seguidos < quantidade and tentativas < max_tentativas:
            try:
                # Espera a lista de seguidores carregar
                self.simular_delay_humano(2, 3)
                
                # Encontra botões de seguir com XPath mais abrangente
                botoes_seguir = self.wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, 
                    "//button[.//div[contains(text(), 'Seguir')] or contains(text(), 'Seguir')]"))
                )
    
                if not botoes_seguir:
                    print("Nenhum botão de seguir encontrado. Rolando a página...")
                    # Rola a página para carregar mais usuários
                    self.driver.execute_script("window.scrollBy(0, 500);")
                    self.simular_delay_humano(2, 3)
                    tentativas += 1
                    continue
    
                for botao in botoes_seguir:
                    if seguidos >= quantidade:
                        break
    
                    try:
                        # Rola até o botão
                        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
                        self.simular_delay_humano(1, 2)
    
                        # Verifica se o botão ainda está visível e clicável
                        if botao.is_displayed() and botao.is_enabled():
                            # Verifica se o texto do botão ainda é "Seguir"
                            texto_botao = botao.text.strip().lower()
                            if "seguir" in texto_botao and "seguindo" not in texto_botao:
                                botao.click()
                                seguidos += 1
                                print(f"Seguindo usuário {seguidos}/{quantidade}")
                                
                                # Delay aleatório entre 30-45 segundos para evitar bloqueios
                                self.simular_delay_humano(30, 45)
    
                    except Exception as e:
                        print(f"Erro ao seguir usuário específico: {e}")
                        continue
    
                # Se não conseguiu seguir ninguém nesta iteração
                if seguidos == 0:
                    # Rola a página para carregar mais usuários
                    self.driver.execute_script("window.scrollBy(0, 500);")
                    self.simular_delay_humano(2, 3)
                
                tentativas += 1
    
            except Exception as e:
                print(f"Erro durante o processo de seguir: {e}")
                tentativas += 1
    
        print(f"Processo finalizado. Seguiu {seguidos} usuários.")
        return seguidos

    def encerrar(self):
        """Encerra o navegador"""
        self.driver.quit()

def main():
    # Configurações
    USERNAME = "SUBSTITUA_PELO_SEU_USUARIO"
    PASSWORD = "SUBSTITUA_PELA_SEA_SENHA"
    PERFIL_ALVO = "SUBSTITUIA_PELO_USUARIO_ALVO"
    QUANTIDADE_SEGUIR = 10  # Ajuste conforme necessário

    # Inicializa o bot
    bot = InstagramBot()

    try:
        # Faz login
        if bot.login(USERNAME, PASSWORD):
            # Busca o perfil alvo
            if bot.buscar_perfil(PERFIL_ALVO):
                # Abre a lista de seguidores
                if bot.abrir_seguidores():
                    # Começa a seguir os usuários
                    bot.seguir_usuarios(QUANTIDADE_SEGUIR)
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    finally:
        bot.encerrar()

if __name__ == "__main__":
    main()