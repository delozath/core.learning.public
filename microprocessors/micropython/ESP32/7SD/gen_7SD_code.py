import pyperclip

import pandas as pd

path  = "/home/omarpr/git/cursos_uam/uea_lic_ib/ip/ESP32/7SD/"
fname = "gpio_7SD.csv"

gpio = pd.read_csv(path+fname)
gpio = {i[1].led:i[1].gpio for i in gpio.iterrows()}

SD7        = {}
SD7['all'] = (1<<gpio['A']) + (1<<gpio['B']) + (1<<gpio['C']) + (1<<gpio['D']) + (1<<gpio['E']) + (1<<gpio['F']) + (1<<gpio['G'])
SD7[0]     = (1<<gpio['A']) + (1<<gpio['B']) + (1<<gpio['C']) + (1<<gpio['D']) + (1<<gpio['E']) + (1<<gpio['F']) 
SD7[1]     = (1<<gpio['B']) + (1<<gpio['C'])
SD7[2]     = (1<<gpio['A']) + (1<<gpio['B']) + (1<<gpio['D']) + (1<<gpio['E']) + (1<<gpio['G'])
SD7[3]     = (1<<gpio['A']) + (1<<gpio['B']) + (1<<gpio['C']) + (1<<gpio['D']) + (1<<gpio['G'])
SD7[4]     = (1<<gpio['B']) + (1<<gpio['C']) + (1<<gpio['F']) + (1<<gpio['G'])
SD7[5]     = (1<<gpio['A']) + (1<<gpio['C']) + (1<<gpio['D']) + (1<<gpio['F']) + (1<<gpio['G'])
SD7[6]     = (1<<gpio['A']) + (1<<gpio['C']) + (1<<gpio['D']) + (1<<gpio['E']) + (1<<gpio['F']) + (1<<gpio['G'])
SD7[7]     = (1<<gpio['A']) + (1<<gpio['B']) + (1<<gpio['C'])
SD7[8]     = SD7['all']
SD7[9]     = (1<<gpio['A']) + (1<<gpio['B']) + (1<<gpio['C']) + (1<<gpio['F']) + (1<<gpio['G']) + (1<<gpio['D'])

text = 'SD7 = {\n'
for i,j in SD7.items():
    if isinstance(i, str):
        text += f"{' '*6}'{i}': {hex(j)}\n"
    else:
        text += f"{' '*6}{i}: {hex(j)}\n"
text += '}'

for i,j in gpio.items():
    

print(text)


