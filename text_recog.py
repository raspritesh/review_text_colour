from PIL import Image
import pytesseract


def textrecog():
    im= Image.open("/home/pi/Downloads/download.jpg")

    text=pytesseract.image_to_string(im, lang='eng')
#print (text)
#print len(text)
#print text[0],text[2],text[5],text[8],text[10]
    a=[]
    a=text[0]
    a=a+text[2]
    a=a+text[5]
    a=a+text[8]
    a=a+text[10]
    return a
