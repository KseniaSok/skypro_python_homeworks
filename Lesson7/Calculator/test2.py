from Lesson7.Calculator.calculator import Calculator
from Lesson7.pytest import chrome_browser

def test_calculator(chrome_browser):
    calculator = Calculator(chrome_browser)
    calculator.insert_time()
    calculator.click()

    assert '15' in calculator.wait_button()