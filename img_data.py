

def take_img():
    cwd = os.getcwd()
    img_path = '%s/data/External' %(cwd)
    print "take_image callback"
    call(['fswebcam','-r' ,'300x240', 'image.jpg', '--no-banner', img_path ])


def delete_img():
    pass