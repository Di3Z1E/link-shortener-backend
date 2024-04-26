import uuid 
from json_manager import JsonManager

class LinkShortener:
    @staticmethod
    def shorten(url: str) -> str:
        """
        Shorten a URL and return its unique ID.

        Args:
            url (str): The URL to shorten.

        Returns:
            str: The unique ID representing the shortened URL.
        """
        unique_id = str(uuid.uuid4())[:8]
        new_url_entity = {"id": unique_id, "url": url}
        url_entities = JsonManager.read()
        url_entities.append(new_url_entity)
        JsonManager.write(url_entities)
        return unique_id
