import cv2
import imagezmq
import socket
import time
from videostream import WebcamVideoStream

class Client():
    def __init__(self, server_address, server_port):
        self.server = imagezmq.ImageSender(connect_to='tcp://{}:{}'.format(server_address, server_port))
        self.device_name = socket.gethostname()
        self.cam = WebcamVideoStream().start()
        time.sleep(2.0)
        print("Client started.")

    def client_loop(self):
        while True:  # send images as stream until Ctrl-C
            image = self.cam.read()
            self.server.send_image(self.device_name, image)