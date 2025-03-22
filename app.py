from flask import Flask, render_template, request
from elgamal import ElGamal

app = Flask(__name__)

elgamal = ElGamal()
keys = elgamal.generate_keys()
public_key = keys["public_key"]
private_key = keys["private_key"]

@app.route("/", methods=["GET", "POST"])
def home():
    """Home Page - Accepts Message Input for Encryption."""
    if request.method == "POST":
        message = request.form["message"]
        ciphertext = elgamal.encrypt(message)
        return render_template("encrypt.html", message=message, ciphertext=ciphertext, public_key=public_key)

    return render_template("index.html")

@app.route("/decrypt", methods=["POST"])
def decrypt():
    """Decrypt Page - Decrypts Ciphertext and Displays Original Message."""
    c1 = int(request.form["c1"])
    c2 = int(request.form["c2"])
    ciphertext = (c1, c2)
    decrypted_message = elgamal.decrypt(ciphertext)
    return render_template("decrypt.html", decrypted_message=decrypted_message, private_key=private_key)

if __name__ == "__main__":
    app.run(debug=True)
