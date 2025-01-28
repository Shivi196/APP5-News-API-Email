import requests

api_key = "98e9182496d84e178a13259aa9035e4a"
# url = "https://finance.yahoo.com/?guccounter=1"
url = "https://newsapi.org/v2/everything?q=tesla&\
        from=2024-12-27&sortBy=publishedAt\
        &apiKey=98e9182496d84e178a13259aa9035e4a"
# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for articles in content["articles"]:
    print(articles["title"])
    print(articles["description"])
# print(type(content))
