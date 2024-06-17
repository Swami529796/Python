import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
 
element_list = []
 
for page in range(1, 3, 1):
   
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
    driver = webdriver.Chrome()
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")
    pageno = driver.find_element(By.XPATH,f"/html/body/div[1]/div[3]/div/div[2]/div[2]/nav/ul/li[2]/span")
 
    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text,pageno.text])
 
with xlsxwriter.Workbook('output_multiplepage.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
 
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)
 
driver.close()