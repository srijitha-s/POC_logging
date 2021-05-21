import google.cloud.logging
#preq create a service account and assign it to an envinornment variable -//cloud.google.com/logging/docs/reference/libraries#client-libraries-install-python

import logging

client = google.cloud.logging.Client()

client.setup_logging()

text = 'Hello, world!'

logging.warning(text)
print("Logged: {}".format(text))

filter_str ="resource.type:global"
count=0
for entry in client.list_entries(filter_=filter_str):
    #if resource.type="global":
    count=count+1
    print("****************")
    print(entry)
    #print(type(entry))
print(count)
if count>=1:
    print("logging profile is sucessfully verified")
