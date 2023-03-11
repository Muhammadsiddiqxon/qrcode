import qrcode as qr

def create_qr(object = "Qr_Code", name = "QR"):
    try:
        code = qr.make(data = object)
        saved = code.save(stream = f"{name}.png")
        return True
    except:
        return False
def main():
    obj = input("Введите слово превратить на шифрку: ")
    name = input("Введите имя шифрку: ")

    create_qr(object = obj, name = name)

if __name__ == '__main__':
    main()