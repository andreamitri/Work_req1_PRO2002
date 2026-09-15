class OnlineOrder:
    pass


class StoreOrder:
    pass


class PhoneOrder:
    pass


class OrderFactory:
    order_types = {
        "online": OnlineOrder,
        "store": StoreOrder,
        "phone": PhoneOrder,
    }

    @classmethod
    def create_order(cls, order_type):
        order_class = cls.order_types.get(order_type)

        if order_class is None:
            raise ValueError(f"Unknown order type: {order_type}")

        return order_class()