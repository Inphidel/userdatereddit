A Python script to check the creation dates of Reddit accounts using the Reddit API via PRAW. Useful for verifying account age to help distinguish real users from bots or throwaways.

# Features
- **Interactive Mode**: Enter usernames one-by-one to check their creation dates.
- **File Mode**: Read usernames from a text file (one per line) using the `-f` flag.
- Handles suspended or deleted accounts gracefully.
- Trims whitespace from inputs and skips empty lines.

# Requirements
- **Python**: 3.12 or higher (for `datetime.UTC`). For older versions, see [Notes for older Python versions](#notes-for-older-python-versions).
- **PRAW**: Python Reddit API Wrapper (`pip install praw`).
- A Reddit account and API credentials (see [Setup](#setup)).

# Setup
1. **Install Python**: Ensure Python 3.12+ is installed. Check with `python --version`.
2. **Install PRAW**: Run `pip install praw` in your terminal or virtual environment.
3. **Get Reddit API Credentials**:
   - Log into your Reddit account.
   - Go to `https://www.reddit.com/prefs/apps`.
   - Click "create app" or "create another app".
   - Fill out:
     - **Name**: e.g., "DateChecker"
     - **App type**: Select "script"
     - **Redirect URI**: `http://localhost:8080`
   - Click "create app".
   - Note your:
     - `client_id`: The 14-character string below the app name.
     - `client_secret`: The longer string labeled "secret." 
4. **Configure the Script**:
   - Open `userdatereddit.py` in a text editor.
   - Replace the placeholders in the `reddit = praw.Reddit(...)` section:
     - `YOUR_CLIENT_ID_HERE` with your `client_id`.
     - `YOUR_CLIENT_SECRET_HERE` with your `client_secret`.
     - `YOUR_REDDIT_USERNAME` with your Reddit username (e.g., `/u/User1`).

# Usage
## Interactive Mode
Run the script without arguments to enter usernames manually:
```bash
python userdatereddit.py
```

- Prompt: Enter a Reddit username to check (or press Enter to finish):    
- Enter a username (e.g., User1) and press Enter.    
- Press Enter with no input to quit:    
    - First empty input: No user input provided. Quitting.        
    - After entries: No more input. Quitting.        

## File Mode

Run with the -f flag to read usernames from a file:
```bash
python userdatereddit.py -f users.txt
```

- users.txt should contain one username per line (e.g.):    
```text
user1
user2
user3
```

- Whitespace is trimmed, and empty lines are skipped.    
- If the file is missing or empty, it will quit with an error message.    

## Example Output

```text
The account u/user1 was created on: 2014-05-05 13:35:55+00:00 UTC
The account u/user2 exists but has no accessible creation date. It may be suspended or deleted.
The account u/user3 was created on: 2005-06-06 00:00:00+00:00 UTC
API error for u/user123: 404 Not Found or similar
```

# Notes

- Suspended Accounts: For accounts like /u/user123, the creation date may not be available if suspended.    
- Rate Limits: Reddit’s API allows ~60 requests/minute. For large files, consider adding time.sleep(1) in the for loop.    
- Error Handling: The script catches API errors (e.g., 404 for non-existent users) and unexpected issues.    

## Notes for Older Python Versions

If using Python 3.11 or older (no datetime.UTC):
1. Install pytz: pip install pytz.    
2. Modify the imports and datetime line:    

python
```python
import pytz
# Replace: from datetime import datetime, UTC
from datetime import datetime
# Replace: creation_date = datetime.fromtimestamp(creation_timestamp, UTC)
creation_date = datetime.fromtimestamp(creation_timestamp, pytz.UTC)
```

# Contributing
Feel free to fork, submit issues, or send pull requests on GitHub!

# License
MIT License (or your preferred license—edit as needed).
