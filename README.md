# RaspfotainmentSystem

  This is a portable infotainment system running off a 2gb rasp pi that pairs with your phone to tap into their built-in infotainment system. Idealized for cars that turn off all the electrical components immediately when the car turns off. This was created after I'd been lent a car without any sort of screen or anything, and not wanting to change any parts with the car I wanted to make a portable device that could run carplay. It was designed with using OpenAuto's free edition, however as long as it can run the shutdown code, any other infotainment software should work exactly the same on the pi. Admittedly, most of the work is spent on making the delayed turn off system, but that's the part that keeps the raspberry pi from getting damaged or corrupted from abrupt shutdowns.

<img width="1309" height="1070" alt="Screenshot 2026-06-20 122216" src="https://github.com/user-attachments/assets/db98eb08-920c-4e8d-a330-b9b89fec53ad" />



## Components List:
1. Rasp pi (should only need 2gb if you use the terminal only OS)
2. [Screen](https://www.aliexpress.us/item/3256811860307211.html?spm=a2g0o.order_list.order_list_main.79.25f01802ugS0kN&gatewayAdapt=glo2usa)
3. [Speaker](https://www.aliexpress.us/item/3256803469695339.html?spm=a2g0o.order_list.order_list_main.84.25f01802ugS0kN&gatewayAdapt=glo2usa)
4. [JD1912](https://www.aliexpress.us/item/3256810090973764.html?spm=a2g0o.order_list.order_list_main.74.25f01802ugS0kN&gatewayAdapt=glo2usa)
5. [Time Relay](https://www.aliexpress.us/item/3256808086519741.html?spm=a2g0o.order_list.order_list_main.64.25f01802ugS0kN&gatewayAdapt=glo2usa)
6. [5v to 12v amplifier](https://www.aliexpress.us/item/3256805878102803.html?spm=a2g0o.order_list.order_list_main.17.25f01802ugS0kN&gatewayAdapt=glo2usa)
7. [type C interface](https://www.aliexpress.us/item/3256810338605989.html?spm=a2g0o.order_list.order_list_main.53.25f01802ugS0kN&gatewayAdapt=glo2usa)
8. [Double USB Charger](https://www.aliexpress.us/item/2251832663934147.html?spm=a2g0o.order_list.order_list_main.47.25f01802gfiJC2&gatewayAdapt=glo2usa)
9. [MCP73871](https://www.aliexpress.us/item/2251832593152922.html?spm=a2g0o.order_list.order_list_main.11.25f01802ugS0kN&gatewayAdapt=glo2usa)
10. [LiPo Pouch](https://www.aliexpress.us/item/3256812285653507.html?spm=a2g0o.order_list.order_list_main.29.25f01802ugS0kN&gatewayAdapt=glo2usa)
11. [Optocoupler (linked gives 20)](https://www.aliexpress.us/item/3256808061802481.html?spm=a2g0o.order_list.order_list_main.5.25f01802vzry7D&gatewayAdapt=glo2usa)
12. [2 Diodes (linked gives 20)](https://www.aliexpress.us/item/2251832761633560.html?spm=a2g0o.order_list.order_list_main.59.25f01802ugS0kN&gatewayAdapt=glo2usa)
13. [3V3300UF Capacitor](https://www.aliexpress.us/item/3256811542313899.html?spm=a2g0o.order_list.order_list_main.23.25f01802ugS0kN&gatewayAdapt=glo2usa)
14. [Wireless Phone Connector (optional unless using IOS on free version of OpenAuto)](https://www.aliexpress.us/item/3256809934129098.html?spm=a2g0o.order_list.order_list_main.41.25f01802ugS0kN&gatewayAdapt=glo2usa)
15. Zip ties
16. M2 type nuts and bolts x 24
17. Wires

## CAD Models
### Individualized Parts
I'll be adding the things here later
### Linkable Parts
- [RaspPi Case](https://linkhere)
- [Speaker Case](https://linkhere)
- [Electronics Container](https://linkhere)
- [Connecting Pieces](https://linkhere)

## Wiring Diagram
<img width="839" height="711" alt="RaspInfotainmentWiring" src="https://github.com/user-attachments/assets/30aff679-3739-416b-9cf8-d529f5dc13e6" />


## Build Instructions:
1. Using some external power source power up the relay. It should be showing four dashes in the middle of the display.
2. Hold the K1 button till P-XX (x being some number) and use the K2 button to switch the left number to 4 and K3/K4 to get the second number to say 2
3. Press the K1 button again and set the timer to the desired delay (15 seconds should be good) using K2/K3 to move the number up/down and K4 to move the decimal
4. Press K1 again to save your changes
5. On the bottom half of the electronics container, place the USB charger, JD1912, and time relay as shown. JD1912 will be held in place when the top part comes in, but the time relay has holes for M2 type nuts and bolts. The USB charger should be held down by a ziptie through the holes next to it.
6. On the upper half of the electronics container, place the USBc interface and LiPo pouch as shown. Several holes are provided for zipties to hold down the LiPo pouch, however the USBc interface is intended with use of an adhesive.
7. If intending on linking all the modules, the next step is to screw in the connecting pieces with M2 nuts and bolts
8. Finish all the wiring according to the diagram above. Any parts not mentioned earlier do not have a designated location and should be safe to be left floating inside the case. The connections to the raspberry pi's GPIO pins should lead outside the case through the bigger hole on the top part of the case.
9. Close the case and put zipties through the holes in the extrusions the cases have off to the side to hold it in place.
10. Place and srew in the raspberry pi into its case with M2 nuts and bolts
11. Connect the 2 wires outside of the electronics container and plug them into the GPIO 21 and ground ports according the wiring diagram
12. Attach the screen the the raspberry pi
13. If you are joining the different modules, use the M2 nuts and bolts to connect the raspberry pi case to the speaker
14. Stick the speaker's USB through the speaker case's hole in the back and connect it to the raspberry pi
15. If joining the modules together, align and screw in the connecting pieces to the speaker module.
16. Place the speaker inside the case
17. Apply the covering mesh to the speaker case
