# Google Dorking Automation Tool

This is a Python tool that automates Google Dorking searches for a specified target domain. It reads a list of dorking rules from a `rules.txt` file, substitutes the domain in each rule with a user-specified target, and then opens each resulting Google search query in the system's default web browser.

## Features
- Automates Google Dorking searches to discover potentially sensitive information on a target domain.
- Supports multiple dorking rules, specified in `rules.txt`, with dynamic domain replacement.
- Opens search results automatically in your default web browser.

## Requirements
- **Python 3.7+**
- Internet access to perform Google searches.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/google-dorking-automation-tool.git
   cd google-dorking-automation-tool
   ```

2. Ensure `rules.txt` is in the same directory as the Python script.

## Usage
1. Add your dorking rules to `rules.txt`. Example dorking rules might include:
   ```
   site:domain.com filetype:pdf
   site:domain.com inurl:login
   site:domain.com intitle:"index of"
   ```

2. Run the script:
   ```bash
   python google_dorking_tool.py
   ```

3. When prompted, enter the target domain:
   ```
   Enter the target domain: example.com
   ```

4. The tool will automatically replace `domain.com` in each rule with `example.com` and open the search results in your default browser.

## Example `rules.txt`

The following are some sample rules to include in your `rules.txt` file:

```plaintext
# Find PDF files on the target domain
site:domain.com filetype:pdf

# Find Excel files on the target domain
site:domain.com filetype:xls OR filetype:xlsx

# Find admin portals
site:domain.com inurl:admin OR intitle:"admin"
```

## Code Overview

The main script consists of:
- **`load_dorks()`**: Reads dorking rules from `rules.txt`.
- **`create_dork_urls()`**: Replaces `domain.com` with the target domain and formats each rule as a Google search URL.
- **`open_dork_urls()`**: Opens each URL in the default browser.
- **`main()`**: Orchestrates the dorking process, from user input to opening URLs.

## Important Notes

- This tool is intended for ethical use only. Ensure you have permission to test against any target domain.
- Avoid using this tool to overload or disrupt Google’s services, as automated search queries can be rate-limited or flagged as abuse.
