import argparse
import dotenv


"""

"""


parser = argparse.ArgumentParser()

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def update_env(key, val):
    dotenv.set_key(dotenv_file, key, val)


def main():
    parser.add_argument("action", help="Specifies action. Current options: 'config', 'refresh_token', and 'new_token'")
    parser.add_argument("--consumer_key", type=str, help="TDA API Consumer Key")
    parser.add_argument("--account_id", type=str, help="TDA Account ID")
    parser.add_argument("-e", "--email", type=str, help="Your email")
    parser.add_argument("--redirect_uri", type=str, help="Your TDA App's Redirect URI")

    args = parser.parse_args()

    if args.action == "new-token":
        exec(open("access_token.py new").read())
    elif args.action == "refresh-token":
        exec(open("refresh_token.py refresh").read())
    elif args.action == "config":
        if args.account_id:
            update_env("CONSUMER_KEY", args.consumer_key)
        if args.account_id:
            update_env("USER_ID", args.account_id)
        if args.email:
            update_env("EMAIL", args.email)
        if args.redirect_uri:
            update_env("REDIRECT_URI", args.redirect_uri)
    else:
        raise ValueError("Invalid tos action")


if __name__ == "__main__":
    main()