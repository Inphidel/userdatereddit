import praw
import argparse
from datetime import datetime, UTC

# Initialize PRAW with Reddit app credentials (replace with your own)
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID_HERE",  # Get this from reddit.com/prefs/apps
    client_secret="YOUR_CLIENT_SECRET_HERE",  # Get this from reddit.com/prefs/apps
    user_agent="DateChecker v1.0 by /u/YOUR_REDDIT_USERNAME"  # Replace with your Reddit username
)

def check_user(username):
    """Check creation date for a single Reddit user."""
    try:
        redditor = reddit.redditor(username)
        if hasattr(redditor, 'created_utc'):
            creation_timestamp = redditor.created_utc
            creation_date = datetime.fromtimestamp(creation_timestamp, UTC)
            print(f"The account u/{username} was created on: {creation_date} UTC")
        else:
            print(f"The account u/{username} exists but has no accessible creation date. It may be suspended or deleted.")
    except praw.exceptions.RedditAPIException as e:
        print(f"API error for u/{username}: {e}")
    except Exception as e:
        print(f"Unexpected error for u/{username}: {e}")

def main():
    # Set up argument parser for command-line options
    parser = argparse.ArgumentParser(description="Check Reddit account creation dates.")
    parser.add_argument("-f", "--file", type=str, help="Path to a file with usernames (one per line)")
    args = parser.parse_args()

    # If -f is provided, read usernames from the file
    if args.file:
        try:
            with open(args.file, 'r') as f:
                usernames = [line.strip() for line in f if line.strip()]  # Trim and skip empty lines
            if not usernames:
                print("No valid usernames found in the file. Quitting.")
                return
            for username in usernames:
                check_user(username)
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found. Quitting.")
        except Exception as e:
            print(f"Error reading file '{args.file}': {e}. Quitting.")
    else:
        # Interactive mode: prompt for usernames
        print("Enter a Reddit username to check (or press Enter to finish):")
        first = True
        while True:
            username = input("Username: ").strip()  # Trim input
            if not username:  # Empty input
                if first:
                    print("No user input provided. Quitting.")
                    break
                else:
                    print("No more input. Quitting.")
                    break
            check_user(username)
            first = False

if __name__ == "__main__":
    main()
