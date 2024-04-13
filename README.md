# Project: project-productie-proces
- Name students: Carlo Dieltjens - Raf Mesotten - Yannick Pottiez
- GitHUB repository: https://github.com/craftyraf/project-productie-proces
- Project date: April 2024

### Set up your virtual environment
- Import 'environment.yaml' (in the same folder as 'README.md'), e.g. with Anaconda Navigator -> Environments -> Import
- Start -> Anaconda Powershell Prompt -> typ: "conda activate environment" (in case 'environment' is the name of the environment you just imported)
- Next, still in Anaconda Powershell Prompt, typ: "jupyter notebook", in order to open jupyter notebook.

### Run the notebooks to test the project
- You can find the notebooks in the subfolder 'notebooks' of the project folder.
- The notebooks use scripts from the folder 'scripts'.

### The scripts that are used by the notebook:
- fuel_mappings.py is a script with a function to map a lot of fuel type categories to a few fuel type categories
- make_a_chart.py is a script with functions that generate and/or plot graphs
- read_files.py is a script with a function that reads json files in a folder and concatenates them to a dataframe
- segment_calculations.py is a script with functions that creates, prints, calculates and saves segments based on production thresholds
- simulate.py is a script with a function that simulates the production processes for three production segments

### Problems with running the notebook? To get an idea of what we did, you can take a look at:
- An HTML file of the notebooks in the folder 'notebooks'
- Output files in the folder 'data\output'
- The scripts in the folder 'scripts'. We provided each function with a clear docstring.
- In case something isn't clear: contact us via email.

We are happy to receive your feedback!

Carlo, Raf and Yannick
