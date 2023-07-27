import pandas as pd
name=[];band_2G= [];  band_3G= [];  band_4G= [];  band_5G= [];  announced= [];  released= []; dimension= [];  weight= [];  
build= [];  sim= [];  bodyother= []; displaytype= [];  displaysize= [];  displayresolution= [];  displayprotection= []; 
displayother= [];  os= [];  chipset= [];  cpu= [];  gpu= [];  memoryslot= []; internalmemory= [];  cam1modules= [];  cam1features= []; 
cam1video= [];  cam2modules= [];  cam2features= []; cam2video= [];  loudspeaker= [];  jack= [];  wlan= [];  bluetooth= []; 
gps= [];  nfc= [];  radio= [];  usb= []; sensors=[];bat_type=[];charging=[];battalktime1=[]; colors= [];  model_names= [];  
sar_us= []; sar_eu= [];  price= [];  benchmarks= []; 
battery_test= [];  popularity= [];  review=[]
specs= {'Name':name, '2G':band_2G, '3G':band_3G, '4G':band_4G, '5G':band_5G, 'Announced':announced, 'Released':released,
        'Dimension':dimension, 'Weight':weight, 'Build':build, 'Sim':sim, 'Body(Other)':bodyother,
        'Display Type':displaytype, 'Display Size':displaysize, 'Resolution':displayresolution, 'Display Protection':displayprotection,
        'Display(Other)':displayother, 'OS':os, 'Chipset':chipset, 'CPU':cpu, 'GPU':gpu, 'Memory(External)':memoryslot,
        'Memory(Internal)':internalmemory, 'Main Camera':cam1modules, 'Main Camera(Features)':cam1features,
        'Main Camera(Video)':cam1video, 'Front Camera':cam2modules, 'Front Camera(Features)':cam2features,
        'Front Camera(Video)':cam2video, 'Speker':loudspeaker, 'Headphone Jack':jack, 'WiFi':wlan, 'Bluetooth':bluetooth,
        'GPS':gps, 'NFC':nfc, 'Radio':radio, 'USB':usb,'Sensors':sensors,'Battery Type':bat_type, 'Charging':charging,
        'Battery Talktime':battalktime1, 'Colors':colors, 'Models':model_names, 'SAR':sar_us,
        'SAR EU':sar_eu, 'Price':price, 'Benchmark Results':benchmarks,
        'Battery Test':battery_test, 'Popularity':popularity, 'Rating':review}

path = 'specs.csv'
pd.DataFrame(specs,columns=list(specs.keys())).to_csv(path)