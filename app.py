from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Inicializa PrometheusMetrics para crear automáticamente el endpoint /metrics
metrics = PrometheusMetrics(app)

# Opcional: Define métricas personalizadas
# Por ejemplo: un contador para rastrear el número de visitas a la página principal
metrics.info('app_info', 'Application Info', version='1.0.0')

@app.route("/")
def home():
    return "Hello, Dockerized Flask App!"

@app.route("/api")
def api():
    return {"message": "This is a simple API"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
