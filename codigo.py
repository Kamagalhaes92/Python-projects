#Step by step
# 1.website
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


#install pyautogui
import pyautogui
import time
pyautogui.PAUSE= 0.5

#pyautogui.click -Simulates a mouse click at the current cursor position.
#pyautogui.write -It writes
#pyautogui.press -It press a key on the keyboard exemple pyautogui.press("win")
#pyautogui.hotkey - it press two keys at the same time (example: Ctrl C)


#open web browser chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
   
#enter on the website
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#wait for website to load
time.sleep(4)

#Log in
pyautogui.click(x=618, y=466)
pyautogui.write("karinemagalhaes92@gmail.com")  
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
#Open product database
# pip install pandas numpy openpyxl
# "tabula" convert pdf files to pandas
#import pandas, library that allows you to work with data base
import pandas as pd
file_path = "produtos.csv"
product_table = pd.read_csv(file_path)


#Register a product
#Repeat until it has finished with loops

for line in product_table.index:

    code = str(product_table.loc[line, "codigo"])

    pyautogui.click(x=601, y=325)

    pyautogui.write(code)
    pyautogui.press("tab")
    #products's brand
    pyautogui.write(str(product_table.loc[line, "marca"]))
    pyautogui.press("tab")
    #type
    pyautogui.write(str(product_table.loc[line, "tipo"]))
    pyautogui.press("tab")
    #category
    pyautogui.write(str(product_table.loc[line, "categoria"]))
    pyautogui.press("tab")
    #price
    pyautogui.write(str(product_table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    #cost
    pyautogui.write(str(product_table.loc[line, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = str(product_table.loc[line, "obs"])
    #if obs is different than "nan" add obs to database
    if obs != "nan" :
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


