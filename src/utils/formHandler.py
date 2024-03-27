import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def fill_in_form(browser,web,dataFrame=None,row=None,placa=None,cedula=None):
    
    _placa = ""
    _cedula = ""
    
    if placa is not None and cedula is not None:
        _placa = placa
        _cedula = cedula
        index = 1
    if dataFrame is not None and row is not None:
        _placa = dataFrame.cell(row=row, column=2).value
        _cedula = dataFrame.cell(row=row, column=3).value
        index = row-1
    
    
    browser.get(web)
    browser.switch_to.frame("MSOPageViewerWebPart_WebPartWPQ2")
    browser.maximize_window()
    cedula_web_input = browser.find_element(By.ID, "cphMain_txtRNC")
    placa_web_input = browser.find_element(By.ID, "cphMain_txtPlaca")
    button = browser.find_element(By.NAME, "ctl00$cphMain$btnConsultar")

    cedula_web_input.click()
    cedula_web_input.clear()
    cedula_web_input.send_keys(_cedula)
    time.sleep(3)
    placa_web_input.click()
    placa_web_input.clear()
    placa_web_input.send_keys(_placa)
    time.sleep(2)
    button.click()
    time.sleep(2)
    
    try:
        placa_web_table= browser.find_element(
            By.XPATH, "//*[@id='cphMain_gvDetallesPlaca']/tbody/tr/td[1]").get_attribute("innerHTML")
        marca_web_table = browser.find_element(
            By.XPATH, "//*[@id='cphMain_gvDetallesPlaca']/tbody/tr/td[2]").get_attribute("innerHTML")
        modelo_web_table = browser.find_element(
            By.XPATH, "//*[@id='cphMain_gvDetallesPlaca']/tbody/tr/td[3]").get_attribute("innerHTML")
        color_web_table = browser.find_element(
            By.XPATH, "//*[@id='cphMain_gvDetallesPlaca']/tbody/tr/td[4]").get_attribute("innerHTML")
        anio_web_table = browser.find_element(
            By.XPATH, "//*[@id='cphMain_gvDetallesPlaca']/tbody/tr/td[5]").get_attribute("innerHTML")
        estado_web_table = browser.find_element(
            By.XPATH, "//*[@id='cphMain_gvDetallesPlaca']/tbody/tr/td[6]").get_attribute("innerHTML")
            
    except NoSuchElementException: 
        placa_web_table = _placa
        marca_web_table = "Error"
        modelo_web_table = "Error"
        color_web_table = "Error"
        anio_web_table = "Error"
        estado_web_table = "Error"
        
    return [index,placa_web_table, marca_web_table, modelo_web_table, color_web_table, anio_web_table, estado_web_table]