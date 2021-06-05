import server
import cv2

def get_frame(device_name, frame):
    frame = cv2.Canny(frame,100,200)
    cv2.imshow(device_name, frame)
    cv2.waitKey(1)

try:
    srv = server.Server()
    srv.server_loop(callback_fn=get_frame)
except Exception as e:
    print(e)
finally:
    srv.close()