import requests
from send_email import send_email
api_key = "98e9182496d84e178a13259aa9035e4a"
# url = "https://finance.yahoo.com/?guccounter=1"
url = "https://newsapi.org/v2/everything?q=tesla&\
        from=2024-12-27&sortBy=publishedAt\
        &apiKey=98e9182496d84e178a13259aa9035e4a"
# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""


# Access the article titles and description
for articles in content["articles"]:

    # title = articles["title"]
    # description = articles["description"]

#     print(description)
#     if title and description is not None:
#         body = f"""\
# Subject :  News Email from the API
#
# {title} + "\n"
# Description of news : {description} + 2 * "\n"
# """


    if articles["title"] and articles["description"] is not None:

        body = body + articles["title"] + "\n" + articles["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)


# print(type(content))



