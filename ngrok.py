from pyngrok import ngrok
link = ngrok.connect(3030,"http")
print(link)