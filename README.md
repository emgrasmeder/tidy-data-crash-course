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
### [Jupyter Notebook](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb):
A lot of data work really depends on inspecting your data visually. Sometimes something really important will surface because of a visualization, or simply by looking at the dataframes that hold the data. (I've given a couple talks about the importance of visualizing data, for example at [Lambda Conf](https://www.youtube.com/watch?v=TrOBMJOh7Vw)) So you'll either want to inspect the data in your IDE or in a Jupyter Notebook. We'll do the latter here:
```bash
poetry run jupyter notebook
```

After starting the server up, you should see something similar to the following in your browser:
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/25e2b8b0-96e8-4532-8b1e-5356cfccfc4d)
and from there you can click on `New` > `Python 3 (ipykernal)`, this will open a new tab with an IPython interactive REPL.
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/1446d249-3f00-4305-be8c-fa740bf24dd7)

If you're new to Notebooks like this, here's my advice: Think of your Jupyter Notebook as a scratch pad. Pretend the file is saved to your `/tmp` folder and will get deleted in a few days. **Any code worth keeping that you've written in a Notebook you should cut and paste into your IDE, give it a function name, write some tests for it, and commit it to version control.** Next time, __import__ that lovely function from your library into your Notebook if you need it in the future.

Code in Notebooks depends on hidden state, it's rarely tested, it's not going to be well documented, in short **Notebook Code Rots Quickly**. 

But we're going to play with 🔥 anyway. For now, just notice that execution order is important in Notebooks:
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/c71c186b-665f-40fd-a5fb-a0c4a83570bb)

Now you're set up with Jupyter Notebooks and Poetry, let's dive into the Data Stuff. Click below to navigate to the Tidy Data page:

| [Tidy Data >](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/tidy-data.md)


b. pandas
  - data frames
2. methodologies
- tidy data
  - melting, joining, for loops
  - stop using for loops
  - variables - observations

