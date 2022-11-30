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

