import qrcode

def QR():
    qr = qrcode.QRCode(version=1, box_size=15, border=5)
    data = input("Enter any data you want converted to a QR code: ")
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    name = input("Enter a name for the image: ")
    img.save(name)
    return img

QR()

