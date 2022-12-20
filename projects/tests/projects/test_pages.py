# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse_lazy
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.support.select import Select
# from webdriver_manager.firefox import GeckoDriverManager


# class CreateProjectPage(StaticLiveServerTestCase):
#     def setUp(self):
#         self.options = webdriver.FirefoxOptions()
#         self.options.headless = True
#         self.driver = webdriver.Firefox(
#             service=FirefoxService(GeckoDriverManager().install()), options=self.options)
#         self.url = reverse_lazy('projects:registrar')

#     def test_preenche_todos_os_campos_e_submete_com_sucesso(self):
#         self.driver.get(f"{self.live_server_url}{self.url}")

#         # preenche os campos do formulario
#         self.driver.find_element(By.NAME, 'nome').send_keys("Projeto 1")
#         self.driver.find_element(
#             By.NAME, 'descricao').send_keys("Um novo projeto")
#         self.driver.find_element(
#             By.NAME, 'data_inicio').send_keys("2022-12-12")
#         self.driver.find_element(
#             By.NAME, 'data_termino').send_keys("2022-12-31")
#         Select(self.driver.find_element(By.NAME, 'situacao')
#                ).select_by_visible_text("Iniciado")

#         # envia o formulario
#         submitBtn = self.driver.find_element(By.CSS_SELECTOR, "form button")
#         submitBtn.send_keys(Keys.PAGE_DOWN)
#         submitBtn.send_keys(Keys.PAGE_DOWN)
#         submitBtn.click()

#         url_redirecionamento = f"{self.live_server_url}{reverse_lazy('projects:inicio')}"
#         self.assertEqual(self.driver.current_url, url_redirecionamento)

#     def tearDown(self):
#         self.driver.quit()
