from bs4 import BeautifulSoup

weather_html = """<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>

</body>
</html>"""

soup = BeautifulSoup(weather_html, 'html.parser')

tds = soup.find_all("td")

# for i in range(-1, 12, 3):
    # print(f"{tds[i+1].text}: {tds[i+2].text}, {tds[i+3].text}")
    

days = tds[0::3]
temps = [int(temp.text.strip('°C')) for temp in tds[1::3]]

conditions = tds[2::3]

max_temp = max(temps)
condition = conditions[temps.index(max_temp)].text

print(f"The highest temp is {max_temp}°C, and it is {condition}")

avg_temp = sum(temps)/len(temps)
print(f"Average temp is {avg_temp}")
