
# QR Code Generator

import qrcode as qr

user_text = input("Enter the text or URL: ").strip()
file_name = input("Enter the file name: ").strip()
file_name = f"{file_name}.jpg"

# Method I
# img = qr.make(user_text)
# img.save(f"./QR_Code_Generator/{file_name}")
# print(f"QR code saved as {file_name}")


# Method II
qrConfig = qr.QRCode(box_size=10, border=4)
qrConfig.add_data(user_text)
qrConfig.make(fit=True)
img = qrConfig.make_image(fill_color="black", back_color="white")
img.save(f"./QR_Code_Generator/{file_name}")
