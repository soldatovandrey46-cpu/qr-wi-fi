from PIL import Image

ssid = 'TP-Link_1C0E_5G'
password = '68745745'
security = 'WPA'

from wifi_qrcode_generator.generator import wifi_qrcode
qr = wifi_qrcode(ssid, False, security, password)

qr.make_image().save('wifi_qr.png')
Image.open('wifi_qr.png')
