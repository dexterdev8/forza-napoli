from time import sleep
from broker import rabbitmq_producer


class Camera:
    def __init__(self, name, type_signal):
        self.name = name
        self.channel = rabbitmq_producer()
        self.routing_key = "ingredients.chef.robot"  # TODO: Parametrize this

        while True:
            self.simulate_trigger_signal()
            sleep(5)

    def simulate_trigger_signal(self):
        # TODO: Come up with a nice way to simulate this
        message = b"Trigger fridge flag"
        self.channel.basic_publish(exchange="topic_logs", routing_key=self.routing_key, body=message)
        print(" [x] Sent %r:%r" % (self.routing_key, message))


if __name__ == "__main__":
    # TODO: Not super convinced about this type signal. Need to re-think it
    C1 = Camera(name="fridge", type_signal=bool)
