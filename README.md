Imagine this: You're a pretty decent software dev, but for some reason you have to start working with data for the first time. Most likely, spreadsheets worked fine for your team/org while you proved the business hypothesis, and now you need to build something more robust while under pressure to keep running business as usual. 


You're going to want to build an application inspired by the principles of [12 Factor App](https://12factor.net/) and the [Ports and Adapters](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) pattern. The goal is to shut down your existing workflow piece by piece, replacing it with your faster, more robust, automated, tested data pipeline. 

### Getting Started

You're going to need to make sure the app works on every environment the same, so we'll use [Poetry](https://python-poetry.org/docs/).
Once you have it installed, you can initialize the Poetry environment. From here on out, every python related step we do will be prefixed with `poetry run` or from within a poetry shell. 

#### Initialize the Environment:
```bash
poetry init
```
making sure to follow the instructions. For now, you can decline any prompts to add dependencies.

#### Adding Dependencies 
Add the dependencies `pandas` and `jupyter`:
```bash
poetry add pandas jupyter
```
#### Jupyter Notebooks
Open the interactive [Jupyter Notebook](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb) with the following command:

```bash
poetry run jupyter notebook
```
After starting the server up, you should see something similar to the following in your browser:
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/25e2b8b0-96e8-4532-8b1e-5356cfccfc4d)


target audience: software developer who hasn't done much with data

1. technologies
a. poetry
b. pandas
  - data frames
c. jupyter
  - executing frames
  - pitfalls
2. methodologies
- tidy data
  - melting, joining, for loops
  - stop using for loops
  - variables - observations

