# Jupyter Notebooks
A lot of data work really depends on inspecting your data visually. Sometimes something really important will surface because of a visualization, or simply by looking at the dataframes that hold the data. (I've given a couple talks about the importance of visualizing data, for example at [Lambda Conf](https://www.youtube.com/watch?v=TrOBMJOh7Vw)) So you'll either want to inspect the data in your IDE or in a [Jupyter Notebook](https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb):
We'll do the latter here.

```bash
poetry run jupyter notebook
```

After starting the server up, you should see something similar to the following in your browser:
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/25e2b8b0-96e8-4532-8b1e-5356cfccfc4d)

and from there you can click on `New` > `Python 3 (ipykernal)`, this will open a new tab with an IPython interactive REPL.
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/1446d249-3f00-4305-be8c-fa740bf24dd7)

# Disclaimer❗
If you're new to Notebooks like this, here's my advice: Think of your Jupyter Notebook as a scratch pad. Pretend the file is saved to your `/tmp` folder and will get deleted in a few days. 
**Any code worth keeping that you've written in a Notebook you should cut and paste into your IDE, give it a function name, write some tests for it, and commit it to version control.** Next time, __import__ that lovely function from your library into your Notebook if you need it in the future.

Code in Notebooks depends on hidden state, it's rarely tested, it's not going to be well documented. In short **Notebook Code Rots Quickly**. 

Jupyter is quite powerful and can be used for collaboration, I've even helped teams deploy Notebooks as production code, but I really think they belong in a narrow context in the development pipeline. As such, I'm keeping the code snippets here in the Markdown files instead of making the entire blog post a Notebook to share and letting you simply execute the code to see that it works. Take some time exploring, that's what this tool exists for. 

But we're going to play with 🔥 anyway. For now, just notice that execution order is important in Notebooks:
![image](https://github.com/emgrasmeder/tidy-data-crash-course/assets/8107614/c71c186b-665f-40fd-a5fb-a0c4a83570bb)

Now you're set up with Jupyter Notebooks and Poetry, let's dive into the Data Stuff. Click below to navigate to the Tidy Data page:

| [Tidy Data >](https://github.com/emgrasmeder/tidy-data-crash-course/blob/main/tidy-data.md)
