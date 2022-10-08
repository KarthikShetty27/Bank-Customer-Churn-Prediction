# Import Flask modules
from flask import Flask, render_template, request

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# Open our model
from tensorflow import keras
model = keras.models.load_model('ann_model')

# print(model.predict([[0, 1, 0, 800, 1, 21, 5, 6000, 4, 1, 1, 50000]]) > 0.5)

# Initialize Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    geography = request.form['geography']
    creditscore = int(request.form['creditScore'])
    gender = int(request.form['gender'])
    age = int(request.form['age'])
    tenure = int(request.form['tenure'])
    balance = int(request.form['balance'])
    numofproducts = int(request.form['numofproducts'])
    hascrcard = int(request.form['hascrcard'])
    isactivemember = int(request.form['isactivemember'])
    estimatedsalary = int(request.form['estimatedsalary'])

    g1 = int(geography[0])
    g2 = int(geography[2])
    g3 = int(geography[4])

    pred = model.predict([[g1, g2, g3, creditscore, gender, age, tenure, balance, numofproducts, hascrcard, isactivemember, estimatedsalary]])
    prediction = int(pred)
    print(prediction)

    if prediction == 1:
        result = "Therefore, Our model predicts that the customer will not stay in the bank."
    else:
        result = "Therefore, Our model predicts that the customer will stay in the bank."


    return render_template('predict.html', prediction_text=result)


# Run app
if __name__ == "__main__":
    app.run(debug=True)
