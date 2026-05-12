print("Biometric system starting...")
For testing : 
Create app.py

from flask import Flask, render_template, request, redirect, url_for, session
import pyotp
import datetime

app = Flask(__name__)
app.secret_key = "bhuwan_secret_key"

# Demo username and password
USERNAME = "bhuwan"
PASSWORD = "1234"

# Fixed secret key for MFA
SECRET_KEY = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(SECRET_KEY)

def write_log(message):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["user_ok"] = True
            write_log("Username/password login success")
            return redirect(url_for("otp"))
        else:
            write_log("Username/password login failed")
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@app.route("/otp", methods=["GET", "POST"])
def otp():
    if not session.get("user_ok"):
        return redirect(url_for("login"))

    if request.method == "POST":
        code = request.form.get("otp")

        if totp.verify(code):
            session["otp_ok"] = True
            write_log("OTP verification success")
            return redirect(url_for("face"))
        else:
            write_log("OTP verification failed")
            return render_template("otp.html", error="Invalid OTP")

    return render_template("otp.html")

@app.route("/face", methods=["GET", "POST"])
def face():
    status = None

    if not session.get("otp_ok"):
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            with open("face_status.txt", "r") as f:
                status = f.read().strip()
        except FileNotFoundError:
            status = "not_detected"

        if status == "detected":
            write_log("Face verification success")
            return redirect(url_for("success"))
        else:
            write_log("Face verification failed")
            return render_template("face.html", status=status, error="No face detected")

    return render_template("face.html", status=status)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)


result: /app.py"
 * Serving Flask app 'app'
 * Debug mode: on
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
On macOS, try searching for and disabling 'AirPlay Receiver' in System Settings.
bhuwankandel@Bhuwans-Laptop Bhuwan_Project 2 %


Create face.py

import cv2

# Load face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)

# Check if camera opened
if not cap.isOpened():
    print("Camera could not be opened.")
    with open("face_status.txt", "w") as f:
        f.write("not_detected")
    exit()

print("Show your face to the camera.")
print("Press q to exit.")

detected_once = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        text = "Face Detected"
        detected_once = True
    else:
        text = "No Face Detected"

    # Draw rectangle around face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show text
    cv2.putText(frame, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    # Show webcam window
    cv2.imshow("Biometric Authentication", frame)

    # Quit on q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

with open("face_status.txt", "w") as f:
    if detected_once:
        f.write("detected")
        print("Face status saved as: detected")
    else:
        f.write("not_detected")
        print("Face status saved as: not_detected")


while it is run it appears like this s/bhuwankandel/Desktop/Bhuwan_Project 
2/face.py"
Show your face to the camera.
Press q to exit.



Create mfa.py 
import pyotp
import qrcode

# Generate secret key
secret = "JBSWY3DPEHPK3PXP"
totp = pyotp.TOTP(secret)

print("Your secret key is:", secret)
print("Add this key to Google Authenticator manually.")

# Create QR code
uri = totp.provisioning_uri(name="BhuwanSIDPS", issuer_name="SIDPS Project")
img = qrcode.make(uri)
img.save("mfa_qr.png")

print("QR code saved as mfa_qr.png")

# Ask for OTP4
while True:
    code = input("Enter OTP: ").strip()

    if totp.verify(code):
        print("Access Granted")
        break
    else:
        print("Invalid Code")


result: bhuwankandel/Desktop/Bhuwan_Project 
2/mfa.py"
