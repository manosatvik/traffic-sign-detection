from flask import Flask, render_template, request
from werkzeug import secure_filename
from keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

testing_file = ''
model = load_model('circle_model.h5')
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

@app.route('/')

def helloIndex():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])

def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      testing_file = f.filename
      model = get_model(f.filename)
      print(model)
      return '<h1>file uploaded successfully</h1>'
def get_model(fname):
    print(fname)
    cr = {0:0,1:1,2:10,3:16,4:2,5:3,6:4,7:5,8:7,9:8,10:9}
    img = cv2.imread('C:/Users/manosatvik/Desktop/collg min project/dataset/Test/'+str(fname))
    print(img.shape)
    img = cv2.resize(img,(80,80))
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img = np.reshape(img,[1,80,80,3])
    classes = model.predict_classes(img)
    print(classes)
    #return (cr[classes[0]])
app.run('localhost', port= 81)