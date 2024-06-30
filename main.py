import os
import cv2
from pyzbar.pyzbar import decode

input_dir=r'pics'  #pictures path

for j in sorted(os.listdir(input_dir)):
    img = cv2.imread(os.path.join(input_dir, j) )

    qr_info = decode(img)

    print(qr_info)
