import pyqrcode 

url=input("enter the url to create qr code for: \n ")
qr=pyqrcode.create(url)
qr.png("webqr.png",scale=8)