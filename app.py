from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Placeholder machine learning function
def predict(input_data):
    # Replace this function with your actual machine learning model
    # In this example, it just returns the input data as it is
    return {'prediction': input_data}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        data = request.get_json()
        print("data: ", data)

        if 'inputs' in data and isinstance(data['inputs'], list):
            input_data = data['inputs']
            print("input_data: ", input_data)
            print(input_data[0])
            print(input_data[1])

            # Call the predict function with the input data
            prediction = predict(input_data)
            print(prediction)

            return jsonify(prediction)
        else:
            return jsonify({'error': 'Invalid JSON format. Missing "inputs" key or not a list.'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
