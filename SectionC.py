from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()

navegador.get("https://finance.yahoo.com/quote/BTC-EUR/history/")

dia1 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[1]/span').text
dia2 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[1]/span').text
dia3 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[3]/td[1]/span').text
dia4 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[4]/td[1]/span').text
dia5 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[5]/td[1]/span').text
dia6 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[6]/td[1]/span').text
dia7 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[7]/td[1]/span').text
dia8 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[8]/td[1]/span').text
dia9 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[9]/td[1]/span').text
dia10 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[10]/td[1]/span').text

close1 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span').text
close2 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[5]/span').text
close3 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[3]/td[5]/span').text
close4 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[4]/td[5]/span').text
close5 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[5]/td[5]/span').text
close6 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[6]/td[5]/span').text
close7 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[7]/td[5]/span').text
close8 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[8]/td[5]/span').text
close9 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[9]/td[5]/span').text
close10 = navegador.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[10]/td[5]/span').text


dados1 = dia1 + ';' + dia2 + ';' + dia3 + ';' + dia4 + ';' + dia5 + ';' + dia6 + ';' + dia7 + ';' + dia8 + ';' + dia9 + ';' + dia10

dados2 = close1 + ';' + close2 + ';' + close3 + ';' + close4 + ';' + close5 + ';' + close6 + ';' + close7 + ';' + close8 + ';' + close9 + ';' + close10
navegador.close()

arrayDate = dados1.split(';')
arrayClose = dados2.split(';')

df1 = pd.DataFrame(arrayDate)
df2 = pd.DataFrame(arrayClose)

df = pd.concat([df1, df2], axis=1)
df.to_csv("eur_btc_rates.csv", index=False, sep=";", header=['Date', 'BTC Closing Value'])
