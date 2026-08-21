from flask import Flask, request, Response
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    w = request.args.get("w", 240, type=int)
    h = request.args.get("h", 320, type=int)
    r = requests.get(f"https://picsum.photos/{w}/{h}", timeout=10)
    im = Image.open(BytesIO(r.content))

    buf = BytesIO()
    im.save(buf, format="JPEG", quality=80, interlace=0)
    data = buf.getvalue()

    headers = {
        "Content-Length": str(len(data)),
        "Content-Type": "image/jpeg"
    }
    return Response(data, headers=headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
