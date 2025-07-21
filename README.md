## Environment Setup
This repository consists of collection of Jupyter notebooks and Python files that will walk you through different applications of data/AI skills in security

The authors have tested this in the following environments
- VS Code 1.98.2 (IDE) on a MacOS 15.3.2 (Platform)
- VS Code 1.98.2 (IDE) on Windows 11 (Platform)

### Instructions
#### MacOS
1. Install uv (uv manages python versions, packages and dependencies)
- Follow your preferred method of installation [here](https://docs.astral.sh/uv/getting-started/installation/). We recommend Homebrew installs on Mac, ensure Homebrew is up-to-date by running `brew update`
- Run `uv python list` and note this output. This will be used later. 
- Add the following to your login shell settings (Ex: ~/.bash_profile on Mac)
```
eval "$(uv generate-shell-completion bash)"
export PATH="$PATH:<your output from step 1b>" (It should look something like: export PATH="$PATH:$HOME/path/to/uv/python/cpython-3.10.16-macos-aarch64-none/bin/")
export UV_PYTHON_PREFERENCE="only-managed"
```

2. Git clone this repository by running:  `git clone git@github.com:AI-and-Security/ai_for_sec_workshop.git` or `git clone https://github.com/AI-and-Security/ai_for_sec_workshop.git`

3. Inside the repository, execute this command `uv run test.py` to test your execution environment. The output is self-explanatory
 
4. In your favorite IDE, navigate to repository/notebooks and click on test.ipynb
- Select your environment for the notebook (This should be the `.venv` folder that is created in repository directory). Refer to your IDE docs/favorite AI assistant to understand how to provide an existing environment for jupyter notebooks. 
- VS Code Example: VS Code will prompt you to select a kernel and provide choices. By default, it should look in the current directory and present .venv as an option
- Execute the first cell to test the environment for notebook execution. The output is self-explanatory

5. All necessary datasets are in the data folder

6. Edit `notebooks/.env.example` file
- If you haven't created an OPENAI_API_KEY before, create one [here](https://platform.openai.com/api-keys). This is different from a ChatGPT account. Attach $5 to the API key
- Add your OPENAI_API_KEY or feel free to modify the code to use any other LLM provider
- Rename `.env.example` to `.env`

7. Edit `ti/.env.example` file
- If you haven't created an OPENAI_API_KEY before, create one [here](https://platform.openai.com/api-keys). This is different from a ChatGPT account. Attach $5 to the API key
- Create an API Key (it is free) with [Serper](https://serper.dev/signup?utm_term=google%20search%20api&gad_source=1&gclid=Cj0KCQjwhr6_BhD4ARIsAH1YdjDsTyDMEH94jjo6XyibEuHw_Nn-ZdqAxbPoTnzzS9Zxz57fOOvqWgMaAn1DEALw_wcB)
- Add your OPENAI_API_KEY or feel free to modify the code to use any other LLM provider
- Rename `.env.example` to `.env`
- Replace "Topic/Your Name" with a something of your choice that is non-adversarial in `ti/src/ti/main.py`

### Windows Instructions
Coming Soon! 