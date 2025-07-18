from kubernetes import client, config
import base64
config.load_kube_config()
#initializing kuberntes client to fetch resources
v1 = client.CoreV1Api()
print("The secrets values listed below are: ")
print("----------------------------------------------------")
secret_name="enter the secret"
namespace="enter you namespace"
raw_secret = (v1.read_namespaced_secret(secret_name, namespace)).data
for key, value in raw_secret.items():
#   secret = (str(base64.b64decode(value).strip())).replace('b', '', 1) 
  secret = (base64.b64decode(value).decode('utf-8')).strip()
  print(f"{key}: {secret}")


