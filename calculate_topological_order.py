import sys
import re
from collections import defaultdict

# Read the dependencies file
with open(sys.argv[1], 'r') as file:
    dependencies_data = file.read()

# Split dependencies by ;
dependencies_list = dependencies_data.split(';')

# Create a dictionary to store dependencies
dependencies = defaultdict(list)

# Parse the dependencies and build the dependency map
for dep in dependencies_list:
    # Extract project_a and project_b using regex
    matches = re.findall(r'"(.*?)" -> "(.*?)"', dep)
    if matches:
        project_a, project_b = matches[0]
        dependencies[project_a].append(project_b)

# Get the projects as command-line arguments
projects = sys.argv[2].split()

# Initialize an empty set to store the topological order
topological_order = set()

# Function to perform depth-first search (DFS) and populate the topological order
def dfs(project):
    # Check if the project has already been visited
    if project in topological_order:
        return

    topological_order.add(project)

    for dep in dependencies[project]:
        dfs(dep)

# Perform DFS on each project
for project in projects:
    dfs(project)

topological_order_string = ""
# Print the topological order for the input projects in "a"->"b"; format
for project in projects:
    for dep in dependencies[project]:
        if dep in topological_order:
            topological_order_string += f'"{project}" -> "{dep}";'

print(topological_order_string)