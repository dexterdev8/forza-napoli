from broker import rabbitmq_producer


class DeliveryTool:
    def __init__(self, coworker_communication):
        self.coworker_communication = coworker_communication

    def simulate_work_sequence(self):
        # Perform some accion
        print("Picking the pizza from the oven and placing it in the box")

    @staticmethod
    def callback(ch, method, properties, body, **args):
        print(" [x] %r:%r" % (method.routing_key, body))
        thisTool = args["args"]
        thisTool.simulate_work_sequence()
        channel = rabbitmq_producer()
        for destination_route in thisTool.cowoker_communication:
            message = b"Task successfully completed"

            channel.basic_publish(exchange="topic_logs", routing_key=destination_route, body=message)

    def __repr__(self):
        return "delivery"
