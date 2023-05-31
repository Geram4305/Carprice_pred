# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify
from Model_files.ml_model import predict_price
import pickle

app = Flask('Carprice_prediction')
#model = pickle.load(open('carprice_rf.pkl', 'rb'))

@app.route('/', methods=['POST'])
def predict():
        vehicle_details = request.get_json()
        print(vehicle_details)
        with open('./Model_files/carprice_rf.pkl', 'rb') as f:
            model_rf = pickle.load(f)
            f.close()
        predictions = predict_price(vehicle_details,model_rf)
        response = {
            'carprice_predictions': list(predictions)
        }
        return jsonify(response)

        #output = round(prediction[0], 2)


        #return render_template('index.html', prediction_text='CO2 Emission of the vehicle is :{}'.format(output))



#@app.route('/', methods=['GET'])
def ping():
    return "Pinging Model Application!!"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

