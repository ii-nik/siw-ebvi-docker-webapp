#!/usr/bin/python

import os
from jinja2 import Environment, FileSystemLoader

user = os.environ["USER"]
print ("Prepare docker-compose.yml for user {}".format(user))
env = Environment(loader = FileSystemLoader("./"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("./docker-compose.jinja")
data = template.render(user=user)
file = open("docker-compose.yml", 'w')
file.write(data)
file.close()
print("Done")
