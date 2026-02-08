from addres import Address
from mailing import Mailing

if __name__ == "__main__":

    frm = Address(index="115115",
                  city="Москва",
                  street="Ленина",
                  house="2",
                  apartment="122")

    to = Address(index="123456",
                 city="Великий Устюг",
                 street="Мира",
                 house="1",
                 apartment="1")

    mail = Mailing(track="ПР123456789RU",
                   from_address=frm,
                   to_address=to,
                   cost=100)

    print(mail)
