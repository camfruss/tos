import dotenv
from getpass import getpass
from globals import POST_ACCESS_TOKEN_URL
import os
import requests
from selenium import webdriver
import sys
from time import time
from urllib.parse import quote, unquote, urlparse


"""
implement steps on https://developer.tdameritrade.com/content/simple-auth-local-apps

TODO: 
- have user re-enter password to make sure is correct
- error handling if anything goes wrong during request
"""


# Retrieve needed .env values
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

redirect_uri = os.environ.get("REDIRECT_URI")
redirect_uri_encoded = quote(redirect_uri, safe="")

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_key_encoded = quote(consumer_key, safe="")

refresh_token = os.environ.get("REFRESH_TOKEN")


def tda_code():
	"""
	"""
	AUTH_URL_QUERY =  \
		("https://auth.tdameritrade.com/auth?response_type=code"
		f"&redirect_uri={redirect_uri_encoded}"
		f"&client_id={consumer_key_encoded}%40AMER.OAUTHAP")

	
	username = input("Your TDA username > ")
	password = getpass("Your TDA password > ")

	options = webdriver.ChromeOptions()
	options.add_argument("--disable-extensions")
	options.add_argument("--window-size=1920,1080")
	options.add_argument("--headless")
	driver = webdriver.Chrome(options=options)

	driver.get(AUTH_URL_QUERY)

	# Log-in to TDAmeritrade online 
	driver.implicitly_wait(10)
	driver.find_element("name", "su_username").send_keys(username)
	driver.find_element("name", "su_password").send_keys(password)
	driver.find_element("name", "authorize").click()

	# Send 2FA message
	driver.implicitly_wait(10)
	driver.find_element("id", "accept").click()

	# Enter 2FA message from device
	sms_code = input("TDA Security Code > ")
	driver.implicitly_wait(10)
	driver.find_element("name", "su_smscode").send_keys(sms_code)
	remember_device_xpath = "/html/body/form/main/div[5]/span/label"
	remember_device_element = driver.find_element("xpath", remember_device_xpath)
	driver.execute_script("arguments[0].click();", remember_device_element)
	driver.find_element("id", "accept").click()

	# Grant API access to account
	driver.implicitly_wait(10)
	driver.find_element("id", "accept").click()

	# Parse URL for access code, decode
	response_url = driver.current_url
	parsed_url = urlparse(response_url)
	code = parsed_url.query.split("=")[1]
	decoded_code = unquote(code)
	
	# Close Chrome session
	driver.quit()

	return decoded_code


def main():
	"""
	"""
	refresh = True
	if sys.argv[0] == "refresh":
		pass
	elif sys.argv[0] == "new":
		refresh = False
	else:
		raise ValueError("Invalid token request parameter. 'new-token' or 'refresh-token'")

	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	body = {
		"grant_type": "refresh_token",
		"refresh_token": refresh_token,
		"client_id": consumer_key + "@AMER.OAUTHAP",
	} if refresh else {
		"grant_type": "authorization_code",
		"access_type": "offline",
		"code": tda_code(),
		"client_id": consumer_key + "@AMER.OAUTHAP",
		"redirect_uri": redirect_uri
	}

	# Update .env file
	try:
		response = requests.post(POST_ACCESS_TOKEN_URL, headers=headers, data=body)
		data = response.json()
		if response.status_code > 299:
			raise SystemExit()
		dotenv.set_key(dotenv_file, "ACCESS_TOKEN", data.get("access_token"))
		dotenv.set_key(dotenv_file, "REFRESH_TOKEN", data.get("refresh_token"))
		dotenv.set_key(dotenv_file, "ACCESS_TOKEN_TIMESTAMP", int(time()))
		if not refresh:
			dotenv.set_key(dotenv_file, "REFRESH_TOKEN_TIMESTAMP", int(time()))
	except requests.exceptions.RequestException as err:
		raise SystemExit(err)


if __name__ == "__main__":
	main()