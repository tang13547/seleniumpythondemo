import time

chromedriverPath = '../resources/driver/chromedriver.exe'
firefoxdriverPath = '../resources/driver/geckodriver.exe'
iedriverPath = '../resources/driver/IEDriverServer.exe'

base_url = "https://www.126.com/"

nowTime = time.strftime("%Y%m%d-%H%M%S")
screenshotName = "../../testOutput/screenshotsave/screenshot_" + nowTime + ".png"