from PIL import Image
import os

def imgcrop(input, xPieces, yPieces):
    files = os.listdir(input)
    print(input)
    print(files)
    for file in files:
        filename, file_extension = os.path.splitext(file)
        im = Image.open(file)
        imgwidth, imgheight = im.size
        height = imgheight // yPieces
        width = imgwidth // xPieces
        for i in range(0, yPieces):
            for j in range(0, xPieces):
                box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
                a = im.crop(box)
                try:
                    
                    a.save('D:/aiModel/Image224/'+filename + "-" + str(i) + "-" + str(j) + file_extension)
                    print('save')
                except:
                    print('pass')
                    pass

print("start")
imgcrop(os.getcwd(),4,4)
