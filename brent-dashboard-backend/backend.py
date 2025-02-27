from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import json
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import os
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load datasets
DATA_FOLDER = "./data"

def load_data():
    try:
        df = pd.read_csv(os.path.join(DATA_FOLDER, "BrentOilPrices_Cleaned.csv"))
        date_cols = [col for col in df.columns if 'date' in col.lower() or 'year' in col.lower()]
        if date_cols:
            df[date_cols[0]] = pd.to_datetime(df[date_cols[0]])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def load_models():
    try:
        models = {}
        model_files = [f for f in os.listdir(os.path.join(DATA_FOLDER, "models")) if f.endswith('.pkl')]
        for model_file in model_files:
            model_name = model_file.split('.')[0]
            with open(os.path.join(DATA_FOLDER, "models", model_file), 'rb') as f:
                models[model_name] = pickle.load(f)
        return models
    except Exception as e:
        print(f"Error loading models: {e}")
        return {}

def load_events():
    try:
        events_df = pd.read_csv(os.path.join(DATA_FOLDER, "significant_events.csv"))
        return events_df
    except:
        events = [
            {"date": "2008-07-11", "event": "Oil price peak before financial crisis", "category": "Economic"},
            {"date": "2014-06-20", "event": "ISIS conflict in Iraq", "category": "Geopolitical"},
            {"date": "2016-01-20", "event": "Oil price crash below $30", "category": "Market"},
            {"date": "2020-03-09", "event": "Saudi-Russia price war", "category": "Geopolitical"},
            {"date": "2020-04-20", "event": "WTI crude futures negative prices", "category": "Market"},
            {"date": "2022-02-24", "event": "Russia-Ukraine conflict begins", "category": "Geopolitical"}
        ]
        return pd.DataFrame(events)

@app.route('/api/data', methods=['GET'])
def get_data():
    df = load_data()
    if df.empty:
        return jsonify({"error": "Data not available"}), 404
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if start_date and 'date' in df.columns:
        df = df[df['date'] >= start_date]
    if end_date and 'date' in df.columns:
        df = df[df['date'] <= end_date]
    return jsonify(df.to_dict(orient='records'))

@app.route('/api/summary', methods=['GET'])
def get_summary():
    df = load_data()
    if df.empty:
        return jsonify({"error": "Data not available"}), 404
    target_col = 'Avg_Price' if 'Avg_Price' in df.columns else 'brent_price'
    summary = {
        "count": len(df),
        "mean": float(df[target_col].mean()),
        "median": float(df[target_col].median()),
        "min": float(df[target_col].min()),
        "max": float(df[target_col].max()),
        "std": float(df[target_col].std()),
        "current": float(df[target_col].iloc[-1]),
        "annual_change": float(df[target_col].iloc[-1] - df[target_col].iloc[-13]) if len(df) > 12 else 0,
        "volatility": float(df[target_col].rolling(window=12).std().iloc[-1]) if len(df) > 12 else 0
    }
    return jsonify(summary)

@app.route('/api/correlations', methods=['GET'])
def get_correlations():
    df = load_data()
    if df.empty:
        return jsonify({"error": "Data not available"}), 404
    target_col = 'Avg_Price' if 'Avg_Price' in df.columns else 'brent_price'
    corr = df.corr()[target_col].sort_values(ascending=False)
    correlations = [{
        "variable": var,
        "correlation": float(val),
        "magnitude": abs(float(val))
    } for var, val in corr.items() if var != target_col]
    return jsonify(correlations)

@app.route('/api/events', methods=['GET'])
def get_events():
    events_df = load_events()
    return jsonify(events_df.to_dict(orient='records'))

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    models = load_models()
    df = load_data()
    if df.empty:
        return jsonify({"error": "Data not available"}), 404

    # ARIMA Forecast
    arima_model = ARIMA(df['Avg_Price'], order=(2, 1, 0))
    arima_fit = arima_model.fit()
    arima_forecast = arima_fit.forecast(steps=5).tolist()

    # Gradient Boosting Forecast
    if 'GradientBoosting' in models:
        model = models['GradientBoosting']
        features = ['Average Closing Price', 'WTA Crude Oil Year Open', 'WTA Crude Oil Year High', 'WTA Crude Oil Year Low', 'WTA Crude Oil Year Close', 'GDP USA', 'GDP CHINA', 'GDP INDIA', 'GDP FRANCE', 'Unemployment (China)', 'Inflation (USA)', 'Inflation (China)', 'Avg_Price_lag1', 'Avg_Price_lag2', 'Avg_Price_rolling_mean_3']
        last_data = df[features].iloc[-1:].values
        gb_forecast = model.predict(last_data).tolist()
    else:
        gb_forecast = [85 + i for i in range(5)] # Dummy if no model

    forecasts = []
    for i in range(5):
        forecasts.append({
            "date": f"2025-{(i+1):02d}-01",
            "forecast": (arima_forecast[i] + gb_forecast[0]) / 2, # Average of both models
            "lower_bound": (arima_forecast[i] + gb_forecast[0]) / 2 * 0.95,
            "upper_bound": (arima_forecast[i] + gb_forecast[0]) / 2 * 1.05
        })
    return jsonify(forecasts)

@app.route('/api/model_performance', methods=['GET'])
def get_model_performance():
    models_perf = [
        {"model": "ARIMA", "rmse": 18.52, "mae": 15.00, "mape": 20.00, "r2": 0.70},
        {"model": "Gradient Boosting", "rmse": 16.12, "mae": 13.00, "mape": 22.08, "r2": 0.85}
    ]
    return jsonify(models_perf)

@app.route('/api/feature_importance', methods=['GET'])
def get_feature_importance():
    features = [
        {"feature": "Average Closing Price", "importance": 0.873635},
        {"feature": "WTA Crude Oil Year High", "importance": 0.055673},
        {"feature": "WTA Crude Oil Year Open", "importance": 0.023532},
        {"feature": "Avg_Price_lag1", "importance": 0.011490},
        {"feature": "GDP FRANCE", "importance": 0.008797},
        {"feature": "WTA Crude Oil Year Low"}
    ]