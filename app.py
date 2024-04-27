from flask import Flask , request , render_template
import requests
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/display_weatherInfo', methods = ['POST'])
def displayWeatherInfo():
    location = request.form.get('location')
    units = request.form.get('units')
    apiKey = request.form.get('apiKey')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units={units}&appid={apiKey}"
    response = requests.get(url)
    jsondata = response.json()

    weatherType = jsondata['weather'][0]['main']
    weatherDescription = jsondata['weather'][0]['description']
    temp = jsondata['main']['temp']
    humidity = jsondata['main']['humidity']

    return f"Weather : {weatherType},Desscription : {weatherDescription}, Temperature : {temp}, Humidity : {humidity} "


if __name__ == '__main__':
    app.run(host='0.0.0.0')