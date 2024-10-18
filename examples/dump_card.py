from smartcard.System import readers
from smartcard.util import toHexString, toASCIIString

from sle5542 import SLE5542


def main():
    try:
        reader = readers()[0]
        connection = reader.createConnection()
        connection.connect()
        card = SLE5542(connection)

        card.select()
        for line in range(0x10):
            data, ok = card.read(0x10 * line, 0x10)
            print(toHexString(data) + " -> " + toASCIIString(data))
    except Exception as e:
        print(f"Error reading card: {e}")


if __name__ == "__main__":
    main()
