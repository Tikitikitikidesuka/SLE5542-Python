import random

from smartcard.System import readers
from smartcard.util import toHexString, toASCIIString

from sle5542 import SLE5542

ADDRESS = 0x20
LENGTH = 0x10
DATA = ("Lucky number " + f"{random.randint(0, 999):03}").encode('ASCII')
PSC = bytes([0xFF, 0XFF, 0XFF])


def main():
    try:
        reader = readers()[0]
        connection = reader.createConnection()
        connection.connect()
        card = SLE5542(connection)

        card.select()
        read_data, success = card.read(ADDRESS, LENGTH)
        print(
            f"Read \"{toASCIIString(read_data)}\" at address {ADDRESS} " + "successfully" if success else "unsucessfully")
        card.present_psc(PSC)
        _, success = card.write(ADDRESS, LENGTH, DATA)
        print(
            f"Wrote \"{toASCIIString(DATA)}\" to address {ADDRESS} " + "successfully" if success else "unsuccessfully")
        read_data, success = card.read(ADDRESS, LENGTH)
        print(
            f"Read \"{toASCIIString(read_data)}\" at address {ADDRESS} " + "successfully" if success else "unsucessfully")
    except Exception as e:
        print(f"Error reading card: {e}")


if __name__ == "__main__":
    main()
