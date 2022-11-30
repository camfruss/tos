import argparse
import dotenv


# TODO: fix to match .env file
parser = argparse.ArgumentParser()

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def update_env(key, val):
    dotenv.set_key(dotenv_file, key, val)


def main():
    parser.add_argument("action", help="Specifies action. Current options: 'config', 'refresh_token', and 'new_token'")
    parser.add_argument("--user_id", type=str, help="TDA API ID")
    parser.add_argument("-e", "--email", type=str, help="Your email")
    parser.add_argument("--redirect_uri", type=str, help="Your TDA App's Redirect URI")

    args = parser.parse_args()

    if args.action == "new_token":
        pass # generate new access token

    if args.action == "refresh_token":
        pass # refresh access token

    if args.action == "config":
        if args.user_id:
            update_env("USER_ID", args.user_id)
        if args.email:
            update_env("EMAIL", args.email)
        if args.redirect_uri:
            update_env("REDIRECT_URI", args.redirect_uri)
