#!/usr/bin/env python3
url = "www.umbctraining.com"
result = url.startswith("www")
print(result)
print(url.endswith(".org"))
new_url = url.upper()
print("ORIGINAL", url, "RETURNED", new_url)

url = url.upper()

print(url)

data = "foo:bar:blah"
fields = data.split(":")
print(fields)

data = "wombat wolverine weasel wildebeest"
fields = data.split()
print(fields)
