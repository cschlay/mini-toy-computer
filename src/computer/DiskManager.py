from pathlib import PurePath
from sqlite3 import connect

from computer.BinaryNumber import BinaryNumber


class DiskManager:
    """
    Used to read or write to the "disk".
    We emulate the disk with .sqlite3 database.
    It has only one table and two columns 'address' and 'data'.
    """

    def __init__(self, disk_location: str, partition: str = 'main'):
        """
        Construct a new disk manager and creates necessary tables if the "disk" does not have them.
        """
        self.location: str = disk_location
        self.partition: str = partition
        disk = connect(self.location)
        disk.execute(f"CREATE TABLE IF NOT EXISTS {self.partition} (address INTEGER PRIMARY KEY, data TEXT NOT NULL)")

        # se = Start Address, ea = End Address
        disk.execute("CREATE TABLE IF NOT EXISTS programs"
                     "(name TEXT PRIMARY KEY, sa INTEGER NOT NULL, ea INTEGER NOT NULL)")
        disk.close()

    def is_empty(self, start: int, end: int) -> bool:
        """
        Check whether addresses [start, end] are empty.
        """
        disk = connect(self.location)
        cursor = disk.cursor()
        cursor.execute(f"SELECT * FROM {self.partition} WHERE address >= {start} and address <= {end}")

        status: bool = cursor.fetchone is None
        disk.close()

        return status

    def install(self, program: str):
        """
        Read a program from file and store it to the disk.
        """
        disk = connect(self.location)
        cursor = disk.cursor()
        cursor.execute(f"SELECT MAX(address) from {self.partition}")

        # Let's assume it is the addresses after the highest used address are empty.
        max_address = cursor.fetchone()[0]
        start_address: int = 0 if max_address is None else max_address + 1
        address: int = start_address

        with open(program) as file:
            for line in file:
                cursor.execute(f"INSERT INTO {self.partition} VALUES ({address}, '{line}')")
                address += 1

        program_name: str = PurePath(program).stem
        cursor.execute(f"INSERT INTO programs VALUES ('{program_name}', {start_address}, {address})")

        disk.commit()
        disk.close()

    def uninstall(self):
        """
        Removes an installed program by name.
        """
        pass

    def read(self, address: int) -> BinaryNumber:
        """
        Reads data from the "disk".
        Returns the data if it exists else returns 0.
        """
        disk = connect(self.location)
        cursor = disk.cursor()
        cursor.execute(f"SELECT data FROM {self.partition} WHERE address = {address}")
        data = cursor.fetchone()
        disk.close()

        if data is not None:
            return BinaryNumber(data[0])
        else:
            return BinaryNumber()

    def write(self, address: int, data: BinaryNumber):
        """
        Write data to the disk.
        """
        disk = connect(self.location)
        cursor = disk.cursor()
        cursor.execute(f"SELECT data FROM main WHERE address = {address}")

        data_string = data.real_str()
        if cursor.fetchone() is None:
            disk.execute(f"INSERT INTO {self.partition} VALUES ({address}, '{data_string}')")
        else:
            disk.execute(f"UPDATE {self.partition} SET data = '{data_string}' WHERE address = {address}")
        disk.commit()
        disk.close()

