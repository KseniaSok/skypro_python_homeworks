from Lesson7.Store.Pages.Shopmain import ShopMainPage
from Lesson7.Store.Pages.Shopcontainer import ShopContainer

def test(chrome):
    excepted_total = '58.29'

    shopmain = ShopMainPage(chrome)
    shopmain.registration()
    shopmain.buy()
    shopmain.click()
    shopmain.container()

    container = ShopContainer(chrome)
    container.checkout()
    container.info()
    container.price()

    assert excepted_total in container.price
    print(f'Сумма равна ${container.price()}')