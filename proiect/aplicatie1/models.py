import pandas as pd
from django.db import models
from django.http import request
#from aplicatie1.views import load_cities as country_id



df = pd.read_csv("C:/Users/radul/OneDrive/Desktop/GooglePython/proiect/worldcities.csv")
sortare=set(df['country'])
list=[]
for x in sortare:
    list.append((x,x))
list=sorted(list)
nume_tari=tuple(list)


sortare2=(df['city_ascii'])

y="Romania"
df_list=sortare2[df['country'].str.contains(y)]
list2=[]
for x in df_list:
    list2.append((x,x))
list2=sorted(list2)
nume_orase=tuple(list2)

class Locations(models.Model):
    city = models.CharField(max_length=100, choices=nume_orase)
    country = models.CharField(max_length=150, choices=nume_tari)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.city} - {self.country}"

