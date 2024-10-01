import requests
from EmployeesApi import workersApi

api = workersApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
    #Создать новую компанию
    name = "Shop"
    descr = "Shop market"
    result = api.create_company(name, descr)
    new_id = result["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # получить список сотрудников 
    body = api.get_employees_list(companyId)
    len_before = len(body)
    # добавить нового сотрудника
    firstName = "Oks"
    lastName = "Sok"
    middleName = "Val"
    company = companyId
    email = "oksok@gmail.com"
    url = "string"
    phone = "89999999999"
    birthdate = "1999-01-01"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Oks"
    assert body[-1]["lastName"] == "Sok"
    assert body[-1]["middleName"] == "Val"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89999999999"
    assert body[-1]["birthdate"] == "1999-01-01"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "Магазин"
    descr = "Маркет"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    begin_list = len(body)
    # добавить нового сотрудника
    firstName = "Саша"
    lastName = "Иванов"
    middleName = "Андреевич"
    company = companyId
    email = "sasha123@mail.ru"
    url = "string"
    phone = "89876543212"
    birthdate = "1999-02-02"
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate,isActive=1)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Саша"
    assert body[-1]["lastName"] ==  "Иванов"
    assert body[-1]["middleName"] == "Андреевич"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "89876543212"
    assert body[-1]["birthdate"] == "1999-02-02"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "New market"
    descr = "Fruits"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Виктор"
    lastName = "Петров"
    middleName = "Александрович"
    company = companyId
    email = "victor@mail.ru"
    url = "string"
    phone = "85762964927"
    birthdate = "1989-10-10"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании 
    body = api.get_employees_list(companyId)
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Сидоров"
    new_email = "sidorov@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "sidorov@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False

def test_delete_employee():
    #Создать новую компанию
    name = "Мясо"
    descr = "Свежее"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "Глеб"
    lastName = "Фролов"
    middleName = "Сергеевич"
    company = companyId
    email = "gleb23@mail.ru"
    url = "string"
    phone = "89999999999"
    birthdate = "1999-05-05"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # удалить сотрудника
    del_emp = api.delete_employee(emp_id)

    # Проверить, что сотрудник был удален
    assert del_emp is not None, "Сотрудник не был удален"