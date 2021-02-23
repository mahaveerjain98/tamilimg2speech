# !wget -O "image4.jpg" "https://www.bing.com/images/search?view=detailV2&ccid=AfoYJ0uj&id=97B416D8A32272C2C97C1724B6D35844E9723F3E&thid=OIP.AfoYJ0ujJcfHIcqajqmvvwHaFz&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR01fa18274ba325c7c721ca9a8ea9afbf%3frik%3dPj9y6URY07YkFw%26riu%3dhttp%253a%252f%252fwww.tamilscraps.com%252fwp-content%252fuploads%252f2016%252f10%252fscrap_229.jpg%26ehk%3dwzcwEGRaUAyj4T7UwFWTey7%252fNb%252bPwxVcVq%252f2yTYuieU%253d%26risl%3d%26pid%3dImgRaw&exph=580&expw=740&q=Friends+Quotes+Tamil&simid=608029552847227081&ck=8F7AA60E356614036E858C9040EFBD64&selectedIndex=75&FORM=IRPRST"
# #online image can be downloaded


# !pip install pytesseract
# !sudo apt update
# !sudo apt install tesseract-ocr
# !sudo apt install libtesseract-dev
# #give type of language to work on the last 
# !sudo apt-get install tesseract-ocr-tam
# !pip install textblob
# !pip install deep-translator
# !pip install gTTS  
# !pip install playsound  



import pytesseract
from PIL import Image
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
from textblob import TextBlob
from deep_translator import GoogleTranslator,MyMemoryTranslator
import gtts
import os
from playsound import playsound
from gtts import gTTS
import argparse
import time
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#Give this path where the tesseract is installed and add the tamil model in the tessdata folder from the tesseract tamilocr website


if __name__ =="__main__":

    st=time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input",help="Enter the Input image where tamil text to be translated ")
    args= parser.parse_args()
    if args.input != None :
        if args.input.endswith("jpg") or args.input.endswith("png"):
            print(f"File is taken as {args.input}")
            image_file = args.input
        else:
            print("incorrect file, Give jpg or png file")
    else:
        print("using Default file tamilimages/OIP1.jpg")
        image_file = "tamilimages/OIP1.jpg"
    
    tst=time.time()    
    text = pytesseract.image_to_string(Image.open(image_file), lang="tam")
    print("time taken for pytesseract:",time.time()-tst)
    text=text.replace("\n"," ").replace("\u200c","").replace("\x0c","")
    bts=time.time()
    tb = TextBlob(text)
    textblob_translated = str(tb.translate(to="en"))
    print("Time taken for blob translate:",time.time()-bts)
    gts=time.time()  
    google_translated = GoogleTranslator(source='auto', target='en').translate(text)
    print("Time taken for google translate:",time.time()-gts)
    result=textblob_translated
    print(result)

    sts=time.time()
    obj = gTTS(text=textblob_translated, lang='en', slow=False)
    filename="result.mp3"
    obj.save(filename)
    print("time to save an sound object:",time.time()-sts)
    playsound(filename)
    os.remove(filename)
    print("Timetaken:",time.time()-st)

