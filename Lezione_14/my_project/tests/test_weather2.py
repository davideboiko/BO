from my_project.weather import check_weather
# failed
def test_check_weather():
    assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree \
        must be considered as average temperature'