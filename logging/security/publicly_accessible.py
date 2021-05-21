import google.cloud.logging
import logging
client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()
text = 'Hello, world!'
logging.warning(text)
for entry in client.list_entries():
    print(entry)