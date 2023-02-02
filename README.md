# Yolov7_OCR
This is my final project.
Using yolov7 to detect car,motorbike and licence plate and utilizing easyocr to read text.

Package                Version
---------------------- --------------------
certifi            2022.12.7
charset-normalizer 3.0.1
colorama           0.4.6
contourpy          1.0.7
cycler             0.11.0
easyocr            1.6.2
fonttools          4.38.0
idna               3.4
imageio            2.25.0
kiwisolver         1.4.4
matplotlib         3.6.3
networkx           3.0
ninja              1.11.1
numpy              1.24.1
opencv-python      4.7.0.68
packaging          23.0
pandas             1.5.3
Pillow             9.4.0
pip                23.0
pyclipper          1.3.0.post4
pyparsing          3.0.9
python-bidi        0.4.2
python-dateutil    2.8.2
pytz               2022.7.1
PyWavelets         1.4.1
PyYAML             6.0
requests           2.28.2
scikit-image       0.19.3
scipy              1.10.0
seaborn            0.12.2
shapely            2.0.1
six                1.16.0
thop               0.1.1.post2209072238
tifffile           2023.1.23.1
torch              1.13.1
torchvision        0.14.1
tqdm               4.64.1
typing_extensions  4.4.0
urllib3            1.26.14

model URL: https://drive.google.com/file/d/1S3qSOv5QrIVMFwnhFPr8AFz5B1nv8Q5M/view?usp=share_link

download model and move it into: runs/train/exp/weights/

run with webcame: cd to project and run `python .\detect.py --source 0`