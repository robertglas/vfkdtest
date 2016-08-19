from selenium import webdriver
from xvfbwrapper import Xvfb


def before_all(context):
    print("")
    context.vdisplay = Xvfb()
    context.vdisplay.start()
    print("> Starting the browser")
    browser = context.config.userdata.get("browser")
    context.driver = webdriver.Firefox()

def after_all(context):
    print("< Closing the browser")
    print("")
    context.driver.close()
    context.driver.quit()
    context.vdisplay.stop()


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass
