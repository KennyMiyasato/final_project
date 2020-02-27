# Restaurant Daily Sales Predictor
Using Daily sales and weather data to predict future daily sales.

## Background
A family owned peruvian restaurant in New Jersey wants help from a data scientist to predict their daily sales.

## Data Sources
1. Clover POS (point-of-sale) website CSV
- 01/01/2015 - 01/20/2020
- Daily sales (1,846 rows/days)
2. Darksky API
- 01/01/2015 - 01/20/2020
- Average Temperature & Precipitation (1,846 rows/days)

## EDA
Average day-of-week trend using 5 years of data

![Weekday_Trends](/figures/slides/Weekday_Trends.png)

Average monthly trend using 5 years of data

![Monthly_Trends](/figures/slides/Monthly_Trends.png)

Average holiday trend using 5 years of data

![Holiday_Trends](/figures/slides/Holiday_Trends.png)

Year-Over-Year Sales

![Yearly_Trends](/figures/slides/Yearly_Trends.png)

### Forecasting Model

Prophet

![Facebook_Prophet](/figures/slides/prophet_forecasting.png)

Prophet had the best RMSE to forecast daily sales. I tried to fit and ARIMA model and also fit Prophet with exogenous variables (feature engineering average temperature and using precipitation) but they were not as accurate to forecast the 1-day window. [*Forecasting tomorrow's sales based on all data including today's*]

Overall, the Prophet + Seasonality model had an RMSE of 449.20. Which would translate to +-$449.20 for any given day.

### Conclusion

Based on my domain knowledge and also speaking to the restaurant owner. We both agreed that it would be best to predict **weekly sales** instead of daily sales. Our assumption is that predicting daily sales seems to be a *random walk*.