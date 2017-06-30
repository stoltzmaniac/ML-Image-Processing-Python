import io
from google.cloud import vision

vision_client = vision.Client()
#file from wget -O img.png https://www.dropbox.com/s/mgxvbii4rzcb6vp/originalWebcamShot.png?dl=0
file_name = './img.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content, )

labels = image.detect_labels()
properties = image.detect_properties()
crop_hints = image.detect_crop_hints()
faces = image.detect_faces()
full_text = image.detect_full_text()
landmarks = image.detect_landmarks()
logos = image.detect_logos()
safe_search = image.detect_safe_search()
text = image.detect_text()
detect_web = image.detect_web()


#export GOOGLE_APPLICATION_CREDENTIALS='/Users/stoltzmanconsulting/Documents/Git Repositories/GitHub/ML-Image-Processing-Python/client_secret.json'
