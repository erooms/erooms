import pandas as pd
import folium
import numpy as np
import imageio.v3 as iio
from supabase import create_client, Client


map = folium.Map(location=[39.67, 20.86], zoom_start=8)

url = "https://qnscunyvfnnzesjgophl.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFuc2N1bnl2Zm5uemVzamdvcGhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxMDc4NzksImV4cCI6MjAzODY4Mzg3OX0.ApOkDtGdm3eGRl0lR8A9PvijBQMtbORS2aVX-UR96ag"
supabase = create_client(url, key)
data = supabase.table("eRoomsShortTerm").select("*").execute()







lendata = len(data.data)

for i in range(0, len(data.data)):
    test=folium.Html(f"""
            <!DOCTYPE html>
            <html data-bs-theme="dark">
              <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet"
                 integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
          
         
            <h1> {data.data[i]['Title']}</h1>  
            <h1>Name: {data.data[i]['Name']}</h1> 
            <h1>LastName: {data.data[i]['Lastname']}</h1> 
            <h1>PhoneNumber: {data.data[i]['Phonenumber']}</h1>
            <h1>Address: {data.data[i]['Address']} </h1>
            <h1>Price: {data.data[i]['Price']} Euros </h1> 
            <p><img src = "./eRooms_Photos/{data.data[i]['Title'].replace(" ", "")}/{data.data[i]['Title'].replace(" ", "")}.gif" width = "400"  height="300" style = "border-radius: 50px;"/></p>
            <h1>Website 2: {data.data[i]['Website2']} </h1> 
           
          
            </html>
              """, script=True)
    popup = folium.Popup(test, max_width=700)
    folium.Marker(
        location=[data.data[i]['y'], data.data[i]['x']],  # lat lon
        popup=popup,
    ).add_to(map)

map.save('shorttermmap.html')