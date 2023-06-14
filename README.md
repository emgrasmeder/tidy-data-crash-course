# A Tidy Data Crash Course
So you're a pretty decent software dev, but for some reason you have to start working with data for the first time. Most likely, spreadsheets worked fine for your team/org while you proved the business hypothesis, and now you need to build something more robust while under pressure to keep running business as usual. 

Already know how to build an application inspired by the principles of the [12 Factor App](https://12factor.net/) and the [Ports and Adapters](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) pattern, you just have to replace your existing workflow with that new app - you know it'll be a faster, more robust, more extensible, automated, tested data pipeline. But you need to get in the mindset and familiarize yourself with how to work in this context.

## Getting Started

If you're coming from a different tech stack, you've maybe never fought with Python environments and versions. My favorite way to deal with this is to use [Poetry](https://python-poetry.org/docs/). Once you have it installed, you can initialize the Poetry environment. From here on out, every python related step we do will be prefixed with `poetry run` or from within a poetry shell. 

### Initialize the Environment:
```bash
poetry init
```
making sure to follow the instructions. If you skip the dependencies in this step, you'll do it after exiting the setup wizard.

### Adding Dependencies: pandas and jupyter 
```bash
poetry add pandas jupyter
```

With the dependencies installed, let's talk a little bit about Jupyter Notebooks and dive in:

| [Jupyter Notebooks >](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/jupyter-notebook.md)
