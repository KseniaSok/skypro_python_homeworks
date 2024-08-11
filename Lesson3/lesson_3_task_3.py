from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Улица1", "дом 5", "кв 5")
from_address = Address("789012", "Тула", "Улица2", "дом 10", "кв 10")
mailing = Mailing(to_address, from_address, 573, "track1234567890")
print(mailing)