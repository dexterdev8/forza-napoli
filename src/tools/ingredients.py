class IngredientsTool:
    def __init__(self):
        pass

    def simulate_work_sequence(self):
        # Perform some accion
        pass

    @staticmethod
    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))

    def __repr__(self):
        return "ingredients"
