import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=rs5gAjNytAo&list=RDGMEMCMFH2exzjBeE_zAHHJOdxgVMrs5gAjNytAo&start_radio=1")
img.save("tereliye.png")
print("Qr code generated")