'''ДЕПЛОИМ МОДЕЛЬ НА ВЕБ-СЕРВИС'''

from flask import Flask, request, jsonify
import pickle
import numpy as np

# url = http://localhost:8000/predict?obj_id=55
# response = {"obj_id": "55", "prediction": 141731, "response_status": "OK"}

app = Flask(__name__)

MODEL_FILE = 'best_model.pkl'
FEATURE_ORDER_FILE = 'feature_order.pkl'
TEST_DATA_FILE = 'test_data.pkl'

# Производим десериализацию трех сериализованных объектов
with open(MODEL_FILE, 'rb') as pkl_file:
    model = pickle.load(pkl_file)

with open(FEATURE_ORDER_FILE, 'rb') as pkl_file:
    feature_order = pickle.load(pkl_file)

with open(TEST_DATA_FILE, 'rb') as pkl_file:
    X_test_depl = pickle.load(pkl_file)


# код Flask метода для предикта обученной моделью
@app.route('/predict', methods=['GET'])
def predict():
    obj_id = request.args.get('obj_id')
    try:
        obj_id = int(obj_id)
        test_features = X_test_depl[X_test_depl['obj_id'] == obj_id][feature_order].values
        # print(test_features)
        # print(test_features.shape)
        res = round((np.exp(model.predict(test_features)[0]) - 1))
        print(res)
        return jsonify({'prediction': res, # (np.exp(res) - 1)
                        'obj_id': str(obj_id),
                        'response_status': 'OK'})
    except:
        return jsonify({'prediction': -1,
                        'obj_id': str(obj_id),
                        'response_status': 'ERROR'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
