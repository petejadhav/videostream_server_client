import cv2
import imagezmq

class Server():
    def __init__(self):
        self.image_hub = imagezmq.ImageHub()

    def server_loop(self, callback=self.get_frame):
        while True:  # show streamed images until Ctrl-C
            device_name, image = self.image_hub.recv_image()
            #cv2.imshow(device_name, image) # 1 window for each RPi
            cv2.waitKey(1)
            self.image_hub.send_reply(b'OK')

    def get_frame(self, device_name, frame):
        while True:
            cv2.imshow(device_name, image)
            yield