Flask Setup

Installation
* Upgrade the package manager pip.

pip install --upgrade pip

* Create virtual environment
python3 -m venv ~/.virtualenvs/flask_setup_env

*Activate virtual environment
source ~/.virtualenvs/flask_setup/bin/activate

*Install requirements in the environment.
pip install -r requirements.txt

*Install pre-commit
pre-commit install

*To create an alias, add this to your ~/.bash_aliases
alias flask_setup="cd ~/projects/flask_setup; source ~/.virtualenvs/flask_setup/bin/activate"

*To runserver
python manage.py runserver

*Docker commands
docker build -t flask_setup .
docker run -p5005:80 -d -v /home/abhishek/projects/flask_setup:/flask_setup flask_setup


