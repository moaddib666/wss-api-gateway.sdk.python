
from margay.sdk.client import Client


if __name__ == '__main__':
    token = input("Auth token:")
    client = Client("ws://127.0.0.1:8080", token)
    client.run()
