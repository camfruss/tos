import argparse
import dotenv
from getpass import getpass


parser = argparse.ArgumentParser()

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def update_env(key, val):
    dotenv.set_key(dotenv_file, key, val)


def main():
    parser.add_argument("action", help="Specifies action. Current options: 'config'")
    parser.add_argument("-u", "--username", type=str, dest="username", help="Your TDA username")
    parser.add_argument("-p", "--password", action="store_true", dest="password", help="Your TDA password")
    parser.add_argument("--user_id", type=str, help="TDA API ID")
    args = parser.parse_args()

    if args.action != "config":
        return

    if args.username:
        update_env("USERNAME", args.username)
    if args.password:
        password = getpass()
        update_env("PASSWORD", password)
    if args.user_id:
        update_env("USER_ID", args.user_id)
