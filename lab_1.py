import requests


if __name__ == "__main__":
	r = requests.get("https://raw.githubusercontent.com/kandrosc/CMPUT_404_lab_1/master/lab_1.py")
	print("Returned a status of "+str(r.status_code))
	print(r.text)
