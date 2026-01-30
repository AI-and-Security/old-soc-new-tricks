This repository consists of a collection of Jupyter notebooks and Python files that will walk you through different applications of data/AI skills in security. We also provide confidence and increase data literacy by equipping security practitioners with the right data tools for their day-to-day job

Pre-Reqs: Computer with browser, at least 10GB of disk space, 16GB RAM, exposure to terminal, IDEs, git and python. 

## API Credentials
1. If you don't already have an OpenRouter account, create one at [OpenRouter](https://openrouter.ai/). 
2. Create an API key. You can use free tier models from OpenRouter (moonshotai/kimi-k2, google/gemini-2.0-flash-exp). We recommend, adding about $5 - $10 to your account if you want to use frontier models.
3. Create an account with [SerperAPI](https://serper.dev) and get an API key. This is always free. 
4. Create an account with VirusTotal if you don't already have one. This is also a free API
6. Copy `notebooks/.env.example` to `notebooks/.env` and populate it with the keys you got from the above steps
7. Copy `ti/.env.example` to `ti/.env` and populate it with the keys you got from the above steps

## Lab Execution

1. Git clone this repository by running:  `git clone git@github.com:AI-and-Security/old-soc-new-tricks.git` or `git clone https://github.com/AI-and-Security/old-soc-new-tricks.git


We have two options to run the labs: 
1. **Recommended**: [Instructions](#docker-jupyterlab-setup)
2. **Create environment locally**: [Instructions](#instructions-to-set-up-environment-locally)



### Instructions to set up environment locally

Note: We expect you to have a basic understanding of your existing environment, tooling, paths and your terminal to debug issues. AI is your friend if you run into errors!

The authors have tested this in the following environments
- VS Code >= 1.98.2 (IDE) on a MacOS Sierra onwards (Platform) with Python 3.12


1. Install uv (uv manages python versions, packages and dependencies)
- Follow your preferred method of installation [here](https://docs.astral.sh/uv/getting-started/installation/). We recommend Homebrew installs on Mac, ensure Homebrew is up-to-date by running `brew update`. 
- Follow the complete guide such that you have `uv` in your $PATH and install auto-bash completion if needed
- If you don't have Python 3.12, install one using `uv python install 3.12`
- Run `uv python list` to verify that the python version is installed. 


2. Inside the repository, execute this command `uv run test.py` to test your execution environment. The output is self-explanatory. This should automatically create a virtual environment (`.venv`) and install dependencies in the repo folder. Alternativly, running `uv sync` will create a virtual environment and install dependencies in the repo folder. 
 
3. In your favorite IDE, navigate to repository/notebooks and click on test.ipynb. Install Jupyter and Python extensions if not already installed to run jupyter notebook. 
- Select your environment for the notebook (This should be the `.venv` folder that is created in repository directory). Refer to your IDE docs/favorite AI assistant to understand how to provide an existing environment for jupyter notebooks. 
- VS Code and its derivatives will prompt you to select a kernel and provide choices. By default, it should look in the current directory and present .venv as an option
- Execute the first cell to test the environment for notebook execution. The output is self-explanatory

4. All necessary datasets are in the data folder


5. Preparing agents
- Replace "Topic/Your Name" with a something of your choice that is non-adversarial in `ti/src/ti/main.py`
- From `ti/` directory, run `uvx crewai run`

### Docker + Jupyterlab Setup

This option standardizes execution across machines. It launches a Jupyter Lab server on your local machine that can run the labs


1. Build and run
Install Docker on your machine if you haven't already - [Docker](https://docs.docker.com/get-docker/)
```
cd <repo directory>
docker compose up --build
```

2. Open Jupyter Lab
Visit http://localhost:8888 in your browser.

Default token is `workshop`. You can override it by setting `JUPYTER_TOKEN` in your shell before running:
```
JUPYTER_TOKEN=my-token docker compose up --build
```

3. Running notebooks and TI
- Notebooks: open files in `notebooks/` and run cells.
- Threat Intel project: open `ti/src/ti/main.py` to set a topic, then run from a notebook cell or terminal:
```
python -m ti.
uvx crewai run from terminal
```


### ** DEPRECATED ** Google Colab Notebooks

1. **IMPORTANT**: Save a copy of the notebook to your Google Drive, do not make modifications or execute on the repository copy. Your Google drive should have at least 2 GB of space
2. In your copy of any of these notebooks, paste in your API keys in the `.env` file in this format
```
OPENROUTER_API_KEY=YOUR_KEY_HERE
SERPER_API_KEY=YOUR_KEY_HERE

# Optional and if you already have these keys
OPENAI_API_KEY=YOUR_KEY_HERE
ANTHROPIC_API_KEY=YOUR_KEY_HERE
```

3. Ignore any warnings during restart!

| Notebook | Description | Colab |
|----------|-------------|-------|
| `test` | Test notebook | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/test.ipynb) |
| `Exercise 1` | Foundations are important | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/asm_explorer.ipynb) |
| `Exercise 2` | Old School is Cool! | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/ai_python.ipynb) |
| `Exercise 3` | To GenAI or Not! | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/ml_genai.ipynb) |
| `Exercise 4` | Research: Push the envelope with LLMs | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/eda_langchain.ipynb) |
| `Exercise 5` | Signals for CoPilot | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/guided_response.ipynb) |
| `Exercise 6` | Basic Threat Intel Agent | [Code Directory](https://github.com/AI-and-Security/old-soc-new-tricks/tree/main/ti) |
| `Exercise 7` | Agentic Analyst | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/AI-and-Security/old-soc-new-tricks/blob/aiv/notebooks/agentic_workflows.ipynb) |

