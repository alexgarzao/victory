# beeweb
Web front test automation tool.

## requirements
- python 3.6 or greather
- pip
- virtualenv

## setup
    cd <my-projects>
    git clone https://github.com/alexgarzao/beeweb.git
    cd beeweb
    virtualenv -p <python-version> <myenv>
    source <myenv>/bin/activate
    pip install -r requirements.txt

Where `<my-projects>` must be replaced by project directory; `<python-version>` must be replaced by the python binary to be used; and `<myenv>` must be replaced by the folder that will keep the virtualenv environment. For example:

    cd projects
    git clone https://github.com/alexgarzao/beeweb.git
    cd beeweb
    virtualenv -p python3.7 .env
    source .env/bin/activate
    pip install -r requirements.txt

To run the google search sample, run the following command:

    make FEATURES_PATH=samples/google-search all
