
# coding: utf-8

# In[12]:

import os #for listing directories
import pandas #for reading csv file 
import folium # for creating Map
from geopy.geocoders import Nominatim #for getting Lat and Long for the address provided


# In[8]:

os.listdir('./../Jupyter/DataAnalysisPandas/')


# In[11]:

data=pandas.read_csv('supermarkets.csv')
data


# In[13]:

nom = Nominatim();


# In[22]:

data[1:2]


# In[32]:

data=data.drop(data.index[1]) #dropping because there is no Latitude and Longitude available for this address


# In[33]:

data


# In[34]:

wholeAddress=data['Address']+', '+data['City']+', '+data['State']+', '+data['Country']


# In[48]:

wholeAddress=list(wholeAddress)


# In[50]:

wholeData=[nom.geocode(wholeAddress[i]) for i in range(5)]
print wholeData


# In[51]:

wholeData[0]


# In[54]:

Latitude=[wholeData[i].latitude for i in range(5)]
Longitude=[wholeData[i].longitude for i in range(5)]


# In[55]:

Latitude


# In[57]:

data.to_csv('superMarketsWithLatLong.csv')


# In[66]:

Location = [str(Latitude[i])+', '+ str(Longitude[i]) for i in range(5)]


# In[75]:

LatLong=(list(Location));
LatLong[0]


# In[80]:

map=folium.Map(location=[LatLong[0]],zoom_start=12,tiles='Stamen Terrain')


# In[81]:

map.save('superMarketsMap.html')


# In[134]:

map2=folium.Map(location=[LatLong[0]],zoom_start=12,tiles='Stamen Terrain')
[folium.Marker(location=[LatLong[i]], popup=data['Name'][i]).add_to(map2) for i in range(5)]


# In[135]:

map2.save('superMarketsMap2.html')


# In[132]:

data


# In[ ]:



