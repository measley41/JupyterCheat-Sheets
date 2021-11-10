# JupyterCheat-Sheets

This is just a collection of notes and examples in Jupyter notebooks that I want to share between work and home.
It also gives me something to put in my first github repository to learn the workflow.

Not much to see here, but I'm happy to share.
I've tried to give credit and cite the original sources where I could.

## Note

I'm experimenting with [Jupytext](https://jupytext.readthedocs.io/en/latest/paired-notebooks.html) formatting.  
In order to use this, open Jupyter Notebook in a conda environment with jupytext installed:  
`conda install -c conda-forge jupytext`  

This is a utility that pairs a Jupyter notebook with a .py version that doesn't include all of the metadata and cell outputs that cause issues with git.  The .py version can be tracked with git and looks like a normal diff. If you open the .py version in Jupyter, it will recreate the notebook automatically.  

