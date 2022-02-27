from time import sleep
from broker import rabbitmq_producer


class IngredientsTool:
    def __init__(self, ingredients, robot_communication):
        self.ingredients = ingredients
        self.robot_communication = robot_communication

    def simulate_work_sequence(self):
        for ingredient in self.ingredients:
            print("Adding {} ...".format(ingredient))
            sleep(5)

    @staticmethod
    def callback(ch, method, properties, body, **args):
        print(" [x] %r:%r" % (method.routing_key, body))
        thisTool = args["args"]
        thisTool.simulate_work_sequence()
        channel = rabbitmq_producer()
        for destination_route in thisTool.coworker_communication:
            message = b"Task successfully completed"

            channel.basic_publish(exchange="topic_logs", routing_key=destination_route, body=message)

    def __repr__(self):
        return "ingredients"


if __name__ == "__main__":
    IngredientTool = IngredientsTool(["tomatoes", "cheese"])
