import requests
from send_email import send_email
api_key = "98e9182496d84e178a13259aa9035e4a"
# url = "https://finance.yahoo.com/?guccounter=1"
topic="tesla"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-12-30&"
       "sortBy=publishedAt&"
       f"apiKey={api_key}&"
       "language=en")
# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)


# Access the article titles and description
body = ""
for articles in content["articles"][:20]:
  if articles["title"] and articles["description"] is not None:
     body = "Subject: Today's News" \
             + "\n"+ body + articles["title"] + "\n" \
             + articles["description"]  \
             + "\n" + articles["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)


# print(type(content))


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

