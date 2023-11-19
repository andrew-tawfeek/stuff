import requests, time, datetime
from bs4 import BeautifulSoup

def gimme_soup(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to download page content."
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def seminar_details(url):
    soup = gimme_soup(url)
    title =  soup.find_all("h1")[1].text
    smaller_details = soup.find_all("div", class_="field-item even")
    print("Title: ")
    print(title)
    print("")
    if len(smaller_details) < 3:
        print("Event details incomplete. Providing available information.")
        print("")
        for item in smaller_details:
            print(item.text)
            print("")
    else:
        speaker = soup.find_all("div", class_="field-item even")[0].text
        print("Speaker: ")
        print(speaker)
        print("")
        date = soup.find_all("span", class_="date-display-single")[0].text
        print("Date: ")
        print(date)
        print("")
        location = soup.find_all("div", class_="field-item even")[2].text
        print("Location: ")
        print(location)
        print("")
        desc = soup.find_all("div", class_="tex2jax")[0].text
        print("Description: ")
        print(desc)
        print("")
        print("URL: " + str(url))
        print("")
        print("-----------------------------")
        print("")

def new_math():
    big_soup = gimme_soup('https://math.washington.edu/events')
    raw_talk_list = big_soup.find_all('h2')[2:12] #was 2:12
    URL_List = [''.join(list(str(x).split("a href=")[1].split(">",1)[0])[1:-1]) for x in raw_talk_list]
    for url in URL_List:
        seminar_details(url)
    while True:
        time.sleep(86400) #waits 24 hours (86400 seconds) to check for new events
        New_URL_List = [''.join(list(str(x).split("a href=")[1].split(">",1)[0])[1:-1]) for x in raw_talk_list]
        for url in New_URL_List:
            if url not in URL_List:
                seminar_details(url)
        print("Updated at " + str(datetime.datetime.now()))

new_math()
#obligatory: https://www.youtube.com/watch?v=UIKGV2cTgqA