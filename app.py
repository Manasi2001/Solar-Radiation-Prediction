import os
import joblib
model = joblib.load(r'SolarRadiationPrediction.pkl')

# importing Flask and other modules
from flask import Flask, request, render_template 
import numpy as np
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["GET", "POST"])
def rad_pred():
    if request.method == "POST":
       temp = request.form.get("temp")
       humidity = request.form.get("humidity")
       wspeed = request.form.get("wspeed")
       wdir = request.form.get("wdir")
       p = model.predict(np.array([temp, humidity, wspeed, wdir]).reshape(-4,4))
       output = 'Radiation in your area is: %.2f' % (p)+' W/m2'
       return render_template('main.html', output=output)
    return render_template('main.html')
  
if __name__=='__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)