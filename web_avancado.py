import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def configurar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def parte_1_selects(driver):
    logging.info("Iniciando Parte 1: Selects")
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    wait = WebDriverWait(driver, 10)
    elemento_select = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    dropdown = Select(elemento_select)
    
    for opcao in dropdown.options:
        logging.info(f"Opção: {opcao.text} (valor: {opcao.get_attribute('value')})")
        
    dropdown.select_by_index(2)
    
    selecionada = dropdown.first_selected_option.text
    assert selecionada == "Option 2", f"Esperado 'Option 2', obtido '{selecionada}'"
    logging.info("Parte 1 validada com sucesso: Option 2 selecionada.")

def parte_2_alerts(driver):
    logging.info("Iniciando Parte 2: Alerts JS")
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    
    botao_alert = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
    botao_alert.click()
    alerta = wait.until(EC.alert_is_present())
    logging.info(f"Texto do alerta: {alerta.text}")
    alerta.accept()
    
    botao_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']")))
    botao_confirm.click()
    alerta_confirm = wait.until(EC.alert_is_present())
    alerta_confirm.dismiss()
    
    resultado_confirm = wait.until(EC.presence_of_element_located((By.ID, "result"))).text
    assert "You clicked: Cancel" in resultado_confirm, f"Inesperado: {resultado_confirm}"
    logging.info(f"JS Confirm validado: {resultado_confirm}")
    
    ra_estudante = "6326314"
    botao_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']")))
    botao_prompt.click()
    
    alerta_prompt = wait.until(EC.alert_is_present())
    alerta_prompt.send_keys(ra_estudante)
    alerta_prompt.accept()
    
    resultado_prompt = wait.until(EC.presence_of_element_located((By.ID, "result"))).text
    assert ra_estudante in resultado_prompt, f"RA não encontrado no resultado: {resultado_prompt}"
    logging.info(f"JS Prompt validado com RA: {resultado_prompt}")

def parte_3_iframes(driver):
    logging.info("Iniciando Parte 3: Iframes")
    driver.get("https://the-internet.herokuapp.com/iframe")
    wait = WebDriverWait(driver, 10)
    
    iframe_elemento = wait.until(EC.presence_of_element_located((By.CSSSelector, "div.tox-edit-area > iframe, iframe#mce_0_ifr")))
    driver.switch_to.frame(iframe_elemento)
    
    corpo_editor = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    corpo_editor.clear()
    corpo_editor.send_keys("Automatizando com sucesso - RA: 6326314")
    
    driver.switch_to.default_content()
    
    cabecalho = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
    assert "An iFrame containing the TinyMCE WYSIWYG Editor" in cabecalho, f"Cabeçalho inválido: {cabecalho}"
    logging.info(f"Retorno ao DOM raiz validado: {cabecalho}")

def parte_4_windows(driver):
    logging.info("Iniciando Parte 4: Troca de Abas / Janelas")
    driver.get("https://the-internet.herokuapp.com/windows")
    wait = WebDriverWait(driver, 10)
    
    handle_original = driver.current_window_handle
    
    link_nova_janela = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    link_nova_janela.click()
    
    wait.until(EC.number_of_windows_to_be(2))
    
    todos_handles = driver.window_handles
    handle_novo = [h for h in todos_handles if h != handle_original][0]
    
    driver.switch_to.window(handle_novo)
    
    texto_nova_pagina = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
    assert texto_nova_pagina == "New Window", f"Esperado 'New Window', obtido '{texto_nova_pagina}'"
    logging.info("Nova aba validada com sucesso.")
    
    driver.close()
    driver.switch_to.window(handle_original)
    
    assert len(driver.window_handles) == 1, "Deveria existir apenas 1 aba aberta."
    assert "The Internet" in driver.title, f"Título incorreto: {driver.title}"
    logging.info("Retorno à aba original validado com sucesso.")

def executar_laboratorio():
    driver = configurar_driver()
    try:
        parte_1_selects(driver)
        parte_2_alerts(driver)
        parte_3_iframes(driver)
        parte_4_windows(driver)
        logging.info("🎉 Laboratório 09 executado com 100% de sucesso!")
    except Exception as e:
        logging.error(f"❌ Erro durante a execução: {e}")
        raise
    finally:
        driver.quit()
        logging.info("Driver encerrado.")

if __name__ == "__main__":
    executar_laboratorio()