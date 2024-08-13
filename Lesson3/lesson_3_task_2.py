from smartphone import Smartphone
catalog = []

phone1 = Smartphone ("Apple", "iPhone XR", "+79991234567")
phone2 = Smartphone ("LG", "G7", "+79991234568")
phone3 = Smartphone ("Samsung", "GALAXY Z", "+79991234569")
phone4 = Smartphone ("HTC", "Desire", "+79991234560")
phone5 = Smartphone ("Nokia", "3310", "+79991234500")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")