# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Link, PermanentLink

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

# Create your views here.

def home(request):
    links = Link.objects.all()

    delay = 50
    options = webdriver.ChromeOptions()
    #options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('/Users/lblagovic/Sites/streamproject/streamproject/streamproject/stream/chromedriver', chrome_options=options)
    for link in links:
    # ODLICNO IZVLACI LINKOVE STREAMA
        browser.get(link.link)
        element_present = EC.presence_of_element_located((By.ID, 'area-middle'))
        WebDriverWait(browser, delay).until(element_present)
        elem = browser.find_element_by_id('area-middle')
        iframe = elem.find_element_by_tag_name('iframe')
        src = iframe.get_attribute('src')
        obj = Link.objects.get(pk=link.id)
        obj.realLink = src
        obj.save()

    browser.quit()

    return redirect(stream)


def stream(request):
    links = Link.objects.all()
    plinks = PermanentLink.objects.all()

    return render(request, 'stream.html', {'links':links, 'plinks':plinks})