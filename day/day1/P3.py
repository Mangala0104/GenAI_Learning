#pip,virtual environment,env file
# pip:pip installs packages.package manager 
# virtual environment: a 'venv' is as directory that contains
# 1.A copy of the python complier
# 2.its own 'pip'
# 4.its own site-packages directory 
# where the python installs third party libraries
# 4. activation scription that modify PATH

python--version #window

python -m venv .venv

#activate 
.venv\Scripts\activate.bat #win

#deactivate 
deactivate

#pip installation (install dependancies/libraries)
pip insatll package_name #syntax


pip install python-dotenv
