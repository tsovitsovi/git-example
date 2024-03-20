from mailing import Mailing
from address import Address

to_address = Address ("605065", "Нижний Новгород", "Дьяконова", "4", "8")
from_address = Address ("855565", "Тбилиси", "Пушкинская", "3", "125")

mailing = Mailing (to_address, from_address, "10000", "666777733")


print(f"Отправление {mailing.track} из {to_address.index}, {to_address.town}, {to_address.street}, {to_address.home} - {to_address.flat} в {from_address.index}, {from_address.town}, {from_address.street}, {from_address.home} - {from_address.flat}. Стоимость {mailing.cost} рублей.")