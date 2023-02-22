def main():

  import requests
  api_key = "7e79c819ced71ead2427b75ccb8ef770"
  user_input = input("Enter city:")

  weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
  )

  if weather_data.json()['cod'] == '404':
    print("No City Found")
  else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
  print(f"The Weather in {user_input} is: {weather}")
  print(f"The Temperature in {user_input} is: {temp}°F")

  restart = input("Do you want to look up a different city? Yes/No : ").lower()
  if restart == "yes":
    main()
  else:
    message = ("Thanks for using my program!")
    print(message)


main()