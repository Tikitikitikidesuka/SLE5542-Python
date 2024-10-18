from smartcard.System import readers

from sle5542 import SLE5542


def main():
    try:
        reader = readers()[0]
        connection = reader.createConnection()
        connection.connect()
        card = SLE5542(connection)

        card.select()
        card.present_psc(bytes([0xFF, 0xFF, 0xFF]))
        for address in range(0x20, 0x100, 0x10):
            data, ok = card.write(address, 0x10, bytes([0x00] * 0x10))
    except Exception as e:
        print(f"Error reading card: {e}")


if __name__ == "__main__":
    main()
