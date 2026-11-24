import rclpy
from rclpy.node import Node


class HelloNode(Node):
    def __init__(self):
        super().__init__('hello_node')
        self.n = 0
        self.create_timer(1.0, self.tick)     # 每 1 秒调用一次 tick

    def tick(self):
        self.n += 1
        self.get_logger().info(f'hello {self.n}')


def main(args=None):
    rclpy.init(args=args)          # 初始化 ROS2
    node = HelloNode()             # 创建节点
    try:
        rclpy.spin(node)           # 让程序一直活着，等回调
    except KeyboardInterrupt:
        pass                       # Ctrl+C 时不算错误
    finally:
        node.destroy_node()        # 收尾：销毁节点
        rclpy.shutdown()           # 关掉 ROS2


if __name__ == '__main__':
    main()