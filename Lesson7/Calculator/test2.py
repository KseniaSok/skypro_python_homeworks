from Lesson7.Calculator.calculator import Calculator

def test_calculator(chrome):
    calculator = Calculator(chrome)
    calculator.insert_time()
    calculator.click()

    assert '15' in calculator.wait_button()