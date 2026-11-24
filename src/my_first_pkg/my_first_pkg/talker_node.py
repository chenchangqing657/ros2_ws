import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.declare_parameter('rate', 1.0)
        rate = self.get_parameter('rate').value
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.n = 0
        self.create_timer(1.0 / rate, self.tick)

    def tick(self):
        self.n += 1
        self.pub.publish(String(data=f'msg {self.n}'))


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        try:
            rclpy.shutdown()   
        except Exception:
            pass   