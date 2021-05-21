import google.cloud.logging
#preq create a service account and assign it to an envinornment variable -//cloud.google.com/logging/docs/reference/libraries#client-libraries-install-python

import logging
#from google.cloud import logging_v2


client = google.cloud.logging.Client()

client.setup_logging()

text = 'Hello, world!'

logging.warning(text)



#client2 = logging_v2.LoggingServiceV2Client()
#entries = []
#response = client2.write_log_entries(entries)
#print(response)

#logger = client.logger('log_name')
filter_str ="resource.type:global"
count=0
for entry in client.list_entries(filter_=filter_str):
    #if resource.type="global":
    count=count+1
    print("****************")
    print(entry)
    #print(type(entry))
print(count)
if count>1:
    print("logging profile is sucessfully verified")
#resource.type="gce_instance" AND
#log_id("syslog")
#filter_str = "logName:log_name AND textPayload:simple"
#for entry in client.list_entries(filter_=filter_str):  # API call(s)
    #do_something_with(entry)
