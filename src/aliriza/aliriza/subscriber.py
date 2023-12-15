import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MekatekSubscriber(Node):

    def __init__(self):
        super().__init__('mekatek_subscriber') # Düğüm oluşturulur
        self.subscription_ = self.create_subscription(String, 'mekatek_topic', self.callback, 10) # Subscriber oluşturur. String tipindeki mesajlar, mekatek_topic'i üzerinden, gelen veri(mesaj) metoda iletilir, kuyruk boyutu.

    def callback(self, msg):
        self.get_logger().info('Alandı: %s' % msg.data) # Yayının gerçekleştiğini belirten log

def main(args=None):
    rclpy.init(args=args)
    subscriber = MekatekSubscriber()
    try:
        rclpy.spin(subscriber)
    except KeyboardInterrupt:
        pass

    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

