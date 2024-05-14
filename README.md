**Weather App using Robo Speaker**  
This project is a simple Python application that fetches current weather data from the WeatherAPI.com API based on user input for a specific city. The weather information is then spoken out loud using text-to-speech capabilities (using the Windows Speech API) and displayed in the console.

**Features**        
Retrieves current weather data for a specified city from WeatherAPI.com.
Utilizes the Windows Speech API (SAPI) to speak out the weather information.
Displays weather information including temperature in Celsius and Fahrenheit, local time, and whether it's currently day or night.
Provides a user-friendly interface for entering the city name.
Handles errors gracefully, informing the user if weather data retrieval fails.
**How to Use**        
Clone the repository to your local machine.
Install the required dependencies (requests library).
Obtain an API key from WeatherAPI.com and replace 'YOUR_API_KEY' in the code with your actual API key.
Run the weather_app.py script.
Enter the name of the city when prompted.
The weather information will be spoken out loud and displayed in the console.        
**Dependencies**        
Python 3.x
requests library
Windows operating system (for using the Windows Speech API)        
**License**        
This project is licensed under the MIT License.
