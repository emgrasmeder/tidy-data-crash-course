Imagine this: You're a pretty decent software dev, but for some reason you have to start working with data for the first time. Most likely, spreadsheets worked fine for your team/org while you proved the business hypothesis, and now you need to build something more robust while under pressure to keep running business as usual. 


You're going to want to build an application inspired by the principles of the [12 Factor App](https://12factor.net/) and the [Ports and Adapters](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) pattern. The goal is to shut down your existing workflow piece by piece, replacing it with your faster, more robust, automated, tested data pipeline. 

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
and from there you can click on `New` > `Python 3 (ipykernal)`, this will open a new tab with an IPython interactive REPL.
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/1446d249-3f00-4305-be8c-fa740bf24dd7)

If you're new to Notebooks like this, here's my advice: Think of your Jupyter Notebook as a scratch pad. Pretend the file is saved to your `/tmp` folder and will get deleted in a few days. **Any code worth keeping that you've written in a Notebook you should cut and paste into your IDE, give it a function name, write some tests for it, and commit it to version control.** Next time, __import__ that lovely function from your library into your Notebook if you need it in the future.

Code in Notebooks depends on hidden state, it's rarely tested, it's not going to be well documented, in short **Notebook Code Rots Quickly**. 

But we're going to play with 🔥 anyway. For now, just watch out that execution order is important in Notebooks like this.
https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/e27a6cfb-f5c1-4fdd-8f0d-08358f2058f0



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

