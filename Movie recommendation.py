from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


def fun(choice):
    if choice == 1:
        url = "https://www.imdb.com/search/title/?genres=action&sort=num_votes,desc&explore=title_type,genres"
    elif choice == 2:
        url = "https://www.imdb.com/search/title/?genres=sci-fi&sort=num_votes,desc&explore=title_type,genres"
    elif choice == 3:
        url = "https://www.imdb.com/search/title/?genres=drama&sort=num_votes,desc&explore=title_type,genres"
    elif choice == 4:
        url = "https://www.imdb.com/search/title/?genres=Thriller&explore=title_type%2Cgenres&ref_=ft_popular_11"
    elif choice == 5:
        url = "https://www.imdb.com/search/title/?genres=comedy&sort=num_votes,desc&explore=title_type,genres"
    elif choice == 6:
        url = "https://www.imdb.com/search/title/?genres=crime&sort=num_votes,desc&explore=title_type,genres"
    q = requests.get(url, headers=headers)
    soup = BeautifulSoup(q.text, "html.parser")
    s = soup.find_all("div", class_="lister-item mode-advanced")
    l = []
    i = 1
    for container in s:
        name = container.h3.a.text
        year = container.h3.find("span", class_="lister-item-year").text
        runtime = (
            container.p.find("span", class_="runtime").text
            if container.p.find("span", class_="runtime")
            else "-"
        )
        imdb = float(container.strong.text)
        cer = container.p.find("span", class_="certificate").text

        data = {
            "place": i,
            "movie_title": name,
            "rating": imdb,
            "year": year,
            "runtime": runtime,
            "age_rating": cer,
        }
        i += 1
        l.append(data)
        if i == 11:
            break
    return l


a = "1"
print("MOVIES & SERIES RECOMMENDATIONS BASED ON IMDB")
while a == "1":
    print("\n1)Action \n2)Sci-Fi \n3)Drama \n4)Thriller \n5)Comedy \n6)Crime\n")
    user = int(input("Enter your choice:"))
    top_10 = list()
    top_10 = fun(user)
    count = 0
    for movie in top_10:
        print(
            movie["place"],
            "-",
            movie["movie_title"],
            movie["year"],
            "|",
            movie["rating"],
            "|",
            " Runtime:",
            movie["runtime"],
            "|",
            "Age Rating:",
            movie["age_rating"],
            "\n",
        )
        if count == 11:
            break
        count += 1
    a = input("To continue press 1 or press enter to exit: ")
    if a != "1":
        exit
