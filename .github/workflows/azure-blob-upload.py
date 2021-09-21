import os
import sys

from azure.storage.blob import BlobClient

print(f"using python executable: {sys.executable}")
print(f"workdir is: {os.getcwd()}")

def blob_upload(filepath):
    blob_client = BlobClient.from_connection_string(
        conn_str=os.environ["AZURE_CONN_STR"],
        container_name=os.environ["AZURE_CONTAINER_NAME"],
        blob_name=os.environ["AZURE_BLOB_NAME"],
    )

    with open(filepath, "rb") as fh:
        blob_client.upload_blob(fh, overwrite=True)


if __name__ == "__main__":
    import sys
    blob_upload(filepath=sys.argv[1])
