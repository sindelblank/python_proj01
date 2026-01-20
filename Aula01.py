# Link da aula: https://www.youtube.com/watch?v=0GDt-6H9NWM
# Link dos arquivos: https://drive.google.com/drive/folders/1ERaraa4ZeXWFWo4K8oNJi4kY6aGZYdzw

# Registrar dados de produtos em um sistema web automaticamente

from playwright.sync_api import sync_playwright
import pandas as pd

# Variáveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "teste@email.com"
senha = "senha12345"

# Passo 1: Ler base de dados (ANTES)
tabela = pd.read_csv("produtos.csv")
tabela = tabela.fillna("(vazio)")

with sync_playwright() as pw:
    # Passo 2: Abrir navegador
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    # Passo 3: Login
    page.goto(link)
    page.locator("#email").fill(email)
    page.locator("#password").fill(senha)
    page.click("button[type='submit']")

    # Passo 4: Preencher produtos (LOOP CORRETO)
    for linha in tabela.itertuples():
        page.locator("#codigo").fill(str(linha.codigo))
        page.locator("#marca").fill(linha.marca)
        page.locator("#tipo").fill(linha.tipo)
        page.locator("#categoria").fill(str(linha.categoria))
        page.locator("#preco_unitario").fill(str(linha.preco_unitario))
        page.locator("#custo").fill(str(linha.custo))
        page.locator("#obs").fill(str(linha.obs))

        page.click("button[type='submit']")

    input("Pressione Enter para fechar o navegador...")
    browser.close()
