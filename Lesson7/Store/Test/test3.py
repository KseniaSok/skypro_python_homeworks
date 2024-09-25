from Lesson7.Store.Pages.Shopmain import ShopMainPage
from Lesson7.Store.Pages.Shopcontainer import ShopContainer
from Lesson7.pytest import chrome_browser

def test(chrome_browser):
    excepted_total = '58.29'

    shopmain = ShopMainPage(chrome_browser)
    shopmain.registration()
    shopmain.buy()
    shopmain.click()
    shopmain.container()

    container = ShopContainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()

    assert excepted_total in container.price()
    print(f'Сумма равна ${container.price()}')