class DeliveryTool:
    def __init__(self):
        pass

    @staticmethod
    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))

    def simulate_work_sequence(self):
        # Perform some accion
        pass

    def __repr__(self):
        return "delivery"
