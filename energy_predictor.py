from sklearn.linear_model import LinearRegression
import numpy as np

def predict_energy(df):
    df["time_step"] = np.arange(len(df))

    X = df[["time_step"]]
    y = df["cpu"]

    model = LinearRegression()
    model.fit(X, y)

    future = np.arange(len(df), len(df)+50).reshape(-1,1)
    predicted_cpu = model.predict(future)

    return predicted_cpu.mean()