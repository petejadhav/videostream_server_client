import cv2
import imagezmq

class Server():
    def __init__(self):
        self.image_hub = imagezmq.ImageHub()
        self.devices = []

    def server_loop(self, callback_fn):
        print("Starting Server loop ...")
        while True:  # show streamed images until Ctrl-C
            (device_name, image) = self.image_hub.recv_image()
            if device_name not in self.devices:
                print("New Device",device_name)
                self.devices.append(device_name)
            callback_fn(device_name,image)
            #cv2.imshow(device_name, image) # 1 window for each RPi
            #cv2.waitKey(1)
            self.image_hub.send_reply(b'OK')
    
    def close(self):
        pass
