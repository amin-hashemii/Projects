import pyshorteners


url = input('URL: ')
shorted = pyshorteners.Shortener().tinyurl.short(url)

print(shorted)