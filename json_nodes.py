# generating the nodes part of a json graph description which will be of form:
# {"nodes":[{"id": ...},{"id": ...}],"links":[{"source": ... , "target": ... }, {"source": ... , "target": ... }]}

import pandas as pd
import csv
import os

df = pd.read_csv("Volumes/Selaphiel/Programming/Projects/School Shooters/shooterdatalists/liststablesdocs/edgelist_bare.csv")
list(df.apply(set)[0])
list(df.apply(set)[1])
temp_list = list(df.apply(set)[0]) + list(df.apply(set)[1])
nodes = list(set(temp_list))

# form the parts of each entry-as-a-string-literal
beginning = ",{\"id\":\""
end = "\"}"
nodes_string = str()

# form the string literal of each entry and append it to larger running str
i = 0
while i < len(nodes):
  new_entry = beginning+nodes[i]+end
  nodes_string = nodes_string + new_entry
  i = i + 1

# get rid of leading comma
nodes_string = nodes_string[1:]
