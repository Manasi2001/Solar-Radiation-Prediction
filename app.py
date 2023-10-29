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
       try:
         p = model.predict(np.array([temp, humidity, wspeed, wdir]).reshape(-4,4))
         if p>0 and p<= 200:
           type = 'low'
         elif p>200 and p<600:
           type = 'moderate'
         elif p>= 600:
           type = 'high'
         output = 'Radiation in your area is: %.2f' % (p)+' W/m2. Solar radiation levels are ' + type + '.'
       except:
         output = 'Recheck your inputs.'
       return render_template('main.html', output=output)
    return render_template('main.html')
  
if __name__=='__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)
