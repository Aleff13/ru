from dotenv import dotenv_values
import re
from playwright.sync_api import Page, expect
import pywhatkit as whats
from win32 import win32clipboard

config = dotenv_values(".env")

number = config['number']
ruUrl = config['ruUrl']

week = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

locations = [
    '//*[@id="post-65"]/div[2]/table/tbody/tr[2]',
    '//*[@id="post-65"]/div[2]/table/tbody/tr[3]',
    '//*[@id="post-65"]/div[2]/table/tbody/tr[4]',
    '//*[@id="post-65"]/div[2]/table/tbody/tr[5]',
    '//*[@id="post-65"]/div[2]/table/tbody/tr[6]',
    '//*[@id="post-65"]/div[2]/table/tbody/tr[7]',
    '//*[@id="post-65"]/div[2]/table/tbody/tr[8]'    
]

def test_menu(page: Page):
    i = 0;

    page.goto("https://ru.ufsc.br/ru/")

    for day in locations:
        page.locator(f'xpath={day}').screenshot(path=f"{i}.png")
        i = i + 1

    for x in range (0, i):
        whats.sendwhats_image(number, f'{x}.png', f"{week[x]}", 15, True)


