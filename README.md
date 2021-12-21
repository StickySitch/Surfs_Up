# Surfs_Up

## Overview & Purpose
In order to determine the ideal surf and ice cream shop location W.avy (Investor)
and I decided to analyze the temperature data of Oahu, Hawaii; Specifically June and 
December. We are analyzing June and December's previous years temperature data
in order to determine if Oahu is a location suitable and sustainable for the surf and 
ice cream shop year round.

## Results

To break down June and Decembers data I have used the pandas ```.describe()``` fucntion
to provide useful summary information. Below I have broken down the key data points.

### June Weather Statistics
![June Weather](https://github.com/StickySitch/Surfs_Up/blob/main/Resources/JuneStats.png)
- ```Count:``` 1700
  - Our ```count``` represents the amount of data points used to calculate these statistics. 1700 data
points observed. This amount of data points provides us with enough data to do our analysis reliably.
- ```Mean:``` 74.94°F
  - The ```mean``` or in other words, the average temperature of June is ```74.94°F```. This temperature is important
because in order to determine if Oahu is a viable location for our shop we need to know that the weather will be sunny and warm the majority of the time.
- ```Min Temp:``` 64°F
  - The ```minimum temperature``` for the month of June in Oahu is ```64°F```. Although this is decently cold, for a LOW, it's not that bad;
Especially since our average temperature is ```75°F```
- ```Max Temp:``` 85°F
  - Now we are definitely in ice cream territory! With a ```maximum temperature``` of ```85°F``` the day is not too hot but also not cold. Perfect for ice cream!

As of right now, Oahu is looking like a great location for a surf/ice cream shop! Let's dive into December!
### December Weather Statistics
![December Weather](https://github.com/StickySitch/Surfs_Up/blob/main/Resources/DecStats.png)
- ```Count:``` 1517
  - In December less data points were observed for December but I believe we still have enough to calculate reliable data.
- ```Mean:``` 71.04°F
  - With December being in the Winter season, our temperatures are inevitably going to be lower. Even though it is the Winter
season, December still has an ```average temperature``` of ```71.04°F```.
- ```Min Temp:``` 56°F
  - With a minimum temperature of ```56°F``` neither surfing or ice cream sound like a good option for those days.
- ```Max Temp:``` 83°F
  - Back into ice cream and surf territory! Our maximum temperature of December is 83°F.

## Summary

We have some good information above but to be honest, more analysis is needed to truly determine if Oahu is a viable location
for our surf/ice cream shop. Our temperature reports are not enough. Below I have some suggestions:

#### Humidity Reports
Humidity plays a huge role when we are talking about weather. For example, 75°F at 80% humidity is much hotter than 75°F at 20% 
humidity. Gathering humidity reports would help us understand the true environment of Oahu.


#### How Many Times Was The Min Temp Observed?
Another big factor for our location is it's minimum temperature. The question is, how many days out of the months were hitting those lows
or got close to it? This information is worth pursuing because if 8 of those 31 days are close to the low, December is not looking good.

#### Cloud Reports
One last suggestion I have is observing and analyzing the cloud reports. If the clouds are out, the suns not so we need to find out how cloudy
Oahu is overall.

Based on temperature, Oahu is looking like a viable option but as I mentioned above, I believe more information is needed to make a smart decision.

