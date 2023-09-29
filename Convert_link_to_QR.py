import qrcode

# Ваша ссылка
url = "https://github.com/kr1zy"

# Создать объект QR-кода
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Добавить данные (в данном случае - ссылку)
qr.add_data(url)
qr.make(fit=True)

# Создать изображение QR-кода
img = qr.make_image(fill_color="black", back_color="white")

# Сохранить изображение QR-кода в файл
img.save("qrcode.png")

# Показать QR-код
img.show()