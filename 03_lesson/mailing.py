from addres import Address


class Mailing:

    def __init__(self, track, from_address, to_address, cost):
        self.track = track
        self.from_address = from_address
        self.to_address = to_address
        self.cost = cost

    def __str__(self):
        return (f"Отправление "
                f"Трек-номер: {self.track} "
                f"Из {self.from_address}\n"
                f"В {self.to_address}.\n"
                f"Стоимость: {self.cost} рублей.\n")
