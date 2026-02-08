from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "GalaxyA56", '+79999999999'),
    Smartphone("IPhone", "16e", '+79998888888'),
    Smartphone("Xiaomi", "Redmi", '+79997777777'),
    Smartphone("IPhone", "14", '+79996666666'),
    Smartphone("Samsung", "GalaxyM14", '+79995555555')
]

for smartphone in catalog:
    print(f"{smartphone.brend} - {smartphone.model}. {smartphone.number}.")
