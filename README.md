# RaspfotainmentSystem

A portable infotainment system running off a 2gb rasp pi that pairs with your phone to tap into their built-in infotainment system. Idealized for cars that turn off all the electrical components immediately when the car turns off. This was created after I'd been lent a car without any sort of screen or anything, and not wanting to change any parts with the car I wanted to make a portable device that could run carplay. It was designed with using [OpenAuto's free edition](https://github.com/f1xpl/openauto), however as long as it can run the shutdown code, any other infotainment software should work exactly the same on the pi. Admittedly, most of the work is spent on making the delayed turn off system, but that's the part that keeps the raspberry pi from getting damaged or corrupted from abrupt shutdowns. It was also specially designed to work with USB ports to make its usage as simple as possible.

<img width="1309" height="1070" alt="Screenshot 2026-06-20 122216" src="https://github.com/user-attachments/assets/db98eb08-920c-4e8d-a330-b9b89fec53ad" />

# How does it Operate?
Honestly, they way it works is rather simple. Once you get it set up, all you have to do is turn on your car and the pi will turn on with it. Turning off your car will start the shutdown initiative to turn off the pi and sustain its power for just a bit longer so that the abrupt shutdown doesn't destroy the device or the SD card.


<img width="2250" height="3450" alt="fallout_zine" src="https://github.com/user-attachments/assets/de5dab89-1610-428d-b1de-226817303fcc" />


## Components List:

| Name | link | needed | price of one | price of package |
| ---  | --- | ---| ---  | ---      |
| Rasp pi |  | 1 | $59.99 | $59.99 |
| Screen | https://www.aliexpress.us/item/3256811860307211.html?spm=a2g0o.order_list.order_list_main.79.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $15.57 | $15.57 |
| Speaker | https://www.aliexpress.us/item/3256803469695339.html?spm=a2g0o.order_list.order_list_main.84.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $22.87 | $22.87 |
| JD1912 | https://www.aliexpress.us/item/3256810090973764.html?spm=a2g0o.order_list.order_list_main.74.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $6.15 | $6.15 |
| Time Relay | https://www.aliexpress.us/item/3256808086519741.html?spm=a2g0o.order_list.order_list_main.64.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $3.32 | $3.32 |
| 5v to 12v amplifier | https://www.aliexpress.us/item/3256805878102803.html?spm=a2g0o.order_list.order_list_main.17.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $4.91 | $4.91 |
| Type C interface | https://www.aliexpress.us/item/3256810338605989.html?spm=a2g0o.order_list.order_list_main.53.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $3.54 | $3.54 |
| Double USB charger | https://www.aliexpress.us/item/2251832663934147.html?spm=a2g0o.order_list.order_list_main.47.25f01802gfiJC2&gatewayAdapt=glo2usa | 1 | $1.95 | $1.95 |
| MCP73871 | https://www.aliexpress.us/item/2251832593152922.html?spm=a2g0o.order_list.order_list_main.11.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $3.25 | $3.25 |
| LiPo Pouch | https://www.aliexpress.us/item/3256812285653507.html?spm=a2g0o.order_list.order_list_main.29.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $13.88 | $13.88 |
| Optocoupler | https://www.aliexpress.us/item/3256808061802481.html?spm=a2g0o.order_list.order_list_main.5.25f01802vzry7D&gatewayAdapt=glo2usa | 1 | $0.13 | $2.57 |
| Diodes | https://www.aliexpress.us/item/2251832761633560.html?spm=a2g0o.order_list.order_list_main.59.25f01802ugS0kN&gatewayAdapt=glo2usa | 2 | $0.09 | $1.70 |
| 3V3300UF Capacitor | https://www.aliexpress.us/item/3256811542313899.html?spm=a2g0o.order_list.order_list_main.23.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $0.48 | $4.82 |
| Wireless Phone Connector (optional unless using IOS on free version of OpenAuto) | https://www.aliexpress.us/item/3256809934129098.html?spm=a2g0o.order_list.order_list_main.41.25f01802ugS0kN&gatewayAdapt=glo2usa | 1 | $29.49 | $29.49 |
| Zipties | https://www.homedepot.com/p/Commercial-Electric-8in-Standard-50lb-Tensile-Strength-UL-21S-Rated-Cable-Zip-Ties-100-Pack-UV-Black-GT-200STCB/203531910 | 9 | $0.12 | $12.46 |
| M2 nuts and bolts | https://www.homedepot.com/p/Prime-Line-M2-0-4-x-8-mm-Grade-A2-70-Stainless-Steel-Phillips-Drive-Flat-Head-Metric-Machine-Screws-10-Pack-9120618/311229766 | 28 | $0.54 | $5.43 x 3 |
| Wires | [Link](https://www.amazon.com/California-JOS-Breadboard-Optional-Multicolored/dp/B0BRTL3BHR?tag=bingshoppinga-20&linkCode=df0&hvadid=80470717339063&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=103304&hvtargid=pla-4584070205420867&psc=1&hvocijid=15639618107126028530-B0BRTL3BHR-&hvexpln=0) | -- | $0.11 | $4.59 |
| USBc Cables | https://www.aliexpress.us/item/3256808184974434.html?spm=a2g0o.order_list.order_list_main.69.25f01802bj1ZPU&gatewayAdapt=glo2usa | 2 | $3.15 | $3.15 x 2 |
| Total Cost | --- | - | --- | $213.65 |

- I will note that AliExpress tends to hold a lot of that stuff on discount, so if you were to build this, your total is likely not going to reach that high

## CAD Models
### Individualized Parts
- [RaspPi Case](https://eventuallyPut)
- [Speaker Case](https://placeholder)
- [Electronics Container](https://placeholder)
- [Connecting Pieces](https://placeholder)
### Linkable Parts
- https://www.thingiverse.com/thing:737250 (I will publish as soon as it will let me, lol. It's also in the repo rn tho.)

## Wiring Diagram
<img width="839" height="711" alt="RaspInfotainmentWiring" src="https://github.com/user-attachments/assets/30aff679-3739-416b-9cf8-d529f5dc13e6" />


## Build Instructions:
1. Make sure to install whatever program you intend on using, as well as the firmware for the shutdown code. Make sure it automatically runs whenever the pi is turned on.
2. Using some external power source power up the relay. It should then show four dashes in the middle of the display.
3. Hold the K1 button till P-XX (x being some number) and use the K2 button to switch the left number to 4 and K3/K4 to get the second number to say 2
4. Press the K1 button again and set the timer to the desired delay (15 seconds should be good) using K2/K3 to move the number up/down and K4 to move the decimal
5. Press K1 again to save your changes
6. On the bottom half of the electronics container, place the USB charger, JD1912, and time relay as shown. JD1912 will be held in place when the top part comes in, but the time relay has holes for M2 type nuts and bolts. The USB charger should be held down by a ziptie through the holes next to it.
7. On the upper half of the electronics container, place the USBc interface and LiPo pouch as shown. Several holes are provided for zipties to hold down the LiPo pouch, however the USBc interface is intended with use of an adhesive.
8. If intending on linking all the modules, the next step is to screw in the connecting pieces with M2 nuts and bolts
9. Finish all the wiring according to the diagram above. Any parts not mentioned earlier do not have a designated location and should be safe to be left floating inside the case. The connections to the raspberry pi's GPIO pins should lead outside the case through the bigger hole on the top part of the case.
10. Close the case and put zipties through the holes in the extrusions the cases have off to the side to hold it in place.
11. Place and srew in the raspberry pi into its case with M2 nuts and bolts
12. Connect the 2 wires outside of the electronics container and plug them into the GPIO 21 and ground ports according the wiring diagram
13. Attach the screen the the raspberry pi
14. If you are joining the different modules, use the M2 nuts and bolts to connect the raspberry pi case to the speaker
15. Stick the speaker's USB through the speaker case's hole in the back and connect it to the raspberry pi
16. If joining the modules together, align and screw in the connecting pieces to the speaker module.
17. Place the speaker inside the case
18. Apply the covering mesh to the speaker case

# Credits
A lot of the design was inspired by https://github.com/soubhik-khan/RPI_delayed_Shutdown however it seems that they integrated their circuit into the car, which I did not want to do (hence the wildly different wiring diagram.) I was originally only going to reference their python script, however after looking through it I realized that it was basically the exact thing I would've had to write so it's admittedly basically only their code but with some minor tweaks. (I'm glad I don't have to figure out how to use python though, I'm still running from that inevitable fate, lol.)


##### Disclaimer
###### As far as my hack club submission goes, I was intending on building this irl, however I was unable to get all the parts in before the deadline, so most of the stuff is untested other than parts of the circuitry and the raspberry pi case which has been tweaked to a basically perfect fit.     I initially had much bigger plans for this like creating flipper zero integration to control the media, but ran out of time :(
