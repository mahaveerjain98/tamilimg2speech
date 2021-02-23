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
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from textblob import TextBlob
from deep_translator import GoogleTranslator,MyMemoryTranslator
import gtts
import os
from playsound import playsound
from gtts import gTTS
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



if __name__ =="__main__":
  
    image_file = "tamilimages/OIP1.jpg"


    # img = mpimg.imread(image_file)
    # plt.imshow(img)
    # plt.show()

    text = pytesseract.image_to_string(Image.open(image_file), lang="tam")
    #  text1 = pytesseract.image_to_string(Image.open(image_file), lang="tam+en")
    text=text.replace("\n"," ").replace("\u200c","").replace("\x0c","")
    

    tb = TextBlob(text)
    textblob_translated = str(tb.translate(to="en"))
    print(textblob_translated)
    
    google_translated = GoogleTranslator(source='auto', target='en').translate(text)
    print(google_translated)

    
    try:
        memory_translated = MyMemoryTranslator(source="tamil", target="en").translate(text=text)
    except:
        memory_translated=""
    print(memory_translated)

    if textblob_translated == google_translated:
        result=textblob_translated
    elif google_translated == memory_translated:
        result=google_translated
    elif memory_translated == textblob_translated:
        result=memory_translated
    else:
        result=google_translated


    obj = gTTS(text=textblob_translated, lang='en', slow=False)
    filename="result.mp3"
    obj.save(filename)
    playsound(filename)
    os.remove(filename)



  # # getting similarity metrics of 2 strings
# def JaccardDistance(str1, str2):
#     str1 = set(str1.split())
#     str2 = set(str2.split())
#     return float(len(str1 & str2)) / len(str1 | str2)

# from collections import Counter
# from sklearn.feature_extraction.text import TfidfVectorizer

# import math
# #Function for finding cosin similarity
# def cosine_similarity(v1,v2):
#     "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
#     sumxx, sumxy, sumyy = 0, 0, 0
#     for i in range(len(v1)):
#         x = v1[i]; y = v2[i]
#         sumxx += x*x
#         sumyy += y*y
#         sumxy += x*y
#     return sumxy/math.sqrt(sumxx*sumyy)

# #document corpus
# new_docs = ['He watches basketball and baseball', 'Julie likes to play basketball and baseball', 'Jane loves to play baseball']
# vectorizer = TfidfVectorizer(stop_words='english',
#                              use_idf=True, lowercase=True)

# first get TFIDF matrix
# X = vectorizer.fit_transform(new_docs)
# cosine_similarity(X[0],X[1])

# import gtts  
# from playsound import playsound  
# from gtts import gTTS 
# obj = gTTS(text=result, lang='en', slow=False) 
# obj.save("example.mp3")   
# # playsound(obj)  

# import IPython
# IPython.display.Audio("example.mp3", autoplay=True)



