import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, Canvas, PhotoImage
from PIL import Image, ImageTk

def generate_qr():
    """Generate QR Code and display it in the GUI."""
    global qr_img
    data = input_entry.get()
    if data.strip():
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        qr_img = img
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(100, 100, image=img_tk)
        canvas.image = img_tk
        status_label.config(text="QR Code Generated Successfully!", fg="green")
    else:
        status_label.config(text="Please enter valid data to generate QR Code.", fg="red")

def save_qr():
    """Save the generated QR Code as a PNG file."""
    if qr_img:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save QR Code"
        )
        if file_path:
            qr_img.save(file_path)
            status_label.config(text="QR Code saved successfully!", fg="green")
    else:
        status_label.config(text="Generate a QR Code before saving.", fg="red")

# Initialize Tkinter window
app = Tk()
app.title("QR Code Generator")
app.geometry("400x400")
app.resizable(False, False)

# Input label and entry
Label(app, text="Enter Data to Generate QR Code:", font=("Arial", 12)).pack(pady=10)
input_entry = Entry(app, font=("Arial", 12), width=30)
input_entry.pack(pady=10)

# Buttons
Button(app, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)
Button(app, text="Save QR Code", command=save_qr, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

# Canvas for displaying the QR code
canvas = Canvas(app, width=200, height=200, bg="white")
canvas.pack(pady=20)

# Status label
status_label = Label(app, text="", font=("Arial", 10))
status_label.pack(pady=10)

# Global QR Image
qr_img = None

# Run the Tkinter event loop
app.mainloop()
