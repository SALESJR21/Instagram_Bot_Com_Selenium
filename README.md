# Instagram Bot com Selenium - Guia de Instalação e Uso

## 🤖 O que é o Instagram Bot?

Este é um bot automatizado desenvolvido em Python que utiliza a biblioteca Selenium para interagir com o Instagram. Ele é capaz de:
- Realizar login automático
- Navegar até perfis específicos
- Acessar listas de seguidores
- Seguir automaticamente uma quantidade definida de usuários

## 📋 Pré-requisitos

1. **Python 3.8 ou superior**
   - [Baixe o Python aqui](https://www.python.org/downloads/)
   - Durante a instalação, marque a opção "Add Python to PATH"

2. **Google Chrome**
   - [Baixe a última versão do Chrome](https://www.google.com/chrome/)

## 🛠️ Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/Instagram_Bot_Com_Selenium.git
cd Instagram_Bot_Com_Selenium
```

2. **Crie e ative um ambiente virtual**
```bash
python -m venv venv
```

Para Windows:
```bash
venv\Scripts\activate
```

Para Linux/macOS:
```bash
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install selenium webdriver-manager
```

## ⚙️ Configuração

1. Abra o arquivo `instagram_bot.py`
2. Localize a seção de configurações no método `main()`:
```python
# Configurações
USERNAME = "seu_usuario"      # Substitua com seu usuário do Instagram
PASSWORD = "sua_senha"        # Substitua com sua senha
PERFIL_ALVO = "perfil_alvo"  # Perfil que deseja seguir os seguidores
QUANTIDADE_SEGUIR = 10        # Quantidade de usuários para seguir
```

## 🚀 Como Usar

1. **Execute o bot**
```bash
python instagram_bot.py
```

2. **O que esperar durante a execução:**
   - O bot abrirá uma janela do Chrome
   - Fará login automaticamente no Instagram
   - Navegará até o perfil alvo
   - Abrirá a lista de seguidores
   - Começará a seguir os usuários conforme configurado

## ⚠️ Observações Importantes

1. **Limites do Instagram**
   - O bot inclui delays aleatórios para simular comportamento humano
   - Recomenda-se não seguir muitos usuários em um curto período
   - Use com moderação para evitar bloqueios da conta

2. **Segurança**
   - Nunca compartilhe suas credenciais
   - Evite commits com suas informações de login
   - Use variáveis de ambiente ou arquivo de configuração separado para credenciais

3. **Manutenção**
   - O Instagram atualiza sua interface periodicamente
   - Pode ser necessário ajustar os seletores XPath ocasionalmente

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:
1. Faça um Fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🐛 Problemas Conhecidos e Soluções

Se encontrar o erro "ChromeDriver não encontrado":
```bash
pip install --upgrade webdriver-manager
```

Para outros problemas, verifique se:
- Chrome está atualizado
- Todas as dependências estão instaladas
- As credenciais estão corretas
- A conexão com a internet está estável

        
