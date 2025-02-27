from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv(r"C:\Users\neba\Desktop\brent_oil\data\processed\BrentOilPrices_Cleaned.csv")  # Load your data

@app.route('/api/oil_prices', methods=['GET'])
def get_oil_prices():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    else:
        filtered_df = df

    data = filtered_df[['Date', 'Avg_Price']].to_dict(orient='records')
    return jsonify(data)

@app.route('/api/correlations', methods=['GET'])
def get_correlations():
    correlation_data = {
        "Federal Funds Annual % change": 0.044578,
        "Average Closing Price": 0.993423,
        "WTA Crude Oil Year Open": 0.963548,
        "WTA Crude Oil Year High": 0.969042,
        "WTA Crude Oil Year Low": 0.923571,
        "WTA Crude Oil Year Close": 0.883179,
        "GDP FRANCE": 0.883835,
        "Year": 0.748065,
        "GDP USA": 0.736781,
        "GDP INDIA": 0.710435,
        "GDP CHINA": 0.663119,
        "Unemployment (China)": 0.611468,
        "GDP JAPAN": 0.595700,
        "Unemployment (USA)": 0.253987,
        "Inflation (USA)": -0.005927,
        "Inflation (France)": -0.025700,
        "Inflation (Japan)": -0.038208,
        "Inflation (India)": -0.040826,
        "WTA Crude Oil Annual % Change": -0.105616,
        "Unemployment (India)": -0.332953,
        "Inflation (China)": -0.333869,
        "Europe & Central Asia (IDA & IBRD countries) Unemployment": -0.419435,
        "Inflation (Germany)": -0.518169,
        "Federal Funds Year Close": -0.529670,
        "Federal Funds Average Yield": -0.541681,
        "Federal Funds Year Open": -0.542303,
        "Federal Funds Year Low": -0.548969,
        "Federal Funds Year High": -0.593096
    }
    return jsonify(correlation_data)

if __name__ == '__main__':
    app.run(debug=True)