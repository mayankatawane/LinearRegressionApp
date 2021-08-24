from flask import Flask, render_template,request
from flask_cors import cross_origin

import pickle
application =Flask(__name__)

@application.route('/',methods = ['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')


@application.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CRIM=float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            LSTAT = float(request.form['LSTAT'])

            # NEW STUFFS
            filename = 'finalized_model_new.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[CRIM,ZN,INDUS,NOX,RM,TAX,PTRATIO,LSTAT]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction = round(prediction[0],2))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	application.run(debug=True) # running the app