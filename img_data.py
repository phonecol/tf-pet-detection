import os
from subprocess import call

def take_img():
    cwd = os.getcwd()
    img_path = '%s/data/External/image.jpg' %(cwd)
    print ("take_image callback")
    call(['fswebcam','-r' ,'300x240', '--no-banner', img_path ])


def delete_img():
    pass