from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        res = requests.get("http://x.x.x.x:5000/hello", timeout=3)
        msg = res.json().get("message", "Sin respuesta")
    except Exception as e:
        msg = f"Error: {e}"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Frontend en AWS</title></head>
    <body>
        <h1>Respuesta desde GCP:</h1>
        <p>{{{{ msg }}}}</p>
    </body>
    </html>
    """
    return render_template_string(html, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
