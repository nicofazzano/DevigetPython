from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDeviget():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_deviget_challenge(self):
        # Se instancia el driver, se ingresa a la web, se busca el producto y va a la pagina 2
        driver = self.driver
        driver.get("https://www.mercadolibre.com.ar")
        driver.find_element_by_class_name("nav-search-input").send_keys("iphone")
        driver.find_element_by_class_name("nav-search-input").submit()
        driver.find_element_by_xpath("//*[@class='andes-pagination ']//*[text()='2']").click()

        # Se ubica la segunda publicacion referida a la busqueda y si el titulo contiene "iPhone" ingresa, si no rompe el test
        publicacion = driver.find_element_by_css_selector("[id='searchResults'] [class='results-item highlighted article stack product ']:nth-child(2) h2 a")
        if ("iPhone" in publicacion.text):
            publicacion.click()
        else:
            assert False, "La segunda publicacion de la segunda pagina de resultados no es un iPhone"

        # Si el titulo del producto contiene "iPhone" verifica que el precio no este vacio, que este el boton de comprar y que este la galeria de imagenes
        if ("iPhone" in driver.find_element_by_class_name("item-title__primary ").text):
            assert driver.find_element_by_css_selector("[id='productInfo'] [class='price-tag-fraction']").text is not None
            botonComprar = driver.find_element_by_id("BidButtonTop")
            assert "Comprar ahora" in botonComprar.get_attribute("value")
            assert driver.find_element_by_css_selector("[class='gallery-content item-gallery__wrapper']").is_displayed()
        else:
            return False, "El titulo del producto no contiene 'iPhone', verificar que se cargo en la web"

