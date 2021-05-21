import json
import yaml
import subprocess
'''"resource": {
        "labels": {
            "bucket_name": "",
            "location": "global",
            "project_id": "deft-legacy-307909"
        },
        "type": "gcs_bucket" '''
cmd= "gcloud logging read 'resource.labels.location=global AND logName : projects/deft-legacy-307909/logs/cloudaudit.googleapis.com'  --project=deft-legacy-307909"
#resource.type=gcs_bucket AND 
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

my_bytes_value = out

# Decode UTF-8 bytes to Unicode, and convert single quotes
# to double quotes to make it valid JSON
my_str = my_bytes_value.decode('utf-8')

if my_str is not None:
    print("audit profile capturing all activities")

print(my_str)

# converting yaml format string to dict
docs1 = yaml.load_all(my_str)
yaml.warnings({'YAMLLoadWarning': False})
for doc in docs1:
    #print(doc)
    if doc['resource']['labels']['location']=="global":
        print("Ensuring that log profile captures audit logs for all regions including global")
    #converting from dict to string
    s=json.dumps(doc, indent=4, sort_keys=True) 
    #print(type(s))
    print(s)