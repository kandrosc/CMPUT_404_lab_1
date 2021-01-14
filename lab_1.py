import requests


if __name__ == "__main__":
	r = requests.get("http://google.com")
	print("Returned a status of "+str(r.status_code))
	print(r.text)
