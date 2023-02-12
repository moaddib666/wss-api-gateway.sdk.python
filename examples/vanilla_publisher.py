import socket

from margay.sdk.publisher import Publisher

if __name__ == "__main__":

    publisher = Publisher()
    publisher.publish_raw("hello there", socket.gethostname(), recipient="Snow")
