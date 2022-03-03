from socket import timeout
import time
import requests
from urllib import request
from playwright.sync_api import sync_playwright
import os
temps = 1
def clear (): os.system('cls')
finir = "pasfini"
argent = 0.0
while finir != "fini":
    dorcpcurl = "https://goodpay.fr/actions/cb70a510d7c83a14b374c56b7ed2ed83/4e5ac367411fffb0ee2c9b662cdb637d/76decda975f8d40edff864c8838f9c9b"
    Aescpclien = "https://goodpay.fr/actions/0a19bcfcc6385bfbdda771533cd7f694/52e05f93f02f612c66552ca9329fad0e/76decda975f8d40edff864c8838f9c9b"
    orangecpclien = "https://goodpay.fr/actions/0601b74059931609ce1fd8410db6fb14/ebab18d8ead58cc147f05bb58097abfe/76decda975f8d40edff864c8838f9c9b"
    ebooklien = "https://goodpay.fr/actions/56517f19aa289885c43e8db9137fb1b0/d13c3522ade1c7d4a7244fb60e4189ce/76decda975f8d40edff864c8838f9c9b"
    feedcpclien = "https://goodpay.fr/actions/34dbc91ba0166587bc807a9b531b9b4d/b9af0067f306699bc62f6121732ab9f0/76decda975f8d40edff864c8838f9c9b"
    roompoturl = "https://goodpay.fr/actions/b7f520a55897b35e6eb462bbf80915c6/58860e03a9e709c61d386d6b9a65a278/76decda975f8d40edff864c8838f9c9b"
    faguocpcurl = "https://goodpay.fr/actions/e0f9e8ce4809cc21c3d636686bcdd99d/39e40b9977c292c8a2f7926a60cc8834/76decda975f8d40edff864c8838f9c9b"
    sebogourl = "https://goodpay.fr/actions/55a0ce8200cf39c3028ebc66f356bf7e/da49101fce78629f613aef7dd3c52c2d/76decda975f8d40edff864c8838f9c9b"
    dorcelurl = "https://goodpay.fr/actions/0e9d48fe4fca69a47f5353d0a62333c2/bf16ee11629d0b6f2cbfa183b4b06bef/76decda975f8d40edff864c8838f9c9b"
    jeucpcurl = "https://goodpay.fr/actions/efd766aa5e7a2a276d3f990cf7da8f4a/7033ec1d8f1e712442052fbf167d958e/76decda975f8d40edff864c8838f9c9b"
    picacpcurl = "https://goodpay.fr/actions/469167a0e7cc99d4406eacc7e898b258/bd9487e7dd632b87bfc0792d4af248ec/76decda975f8d40edff864c8838f9c9b"
    petitcpcurl = "https://goodpay.fr/actions/9c8780d93f7077ed38cdc242778f7fdc/e1d0bdf0d3d6fb89483648ce7ab98d17/76decda975f8d40edff864c8838f9c9b"
    valpcpcurl = "https://goodpay.fr/actions/1d9b1a8b18c79139022fa537f4a12fd7/fa0781c4de3e78f3b5a56e68580698e5/76decda975f8d40edff864c8838f9c9b"
    cpccampagnesurl = "https://goodpay.fr/actions/e1940719f77abe2ef9a5249421ac8492/ca483a0cac6f28b2e2a237856bb07546/76decda975f8d40edff864c8838f9c9b"
    costacpvurl = "https://goodpay.fr/actions/40a15ab98098e23765f5fe601366d8a9/a9da3b3a94770b8ee9dfcf9f4461b381/76decda975f8d40edff864c8838f9c9b"
    villecpcurl = "https://goodpay.fr/actions/1d76ffc82aa2886416809b12d5e65f5b/66aed5bbbf836a9e23b966c1a52ccff8/76decda975f8d40edff864c8838f9c9b"
    temps = 10
    proxy = {
        "http": "http://ZShFK:P7DNM@192.168.1.10:1001",
        "https": "http://ZShFK:P7DNM@192.168.1.10:1001",
    }
    try:
        s = requests.Session()
        s.proxies = proxy
        t = s.get("https://icanhazip.com/")
        print(t.text)
    except Exception as error:
        time.sleep(2)
        requests.get("http://192.168.1.10:10001/rotate")
        print("faut attendre")
        time.sleep(60)
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=True,timeout=9000,proxy={
            "server": "http://192.168.1.10:1001",
            "username": "ZShFK",
            "password": "P7DNM"
        })
        context = browser.new_context(viewport={'width':800, 'height': 600})
        feedcpc = context.new_page()
        feedcpc.goto(feedcpclien)
        if feedcpc.url == feedcpclien:
            feedcpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        orangecpc = context.new_page()
        orangecpc.goto(orangecpclien)
        if orangecpc.url == orangecpclien:
            orangecpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        dorcel = context.new_page()
        dorcel.goto(dorcelurl)
        if dorcel.url == dorcelurl:
            dorcel.close()
        else:
            temps = 60
            argent = argent + 0.02 
        roompot = context.new_page()
        roompot.goto(roompoturl)
        if roompot.url == roompoturl:
            roompot.close()
        else:
            temps = 60
            argent = argent + 0.04
        faguocpc = context.new_page()
        faguocpc.goto(faguocpcurl)
        if faguocpc.url == faguocpcurl:
            faguocpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        sebogo = context.new_page()
        sebogo.goto(sebogourl)
        if sebogo.url == sebogourl:
            sebogo.url
        else:
            temps = 60
            argent = argent + 0.03
        jeucpc = context.new_page()
        jeucpc.goto(jeucpcurl)
        if jeucpc.url == jeucpcurl:
            jeucpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        aescpc = context.new_page()
        aescpc.goto(Aescpclien)
        if aescpc.url == Aescpclien:
            aescpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        picacpc = context.new_page()
        picacpc.goto(picacpcurl)
        if picacpc.url == picacpcurl:
            picacpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        petitcpc = context.new_page()
        petitcpc.goto(petitcpcurl)
        if petitcpc.url == petitcpcurl:
            petitcpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        dorcpc = context.new_page()
        dorcpc.goto(dorcpcurl)
        if dorcpc.url == dorcpcurl:
            dorcpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        valpcpc = context.new_page()
        valpcpc.goto(valpcpcurl)
        if valpcpc.url == valpcpcurl:
            valpcpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        cpccampagne = context.new_page()
        cpccampagne.goto(cpccampagnesurl)
        if cpccampagne.url == cpccampagnesurl:
            cpccampagne.close()
        else:
            temps = 60
            argent = argent + 0.02
        costacpc = context.new_page()
        costacpc.goto(costacpvurl)
        if costacpc.url == costacpvurl:
            costacpc.close()
        else:
            temps = 60
            argent = argent + 0.05
        villecpc = context.new_page()
        villecpc.goto(villecpcurl)
        if villecpc.url == villecpcurl:
            villecpc.close()
        else:
            temps = 60
            argent = argent + 0.02
        time.sleep(temps)
        browser.close()
        #print(os.system('"C:/Program Files (x86)/Minimal ADB and Fastboot/adb.exe" shell svc data disable'))
        #time.sleep(1)
        #print(os.system('"C:/Program Files (x86)/Minimal ADB and Fastboot/adb.exe" shell svc data enable'))
        #time.sleep(5)
        clear()
        print("Vous avez fait " + str(argent)+"€")
        #requests.get("http://192.168.1.10:10001/rotate")
        os.system('uhubctl -l 1-1 -p 2 -a 2')
        time.sleep(60)