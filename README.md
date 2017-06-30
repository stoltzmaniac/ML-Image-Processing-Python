# ML-Image-Processing-Python
Utilizing opencv and image processing with machine learning.

## Notes:

This project currently runs on Google Compute Engine
You must have: Python 3, pip3

cd ~
mkdir googleCloudProjects
nano ~/.profile
export GOOGLE_APPLICATION_CREDENTIALS=~/googleCloudProjects/client_secret.json **private file downloaded from google cloud console**
source ~/.bashrc
sudo apt-get install  python3-pip
sudo pip install google-cloud

mkdir VisionClient
cd VisionClient

Then you can run your py scripts!
For example: python3 -i sandbox.py

Report.py works as python3 -i report.py "./images/img.png" in which you can replace with http: