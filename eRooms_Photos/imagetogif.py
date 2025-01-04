import imageio.v3 as iio
from PIL import Image
width=1400
height=800
photos=10
titles= ['./ElegantStudio/' ,
         './BoutiqueAtHistoricCentrum2/' ,
         './Ilishouse/',
         './KompsoStudio/',
         './PlateiaPargisApartmentsI/',
         './PlateiaPargisApartmentsII/'
         ]
for title in titles:
    gifname=title.strip("./")
    print(gifname)

    filenames_initial =[]
    for photo in range(photos):
        filenames_initial.append(str(title)+str(photo+1)+'.jpg')


    filenames_size=[]

    for filename_initial  in filenames_initial:
        filenames_size.append(Image.open(filename_initial).resize((width,height)))

    i=0
    for filename_size in filenames_size:
         i= i+1
         filename_size.save(str(title)+str(i)+'.jpg')

    filenames = []


    for photos in range(photos):
        filenames.append(str(title)+str(photos+1)+'.jpg')


    images= []

    for filename in filenames:
        images.append(iio.imread(filename))

    iio.imwrite(str(title)+gifname+'.gif' , images ,duration=2000, loop=0)