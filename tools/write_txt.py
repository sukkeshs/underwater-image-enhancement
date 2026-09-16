import os


def getfiles():
    path = 'D:/uwenh/UWEnhancement/DATA/Test/gt'
    filenames = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff'))]
    print(filenames)
    return filenames


if __name__ == '__main__':

    a = getfiles()
    with open("test_time.txt", "w") as f:
        for filename in a:
            print(filename)
            f.write(filename + '\n')