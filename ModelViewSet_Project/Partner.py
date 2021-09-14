
import requests

# url = "http://127.0.0.1:5555/api/employees/"

# response = requests.get("http://127.0.0.1:5555/api/employees/")

payload = {
    "eno" : 40,
    "ename" : "Kiran",
    "salary" : 45000
}

# response = requests.post("http://127.0.0.1:5555/api/employees/",data=payload)

id = input("enter any id :")
# response = requests.get("http://127.0.0.1:5555/api/employees/"+id+'/')
# response = requests.delete("http://127.0.0.1:5555/api/employees/"+id+'/')
response = requests.put("http://127.0.0.1:5555/api/employees/"+id+'/', data=payload)


if response.status_code==200:
    try:
        dict_data = response.json()
    except:
        print('Your response is not JSON')
    else:
        print(dict_data)

elif response.status_code==404:
    print(response.status_code)
    print('Requested resource not available')

elif response.status_code==201:
    print(response.status_code)
    print('Data created successfully')

elif response.status_code==400:
    print(response.status_code)
    print('Data not created successfully')

elif response.status_code==204:
    print(response.status_code)
    print('Data deleted successfully')

else:
    print(response.status_code)
    print('Something wrong')