# monorepoworkflows

- Triggers the workflow on push or pull request events but only for the `main` branch. Additionally ignore if only `README.md`
file changes.
- Gets all the files changed/modified in a pull request or push's commits.
- Filters our the projects in `.deployignore` and the projects where only `README.md` files are modififed.
- Calculates the topological order for the modified projects and print out on the GitHub Actions UI.
  The script `calculate_topological_order.py` takes `project dependencies DAG` and the `filtered projects` as inputs
  and prints the topological order which is a subset of the original topological order from the raw DAG file.