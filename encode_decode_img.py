# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:06:39 2019

@author: VC5052254
"""

from flask import Flask, render_template, request,jsonify
import base64
#import cv2
#import numpy as np
#import io
import webbrowser
import os

app = Flask(__name__)

@app.route('/show', methods=['POST'])
def show():
    data = request.json     
    jpg_img = data['base64String']
    #print(jpg_img)
    
    #b64_histogram = "data:image/png;base64," + jpg_img
    #cv2.imwrite('',b64_histogram)
    
    #img_split = str(jpg_img)
   # x = img_split.split(",")[1]
    
    #base64imgfile_to_array(jpg_img)
    
    #s=x.decode()
    #print(s)
    
    return jsonify({'imgSrc':jpg_img})
    #return render_template("img_output.html", result= image_64_decode)

'''
def base64imgfile_to_array(b64enc_filestring, params={}):
     file_string = base64.b64decode(b64enc_filestring)
     file_buffer = io.BytesIO()       
     file_buffer.write(file_string)
     file_buffer.seek(0)
    
     file_bytes = np.asarray(bytearray(file_buffer.read()), dtype=np.uint8)
     img_array = cv2.imdecode(file_bytes, 0)
     return img_array
'''
    
   
''' 
    plt = request.form['file']
    print(plt)
    # Saving fig to disk in png format
    plt.savefig('my_plt.jpg')

    # Rendering fig in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='jpg')
    figfile.seek(0)
    figdata_jpg = base64.b64encode(figfile.getvalue()).decode('ascii')
    prnt(figdata_jpg)
    
    
    -------------------------------------------------
    result = request.json
    image_64_decode = base64.b64decode(result)
    image_result = open('img_decode.jpg', 'wb') # create a writable image and write the decoding result image_result.write(image_64_decode)
    image_result.write(image_64_decode)
 '''
    
if __name__ == '__main__':
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('file://' + os.path.realpath('templates/drui.html'))

    #url = os.getcwd() +'\\templates\\drui.html'
    #webbrowser.get(chrome_path).open(url)
    app.run(port=5000)