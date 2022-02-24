from configApp import create_app
import os

app = None

if __name__ == '__main__':
        app = create_app()
        app.run(host= "0.0.0.0", port=os.getenv('PORT'), debug=os.getenv('DEBUG'))
  

# INSTALAR PILLOW Y QRCODE      
#   import qrcode 

# # Crear instancia de código qr
# qr = qrcode.QRCode(
#     version = 1,
#     error_correction = qrcode.constants.ERROR_CORRECT_H,
#     box_size = 10,
#     border = 4,
# )

# # Los datos que desea almacenar
# data = "Los datos que necesita almacenar en el código QR"

# # Agregar datos
# qr.add_data(data)
# qr.make(fit=True)

# # Crea una imagen a partir de la instancia de QR Code
# img = qr.make_image()

# # Guárdelo en algún lugar, cambie la extensión según sea necesario:
# # img.save("image.png")
# # img.save("image.bmp")
# # img.save("image.jpeg")
# img.save("image.jpg")
    

    