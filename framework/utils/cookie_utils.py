from framework.browser.browser import Browser


def get_cookies():
    return Browser().driver.get_cookies()


def add_cookie(cookie):
    Browser().driver.add_cookie({"name": cookie.name, "value": cookie.value})


def delete_cookie(cookie):
    Browser().driver.delete_cookie(cookie.name)


def is_cookie_exist(cookie):
    return Browser().driver.get_cookie(cookie.name) is not None
