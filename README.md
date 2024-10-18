# SLE5542 Python Library

A Python library to interface with SLE5542 smart cards via PC/SC.

## Installation

1. Clone the repository

```bash
git clone https://github.com/Tikitikitikidesuka/SLE5542-Python
```

2. Navigate to the project directory

```bash
cd SLE5542-Python
```

3. Install the library

```bash
pip install .
```

After this process, you may use the library on any project.

## Usage

### Available Methods

- `select()`: Selects the smart card. 
- `read(address: int, length: int)`: Reads data from a specific memory address on the card.
- `write(address: int, length: int, data: bytes)`: Writes data to a specific memory address on the card.
- `present_psc(psc: bytes)`: Presents the Personal Security Code (PSC) to the card.
- `change_psc(psc: bytes)`: Changes the PSC on the card.
- `read_psc_error_counter()`: Reads the PSC error counter.

### Example Code

```python
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
```

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.