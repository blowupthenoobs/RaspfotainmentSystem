# RaspfotainmentSystem

  This is a portable infotainment system running off a 2gb rasp pi that pairs with your phone to tap into their built-in infotainment system. Idealized for cars that turn off all the electrical components immediately when the car turns off. This was created after I'd been lent a car without any sort of screen or anything, and not wanting to change any parts with the car I wanted to make a portable device that could run carplay. It was designed with using OpenAuto's free edition, however as long as it can run the shutdown code, any other infotainment software should work exactly the same on the pi.


## Components List:
1. Rasp pi (should only need 2gb if you use the terminal only OS)
2. [Screen](https://www.aliexpress.us/item/3256811860307211.html?spm=a2g0o.order_list.order_list_main.79.25f01802ugS0kN&gatewayAdapt=glo2usa)
3. [Speaker](https://www.aliexpress.us/item/3256803469695339.html?spm=a2g0o.order_list.order_list_main.84.25f01802ugS0kN&gatewayAdapt=glo2usa)
4. [JD1912](https://www.aliexpress.us/item/3256810090973764.html?spm=a2g0o.order_list.order_list_main.74.25f01802ugS0kN&gatewayAdapt=glo2usa)
5. [Time Relay](https://www.aliexpress.us/item/3256808086519741.html?spm=a2g0o.order_list.order_list_main.64.25f01802ugS0kN&gatewayAdapt=glo2usa)
6. [5v to 12v amplifier](https://www.aliexpress.us/item/3256805878102803.html?spm=a2g0o.order_list.order_list_main.17.25f01802ugS0kN&gatewayAdapt=glo2usa)
7. [type C interface](https://www.aliexpress.us/item/3256810338605989.html?spm=a2g0o.order_list.order_list_main.53.25f01802ugS0kN&gatewayAdapt=glo2usa)
8. [MCP73871](https://www.aliexpress.us/item/2251832593152922.html?spm=a2g0o.order_list.order_list_main.11.25f01802ugS0kN&gatewayAdapt=glo2usa)
9. [LiPo Pouch](https://www.aliexpress.us/item/3256812285653507.html?spm=a2g0o.order_list.order_list_main.29.25f01802ugS0kN&gatewayAdapt=glo2usa)
10. [Optocoupler (linked gives 20)](https://www.aliexpress.us/item/3256808061802481.html?spm=a2g0o.order_list.order_list_main.5.25f01802vzry7D&gatewayAdapt=glo2usa)
11. [2 Diodes (linked gives 20)](https://www.aliexpress.us/item/2251832761633560.html?spm=a2g0o.order_list.order_list_main.59.25f01802ugS0kN&gatewayAdapt=glo2usa)
12. [3V3300UF Capacitor](https://www.aliexpress.us/item/3256811542313899.html?spm=a2g0o.order_list.order_list_main.23.25f01802ugS0kN&gatewayAdapt=glo2usa)
13. [Wireless Phone Connector (optional unless using IOS on free version of OpenAuto)](https://www.aliexpress.us/item/3256809934129098.html?spm=a2g0o.order_list.order_list_main.41.25f01802ugS0kN&gatewayAdapt=glo2usa)

## Wiring Diagram
<img width="839" height="711" alt="RaspInfotainmentWiring" src="https://github.com/user-attachments/assets/30aff679-3739-416b-9cf8-d529f5dc13e6" />


## Build Instructions:
1. this is step 1
2. and step 2
3. After powering on the relay, hold the K1 button and use the K2 button to switch the left number to 4 and K3/K4 to get the second number to say 2
4. Press the K1 button again and set the timer to the desired delay (15 seconds should be good) using K2/K3 to move the number up/down and K4 to move the decimal
5. Press K1 again to save your changes





