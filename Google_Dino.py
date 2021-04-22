import numpy as np
import cv2
from mss import mss
import pyautogui as pag

main_point = {'top': 260, 'left': 770, 'width': 33, 'height': 25}

def process_image (original_image):
  processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
  processed_image = cv2.Canny(original_image, 200, 200)
  return processed_image

def screen_record():
  sct = mss()

  while(True):
    img = sct.grab(main_point)
    img = np.array(img)
    processed_image = process_image(img)
    mean = np.mean(processed_image)

    if not mean == float(0):
      pag.press('space')

    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break

screen_record()