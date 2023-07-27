import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

links = []
with open("phone_links.txt", "r") as f:
    for line in f:
        if re.search('oneplus',line[:-1]):
            links.append(line[:-1])

filepath = 'specs.csv'

ip_addresses = []
with open("ip_addresses.txt", "r") as f:
    for i in range(100):
        ip_addresses.append(f.readline()[0:-1])
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


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

def get_specs(html,specs):
    soup = BeautifulSoup(html.content,'lxml')
    # name
    name1 = soup.find('h1',{'data-spec':'modelname'})
    name.append(None) if name1 is None else name.append(name1.get_text())
    # network tab
    col_names_html = soup.select('#specs-list td.ttl')
    col_names = []
    for col_name in col_names_html:
        col_names.append(col_name.get_text())
    band_2G.append(True)  if '2G bands' in col_names else band_2G.append(False)
    band_3G.append(True)  if '3G bands' in col_names else band_3G.append(False)
    band_4G.append(True)  if '4G bands' in col_names else band_4G.append(False)
    band_5G.append(True)  if '5G bands' in col_names else band_5G.append(False)
    # Launch Info
    announced1 = soup.find("td", {"data-spec" : "year"})
    announced.append(None) if announced1 is None else announced.append(announced1.get_text())
    released1 = soup.find("td", {"data-spec" : "status"})
    released.append(None) if released1 is None else released.append(released1.get_text())
    # Body
    dimension1 = soup.find("td", {"data-spec" : "dimensions"})
    dimension.append(None) if dimension1 is None else dimension.append(dimension1.get_text())
    weight1 = soup.find("td", {"data-spec" : "weight"})
    weight.append(None) if weight1 is None else weight.append(weight1.get_text())
    build1 = soup.find("td", {"data-spec" : "build"})
    build.append(None) if build1 is None else build.append(build1.get_text())
    sim1 = soup.find("td", {"data-spec" : "sim"})
    sim.append(None) if sim1 is None else sim.append(sim1.get_text())
    bodyother1 = soup.find("td", {"data-spec" : "bodyother"})
    bodyother.append(None) if bodyother1 is None else bodyother.append(bodyother1.get_text())
    # Display
    displaytype1 = soup.find("td", {"data-spec" : "displaytype"})
    displaytype.append(None) if displaytype1 is None else displaytype.append(displaytype1.get_text())
    displaysize1 = soup.find("td", {"data-spec" : "displaysize"})
    displaysize.append(None) if displaysize1 is None else displaysize.append(displaysize1.get_text())
    displayresolution1 = soup.find("td", {"data-spec" : "displayresolution"})
    displayresolution.append(None) if displayresolution1 is None else displayresolution.append(displayresolution1.get_text())
    displayprotection1 = soup.find("td", {"data-spec" : "displayprotection"})
    displayprotection.append(None) if displayprotection1 is None else displayprotection.append(displayprotection1.get_text())
    displayother1 = soup.find("td", {"data-spec" : "displayother"})
    displayother.append(None) if displayother1 is None else displayother.append(displayother1.get_text())
    # Platform
    os1 = soup.find("td", {"data-spec" : "os"})
    os.append(None) if os1 is None else os.append(os1.get_text())
    chipset1 = soup.find("td", {"data-spec" : "chipset"})
    chipset.append(None) if chipset1 is None else chipset.append(chipset1.get_text())
    cpu1 = soup.find("td", {"data-spec" : "cpu"})
    cpu.append(None) if cpu1 is None else cpu.append(cpu1.get_text())
    gpu1 = soup.find("td", {"data-spec" : "gpu"})
    gpu.append(None) if gpu1 is None else gpu.append(gpu1.get_text())
    # Memory
    memoryslot1 = soup.find("td", {"data-spec" : "memoryslot"})
    memoryslot.append(None) if memoryslot1 is None else memoryslot.append(memoryslot1.get_text())
    internalmemory1 = soup.find("td", {"data-spec" : "internalmemory"})
    internalmemory.append(None) if internalmemory1 is None else internalmemory.append(internalmemory1.get_text())
    # Camera
    cam1modules1 = soup.find("td", {"data-spec" : "cam1modules"})
    cam1modules.append(None) if cam1modules1 is None else cam1modules.append(cam1modules1.get_text())
    cam1features1 = soup.find("td", {"data-spec" : "cam1features"})
    cam1features.append(None) if cam1features1 is None else cam1features.append(cam1features1.get_text())
    cam1video1 = soup.find("td", {"data-spec" : "cam1video"})
    cam1video.append(None) if cam1video1 is None else cam1video.append(cam1video1.get_text())
    cam2modules1 = soup.find("td", {"data-spec" : "cam2modules"})
    cam2modules.append(None) if cam2modules1 is None else cam2modules.append(cam2modules1.get_text())
    cam2features1 = soup.find("td", {"data-spec" : "cam2features"})
    cam2features.append(None) if cam2features1 is None else cam2features.append(cam2features1.get_text())
    cam2video1 = soup.find("td", {"data-spec" : "cam2video"})
    cam2video.append(None) if cam2video1 is None else cam2video.append(cam2video1.get_text())
    # Sound
    loudspeaker1 = soup.findAll('a',text='Loudspeaker')[0]
    loudspeaker1 = None if loudspeaker1 is None else loudspeaker1.parent.parent.find('td',class_='nfo')
    loudspeaker.append(None) if loudspeaker1 is None else loudspeaker.append(loudspeaker1.get_text())
    jack1 = soup.find('a',text='3.5mm jack')
    jack1 = None if jack1 is None else jack1.parent.parent.find('td',class_='nfo')
    jack.append(None) if jack1 is None else jack.append(jack1.get_text())
    # Comms
    wlan1 = soup.find("td", {"data-spec" : "wlan"})
    wlan.append(None) if wlan1 is None else wlan.append(wlan1.get_text())
    bluetooth1 = soup.find("td", {"data-spec" : "bluetooth"})
    bluetooth.append(None) if bluetooth1 is None else bluetooth.append(bluetooth1.get_text())
    gps1 = soup.find("td", {"data-spec" : "gps"})
    gps.append(None) if gps1 is None else gps.append(gps1.get_text())
    nfc1 = soup.find("td", {"data-spec" : "nfc"})
    nfc.append(None) if nfc1 is None else nfc.append(nfc1.get_text())
    radio1 = soup.find("td", {"data-spec" : "radio"})
    radio.append(None) if radio1 is None else radio.append(radio1.get_text())
    usb1 = soup.find("td", {"data-spec" : "usb"})
    usb.append(None) if usb1 is None else usb.append(usb1.get_text())
    # Features
    sensors1 = soup.find("td", {"data-spec" : "sensors"})
    sensors.append(None) if sensors1 is None else sensors.append(sensors1.get_text())
    # Battery
    bat_type1 = soup.find("td", {"data-spec" : "batdescription1"})
    bat_type.append(None) if bat_type1 is None else bat_type.append(bat_type1.get_text())
    charging1 = soup.find('a',text='Charging')
    charging1 = None if charging1 is None else charging1.parent.parent.find('td',class_='nfo')
    charging.append(None) if charging1 is None else charging.append(charging1.get_text())
    battalktime11 = soup.find("td", {"data-spec" : "battalktime1"})
    battalktime1.append(None) if battalktime11 is None else battalktime1.append(battalktime11.get_text())
    # Misc
    colors1 = soup.find("td", {"data-spec" : "colors"})
    colors.append(None) if colors1 is None else colors.append(colors1.get_text())
    model_names1 = soup.find("td", {"data-spec" : "models"})
    model_names.append(None) if model_names1 is None else model_names.append(model_names1.get_text())
    sar_us1 = soup.find("td", {"data-spec" : "sar-us"})
    sar_us.append(None) if sar_us1 is None else sar_us.append(sar_us1.get_text())
    sar_eu1 = soup.find("td", {"data-spec" : "sar-eu"})
    sar_eu.append(None) if sar_eu1 is None else sar_eu.append(sar_eu1.get_text())
    price1 = soup.find("td", {"data-spec" : "price"})
    price.append(None) if price1 is None else price.append(price1.get_text())
    # Tests
    benchmarks1 = soup.find("td", {"data-spec" : "tbench"})
    benchmarks.append(None) if benchmarks1 is None else benchmarks.append(benchmarks1.get_text())
    battery_test1 = soup.find("td", {"data-spec" : "batlife"})
    battery_test.append(None) if battery_test1 is None else battery_test.append(battery_test1.get_text().strip())
    # Others
    popularity1 = soup.select('li.help-popularity span')
    popularity.append(None) if popularity1 is None else popularity.append(popularity1[0].get_text())
    review_url = soup.select('li.article-info-meta-link.article-info-meta-link-review.light.large.help.help-review a')
    if review_url is None or review_url==[]:
        review.append(None)
    else :
        review_url = "https://www.gsmarena.com/"+review_url[0]['href']
        review_response = requests.get(review_url,proxies=proxy,headers=headers)
        review_soup = BeautifulSoup(review_response.content,'lxml')
        review1 = review_soup.select('span.score')
        review.append(None) if review1 is None or review1==[] else review.append(review1[0].get_text())

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



i=0
for ip_address in ip_addresses:
    proxy = {'http': 'http://' + ip_address}
    while i<len(links):
        try:
            response = requests.get(links[i], proxies=proxy,headers=headers)
            if response.status_code == 429:
                break
            get_specs(response,specs)
            i=i+1
            print(f"{i} links are done")
            if i%1==0:
                temp = pd.read_csv(filepath,index_col=0)
                pd.concat([temp,pd.DataFrame(specs)],ignore_index=True).to_csv(filepath)
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
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while using {ip_address}: {e}")
    if i==len(links):
        break
    if response.status_code == 429:
        continue


print(specs,'\n\n')