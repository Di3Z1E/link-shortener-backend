import json

class JsonManager:
    FILE_NAME = "links.json"

    @staticmethod
    def read() -> list:
        """
        Read data from the JSON file.

        Returns:
            list: List containing JSON data.
        """
        try:
            with open(JsonManager.FILE_NAME) as f:
                data = json.load(f)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def write(data: list) -> bool:
        """
        Write data to the JSON file.

        Args:
            data (list): List containing JSON data to write.

        Returns:
            bool: True if writing is successful, False otherwise.
        """
        try:
            with open(JsonManager.FILE_NAME, "w") as f:
                json.dump(data, f)
            return True
        except Exception as e:
            print("Error writing JSON:", e)
            return False
