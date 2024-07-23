import csv
import requests
from bs4 import BeautifulSoup


def get_all_lists(username):
    url = f"https://github.com/{username}?tab=stars"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"Other error occurred: {err}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")

    lists = []
    tags = soup.find_all('h3', class_='f4 text-bold no-wrap mr-3')
    for tag in tags:
        lists.append(tag.text.strip())

    return lists


def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return [], None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    # Extracting list elements
    list_elements = soup.select(
        ".col-12.d-block.width-full.py-4.border-bottom.color-border-muted"
    )
    for element in list_elements:
        item = {}

        # Extracting name
        name_element = element.select_one("h3 a")
        item["name"] = name_element.text.strip() if name_element else None
        item["name_link"] = name_element["href"] if name_element else None

        # Extracting description
        description_element = element.select_one("p[itemprop='description']")
        item["description"] = (
            description_element.text.strip() if description_element else None
        )

        # Extracting language
        language_element = element.select_one("span[itemprop='programmingLanguage']")
        item["language"] = language_element.text.strip() if language_element else None

        # Extracting stargazers
        stargazers_element = element.select_one("a[href$='/stargazers']")
        item["stargazers"] = (
            stargazers_element.text.strip() if stargazers_element else None
        )

        # Extracting forks
        forks_element = element.select_one("a[href$='/forks']")
        item["forks"] = forks_element.text.strip() if forks_element else None

        # Extracting updated
        updated_element = element.select_one("relative-time")
        item["updated"] = updated_element["datetime"] if updated_element else None

        data.append(item)

    # Extracting next page url
    next_page_element = soup.select_one(".pagination a[rel='next']")
    next_page_url = next_page_element["href"] if next_page_element else None

    return data, next_page_url


def crawl_data(start_url):
    all_data = []
    base_url = "https://github.com"
    url = start_url
    while url:
        data, next_page_url = get_data(url)
        all_data.extend(data)
        if next_page_url:
            url = (
                base_url + next_page_url
            )
        else:
            url = None
    return all_data


def save_to_csv(data, list_name):
    with open(f"github_stars_{list_name}.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "name_link",
                "description",
                "language",
                "stargazers",
                "forks",
                "updated",
            ],
        )
        writer.writeheader()
        writer.writerows(data)


def main(username):
    # get all lists
    lists = get_all_lists(username)

    for list_name in lists:
        start_url = f"https://github.com/stars/{username}/lists/{list_name}?page=1"
        all_data = crawl_data(start_url)
        # write to csv file
        save_to_csv(all_data, list_name)


if __name__ == "__main__":
    username = "username"
    main(username)
