import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Đọc dữ liệu
df = pd.read_csv("data.csv")

X = df[["Toan", "Van", "Anh", "Yeu_thich_cong_nghe"]]
y = df["Nganh"]

# Tạo mô hình
model = RandomForestClassifier()
model.fit(X, y)

# Lưu model
joblib.dump(model, "model.pkl")

print("Đã tạo xong model.pkl")
