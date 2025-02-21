from pymongo import MongoClient
from config import DATABASE_URI, DATABASE_NAME

class Database:
    def __init__(self):
        self.client = MongoClient(DATABASE_URI)
        self.db = self.client[DATABASE_NAME]
        self.files_collection = self.db["files"]

    def add_file(self, file_name: str, file_link: str):
        """Add a file to the database."""
        self.files_collection.insert_one({"file_name": file_name, "file_link": file_link})

    def search_files(self, query: str):
        """Search files in the database."""
        return list(self.files_collection.find({"file_name": {"$regex": query, "$options": "i"}}))