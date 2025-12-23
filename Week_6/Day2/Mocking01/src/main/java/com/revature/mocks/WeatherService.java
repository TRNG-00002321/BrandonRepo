package com.revature.mocks;

public class WeatherService {

    private WeatherApiClient weatherApiClient;

    //injecting a dependency
    public WeatherService(WeatherApiClient weatherApiClient, int temp) {
        this.weatherApiClient = weatherApiClient;
    }

    public String getWeatherMessager(String city){
        double temp= weatherApiClient.fetchTemperature(city);


        if(temp>30){
            return "It's Hot in " + city;
        } else if (temp>15){
            return "It's warm in " + city;
        }
        return "It's cold in " + city;


    }
}
