from sqlite3 import connect

from BinaryNumber import BinaryNumber


class DiskManager:
    """
    Used to read or write to the "disk".
    We emulate the disk with .sqlite3 database.
    It has only one table and two columns 'address' and 'data'.
    """

    def __init__(self, disk_location: str):
        """
        Construct a new disk manager and creates necessary tables if the "disk" does not have them.
        """
        self.location = disk_location
        disk = connect(self.location)
        disk.execute("CREATE TABLE IF NOT EXISTS main (address INTEGER PRIMARY KEY, data TEXT)")
        disk.close()

    def read(self, address: int) -> BinaryNumber:
        """
        Reads data from the "disk".
        Returns the data if it exists else returns 0.
        """
        disk = connect(self.location)
        cursor = disk.cursor()
        cursor.execute(f"SELECT data FROM main WHERE address = {address}")
        data = cursor.fetchone()
        disk.close()

        if data is not None:
            return BinaryNumber(data[0])
        else:
            return BinaryNumber()

    def write(self, address: int, data: BinaryNumber):
        """
        Writes data to the disk.
        """
        disk = connect(self.location)
        cursor = disk.cursor()
        cursor.execute(f"SELECT data FROM main WHERE address = {address}")

        data_string = data.real_str()
        if cursor.fetchone() is None:
            disk.execute("INSERT INTO main VALUES (?, ?)", (address, data_string))
        else:
            disk.execute(f"UPDATE main SET data = '{data_string}' WHERE address = {address}")
        disk.commit()
        disk.close()
