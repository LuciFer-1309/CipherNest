
import os
from io import BytesIO

from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet, InvalidToken


app = Flask(__name__)

# Fernet key Vercel ke environment variable se load hogi
key_value = os.environ.get("FERNET_KEY")

if not key_value:
    raise RuntimeError(
        "FERNET_KEY environment variable is missing. "
        "Please configure it before starting the application."
    )

try:
    FERNET_KEY = key_value.encode("ascii")
    Fernet(FERNET_KEY)  # Verify that the key is valid
except (ValueError, UnicodeEncodeError):
    raise RuntimeError("FERNET_KEY is invalid. Generate a valid Fernet key.")


# Caesar Cipher encryption
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            position = ord(char) - ord("A")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("A"))

        elif char.islower():
            position = ord(char) - ord("a")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("a"))

        else:
            result += char

    return result


# Caesar Cipher decryption
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Main website page
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    message = ""
    error = ""
    operation = "encrypt"
    method = "fernet"
    shift = 3

    if request.method == "POST":
        operation = request.form.get("operation", "encrypt")
        method = request.form.get("method", "fernet")
        text = request.form.get("text", "")

        try:
            shift = int(request.form.get("shift", "3"))

            if not text.strip():
                raise ValueError("Please enter a message.")

            if operation not in ("encrypt", "decrypt"):
                raise ValueError("Invalid operation selected.")

            if method not in ("caesar", "fernet"):
                raise ValueError("Invalid encryption method selected.")

            if method == "caesar":
                if not 0 <= shift <= 25:
                    raise ValueError("Shift must be between 0 and 25.")

                if operation == "encrypt":
                    result = caesar_encrypt(text, shift)
                else:
                    result = caesar_decrypt(text, shift)

            else:
                cipher = Fernet(FERNET_KEY)

                if operation == "encrypt":
                    result = cipher.encrypt(
                        text.encode("utf-8")
                    ).decode("ascii")
                else:
                    result = cipher.decrypt(
                        text.encode("ascii")
                    ).decode("utf-8")

            message = "Operation completed successfully!"

        except (ValueError, UnicodeError):
            error = (
                "Invalid input. Check your message, shift "
                "and encrypted text."
            )

        except InvalidToken:
            error = (
                "Decryption failed. The encrypted text may be "
                "incorrect, or the key may not match."
            )

        except Exception:
            error = "Something went wrong. Please try again."

    return render_template(
        "index.html",
        result=result,
        message=message,
        error=error,
        operation=operation,
        method=method,
        shift=shift
    )


# Download output as a text file
@app.route("/download", methods=["POST"])
def download():
    text = request.form.get("result", "")

    if not text:
        return "There is no output to download.", 400

    file_data = BytesIO(text.encode("utf-8"))
    file_data.seek(0)

    return send_file(
        file_data,
        mimetype="text/plain",
        as_attachment=True,
        download_name="encrypted_message.txt"
    )


if __name__ == "__main__":
    app.run(debug=False)
