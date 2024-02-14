from Betclic_tennis_scraper import *
if __name__ == '__main__':
    
    match_links = get_match_links()

    if match_links.get('Error'):
        print("we have a problem of too many requests")
    else:
        links = match_links.get('links')

    all_text = []

    for url in links[:1]:
        driver = create_tennis_driver(url)
        if driver is None:
            continue
        else:
            info = retrieve_tennis_point_service(driver)
            try:
                result = re.search(r'Aces(.*?)0 selection', info, re.DOTALL)
                if result:
                    extracted_text = result.group(1).strip()
                all_text.append(extracted_text)
            except Exception:
                print("no Aces found")
    text = '|'.join(elm for elm in all_text)

    # Writing to a file
    with open("tennis_data.txt", "w") as file:
        file.write(text)
