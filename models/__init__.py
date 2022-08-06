#!/usr/bin/python3

from models.engine.file_storage import FileStorage

# persist all data objects every time program is launch
storage = FileStorage()
storage.reload()
