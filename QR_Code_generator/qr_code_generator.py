import qrcode


data = input('Enter the text or URL:').strip()
while True:
    format_of_image = ('.png', '.jpg')
    filename = input('Enter the filename: ').strip()
    if filename.endswith(format_of_image):
        break
    print('enter file name as filename.jpg or filename.png')

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')