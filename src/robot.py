from broker import rabbitmq_consumer
from tools import *


class Robot:
    def __init__(self, role, tool):
        self.role = role
        self.tool = tool
        self._set_binding_key()
        self._robot_connect()
        self._robot_consume()

    def _robot_connect(self):
        self.channel, self.queue_name = rabbitmq_consumer(self.binding_key)

    def _robot_consume(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.tool.callback, auto_ack=False)
        self.channel.start_consuming()

    def _set_binding_key(self):
        self.binding_key = "{}.{}.robot".format(self.tool, self.role)
        print(self.binding_key)


if __name__ == "__main__":
    Rct = Robot("chef", ingredients.IngredientsTool())
    # Rcp = Robot("Chef", pick.PickTool())

    # Rpp = Robot("Prod", delivery.DeliveryTool())
    # Rpt = Robot("Prod", slicer.SliceTool())
