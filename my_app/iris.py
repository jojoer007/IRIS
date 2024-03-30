from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

def predict_iris(features):
# โหลดข้อมูล IRIS
    iris = load_iris()
    X = iris.data
    y = iris.target

# สร้างและฝึกโมเดล Decision Tree
    model = DecisionTreeClassifier()
    model.fit(X, y)

# บันทึกโมเดลเป็นไฟล์
    joblib.dump(model, 'decision_tree_model.pkl')

# โหลดโมเดล
    loaded_model = joblib.load('decision_tree_model.pkl')

# ใช้โมเดลทำนาย
    prediction = loaded_model.predict(features)[0]
    
    value = []
    for label in prediction:
        if label == 0:
            value.append('Setosa')
        elif label == 1:
            value.append('Virginica')
        else:
            value.append('Versicolour')
    
    return value