import webbrowser

def load_dorks(filename):
    try:
        with open(filename, 'r') as file:
            dorks = file.read().splitlines()
        return dorks
    except FileNotFoundError:
        print("The file 'rules.txt' was not found.")
        return []

def create_dork_urls(dorks, target_domain):
    urls = []
    for dork in dorks:
        # Replace 'domain.com' placeholder with the target domain
        modified_dork = dork.replace('domain.com', target_domain)
        # Create the Google search URL
        search_url = f"https://www.google.com/search?q={modified_dork}"
        urls.append(search_url)
    return urls

def open_dork_urls(urls):
    for url in urls:
        # Open each URL in the default browser
        webbrowser.open(url)

def main():
    target_domain = input("Enter the target domain: ")
    dorks = load_dorks('rules.txt')
    
    if dorks:
        urls = create_dork_urls(dorks, target_domain)
        print(f"Opening {len(urls)} dorking URLs for '{target_domain}'...")
        open_dork_urls(urls)
    else:
        print("No dorks loaded.")

if __name__ == "__main__":
    main()
