# Automating Covered Calls on TDA's ToS


/src has all the code responsible for making trades

/tools manages tokens

Update package from setup.py file
`pip install -e .`

need to manually log in every 90 days

username and password are not part of `.env`, API keys are
Decision because 
malicious code could find secrets if in VC or on system, need account credentials to be of use (based on my understanding)
small price to pay for security 

access_token expires in 30 minutes
refresh_token expires every 90 days

TODO: update install_requires in setup.py...do you need requirements if have that??


TODO: update so that chrome version is newer
There should probably be a dockerfile, but in the meantime, running the following commands will suffice.
```
sudo yum update
sudo yum install python3 -y
sudo yum -y install libX11

sudo curl https://intoli.com/install-google-chrome.sh | bash
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version

cd /tmp/
sudo wget https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
chromedriver --version
```
Note: When installing `chromedriver`, make sure the version is compatible with the version of `google-chrome`. 
Otherwise, it won't work. You can check `https://chromedriver.chromium.org/downloads` to see the most up-to-date 
versions.


TODO: make available on pypi

`token.py` breaks all imports, so re-name