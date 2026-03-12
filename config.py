import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # ------------------------------
    # Azure Blob Storage
    # ------------------------------
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'articlecmsstorageaditya'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'VomofpjpyTS9q56etrke2OwjQEadvjkJqXFCI47jc7/Ai8HhG56cJ2mShAXNkkpwJS1eAQw7SHIH+AStFdmXYw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # ------------------------------
    # Azure SQL Database
    # ------------------------------
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacitycmsaditya.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'articlecmsdb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'azureadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Udacity@12345'

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ------------------------------
    # Microsoft Authentication (MSAL)
    # ------------------------------
    CLIENT_SECRET = "qM58Q~jqKUH.I.XKAF4Z8WbShO-CQAOk6tK71az."

    AUTHORITY = "https://login.microsoftonline.com/common"

    CLIENT_ID = "7fb96afa-db98-4706-b69e-21e447ca6dbe"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
