# A Tidy Data Crash Course
So you're a pretty decent software dev, and you've been tasked with phasing out your organization's Spreadsheet based workflow. It could be financial data, it could be logistics, it could be patient health data. It's really common and totally OK to start out using spreadsheets! But most likely, those spreadsheets worked fine while getting things off the ground, and now you need to build something more robust while under pressure to keep running business as usual. 

You just have to replace your existing workflow with that new app - you know it'll be a faster, more robust, more extensible, automated, tested data pipeline. But you need to get in the mindset and familiarize yourself with how to work in this context. This little breeze through will introduce you to the tools and help you build a little but of muscle memory for how you'll ditch your spreadsheets and get started with a robust Python solution.

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
