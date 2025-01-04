import pandas as pd
import folium
import numpy as np
import imageio.v3 as iio
from supabase import create_client, Client
from bs4 import BeautifulSoup as Soup


## usefule link
#https://levelup.gitconnected.com/creating-interactive-maps-with-python-folium-and-some-html-f8ac716966f
exportfilename= "test.html"
gr =False
en= True
database ="eRoomsShortTerm"


map = folium.Map(location=[39.67, 20.86], zoom_start=8)

url = "https://qnscunyvfnnzesjgophl.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFuc2N1bnl2Zm5uemVzamdvcGhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxMDc4NzksImV4cCI6MjAzODY4Mzg3OX0.ApOkDtGdm3eGRl0lR8A9PvijBQMtbORS2aVX-UR96ag"
supabase = create_client(url, key)
data = supabase.table(database).select("*").execute()







lendata = len(data.data)

for i in range(0, len(data.data)):
    test=folium.Html(f"""
            <!DOCTYPE html>
            <html>
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

#par ="<p>Test Page</p>"
#body.insert_after(par)

map.save('shorttermmap.html')



HtmlFile = open(exportfilename, 'r', encoding='utf-8')
source_code = HtmlFile.read()

soup = Soup(source_code,'html.parser')

with open(exportfilename, "w", encoding='utf-8') as file:
    file.write(str(soup))


f = open(exportfilename ,'r', encoding='utf-8')
yourList = f.readlines()
#print(yourList)
i=-1
for text in yourList:
   # print(text)
    i= i+1
    if text.strip() =="<body>":
       print("I got u in pos ", i)

#print(len(yourList))
#print(yourList[-1])


greek  = """ 
   <nav class="navbar navbar-expand-lg bg-body-tertiary" >
    <div class="container-fluid" >
      
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
           <li class="nav-item">
            <a class="navbar-brand" href="#" > <img src="./bed_icon.png" alt="erooms icon" height="30"> </a>
          </li> 
             <li class="nav-item">
            <a class="navbar-brand" href="#" > <h2>eRooms</h2> </a>
          </li> 
          <li class="nav-item">
           <h4> <a class="nav-link active" aria-current="page" href="index_gr.html">Αρχική</a></h4>
          </li>
          <li class="nav-item">
            <h4>  <a class="nav-link active" aria-current="page" href="longtermmap_gr.html">Χάρτης Μακροχρόνιας Ενοικίασης</a></h4>
          </li> 
          <li class="nav-item">
             <h4> <a class="nav-link active" aria-current="page" href="shorttermmap.html">Χάρτης Βραχυχρόνιας Ενοικίασης</a></h4>
          </li> 

          <li class="nav-item">
            <h4>  <a class="nav-link active" aria-current="page" href="register_gr.html">Καταχωρήστε την Ιδιοκτησίας(Δωρεάν!)</a></h4>
          </li> 

          <li class="nav-item">
            <h4>  <a class="nav-link active" aria-current="page" href="download_gr.html">Λήψη Κιν. Εφαρμογής</a></h4>
          </li> 

           
          <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="index.html">
              <img src="./uk.svg" alt="british icon" height="30"> </a>
          </li> 

            <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="index.html">
             <h4>English</h4></a>
          </li> 

          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="index_gr.html">
              <img src="./gr.svg" alt="british icon" height="30">
               </a>
          </li> 

           <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="index_gr.html">
               <h4> Ελληνικά</h4></a>
          </li> 

          <li class="nav-item">
            <h4> <a class="nav-link" href="about_gr.html">About</a></h4>
          
         
        </ul>
        
      </div>
    </div>
  </nav>

"""
english = """ 

 <nav class="navbar navbar-expand-lg bg-body-tertiary" >
    <div class="container-fluid" >
      
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
           <li class="nav-item">
            <a class="navbar-brand" href="#" > <img src="./bed_icon.png" alt="erooms icon" height="30"> </a>
          </li> 
             <li class="nav-item">
            <a class="navbar-brand" href="#" > <h2>eRooms</h2> </a>
          </li> 
          <li class="nav-item">
           <h4> <a class="nav-link active" aria-current="page" href="index.html">Home</a></h4>
          </li>
          <li class="nav-item">
            <h4>  <a class="nav-link active" aria-current="page" href="longtermmap.html">LongTerm Map</a></h4>
          </li> 
          <li class="nav-item">
             <h4> <a class="nav-link active" aria-current="page" href="shorttermmap.html">ShortTerm Map</a></h4>
          </li> 

          <li class="nav-item">
            <h4>  <a class="nav-link active" aria-current="page" href="register.html">Register Your Property(free!)</a></h4>
          </li> 

          <li class="nav-item">
            <h4>  <a class="nav-link active" aria-current="page" href="download.html">Download Mobile App</a></h4>
          </li> 

           
          <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="index.html">
              <img src="./uk.svg" alt="british icon" height="30"> </a>
          </li> 

            <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="index.html">
             <h4>English</h4></a>
          </li> 

          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="index_gr.html">
              <img src="./gr.svg" alt="british icon" height="30">
               </a>
          </li> 

           <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="index_gr.html">
               <h4> Ελληνικά</h4></a>
          </li> 

          <li class="nav-item">
            <h4> <a class="nav-link" href="about.html">About</a></h4>
          
         
        </ul>
        
      </div>
    </div>
  </nav>




"""

yourList[2]= """<html data-bs-theme="dark"> """

bootstrap= """ <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css"
 rel="stylesheet" integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">  """

yourList.insert(33,bootstrap)
if gr == True:
    yourList.insert(35,greek)
if en == True:
    yourList.insert(35,greek)
#for text in yourList:
#    print(text)


with open(exportfilename, 'w' ,encoding='utf-8') as f:
    for text in yourList:
        f.write(text)
