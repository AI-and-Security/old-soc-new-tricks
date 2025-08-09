This repository consists of a collection of Jupyter notebooks and Python files that will walk you through different applications of data/AI skills in security. We also provide confidence and increase data literacy by equipping security practitioners with the right data tools for their day-to-day job

Pre-Reqs: Computer with browser, at least 10GB of disk space, 8GB RAM if not running local models, exposure to terminal, IDEs, git and python. 

## Model Access
1. If you don't already have an OpenRouter account, create one at [OpenRouter](https://openrouter.ai/). 
2. Create an API key. You can use free tier models from OpenRouter (moonshotai/kimi-k2, google/gemini-2.0-flash-exp). We recommend, adding about $5 to your account if you want to use frontier models.
3. Create an account with [SerperAPI](https://serper.dev) and get an API key. This is always free. 

## 🔗 Google Colab Notebooks

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
| `Module1` | Old School is Cool! | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/ai_python.ipynb) |
| `Module2` | To GenAI or Not! | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/ml_genai.ipynb) |
| `Module3` | Upskilling the LLMs | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AI-and-Security/old-soc-new-tricks/blob/main/notebooks/eda_langchain.ipynb) |


## 💻 Local Environment Setup

Note: We expect you to have a basic understanding of your existing environment, tooling, path, terminal to debug issues. AI is your friend! 

The authors have tested this in the following environments
- VS Code >= 1.98.2 (IDE) on a MacOS 15.3.2 (Platform) with Python 3.11

### Instructions

1. Install uv (uv manages python versions, packages and dependencies)
- Follow your preferred method of installation [here](https://docs.astral.sh/uv/getting-started/installation/). We recommend Homebrew installs on Mac, ensure Homebrew is up-to-date by running `brew update`. 
2. Follow the complete guide such that you have `uv` in your $PATH and install auto-bash completion if needed
3. If you don't have Python 3.11, install one using `uv python install 3.11`
4. Run `uv python list` to verify that the python version is installed. 

2. Git clone this repository by running:  `git clone git@github.com:AI-and-Security/old-soc-new-tricks.git` or `git clone https://github.com/AI-and-Security/old-soc-new-tricks.git`

3. Inside the repository, execute this command `uv run test.py` to test your execution environment. The output is self-explanatory. This should automatically create a virtual environment (`.venv`) and install dependencies in the repo folder. 
 
4. In your favorite IDE, navigate to repository/notebooks and click on test.ipynb. Install Jupyter and Python extensions if not already installed to run jupyter notebook. 
- Select your environment for the notebook (This should be the `.venv` folder that is created in repository directory). Refer to your IDE docs/favorite AI assistant to understand how to provide an existing environment for jupyter notebooks. 
- VS Code Example: VS Code will prompt you to select a kernel and provide choices. By default, it should look in the current directory and present .venv as an option
- Execute the first cell to test the environment for notebook execution. The output is self-explanatory

5. All necessary datasets are in the data folder

6. Rename`notebooks/.env.example` to `notebooks/.env` and populate it with the model provider keys

7. Edit `ti/.env.example` file
- Rename `.env.example` to `.env`
- Replace "Topic/Your Name" with a something of your choice that is non-adversarial in `ti/src/ti/main.py`
- From `ti/` directory, run `uvx crewai run`
