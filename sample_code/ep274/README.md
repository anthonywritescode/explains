# [programmable nintendo switch controller (intermediate)](https://youtu.be/chvgQUX7QaI)

I've been working on this project for quite a while -- it allows me to program a nintendo switch controller using python!  In this video I show all the parts I used and how I put it together as well as how I've used it to find shiny pokemon, mass release pokemon and more!

## Interactive examples

### Bash

```bash
git clone git@github.com:asottile/switch-microcontroller
# git clone https://github.com/asottile/switch-microcontroller
cd switch-microcontroller

make MCU=atmega32u4
sudo --validate
sudo avrdude -v -patmega32u4 -cavr109 -P/dev/ttyACM0 -Uflash:w:output.hex

nano press.py
python -m press A
python -m press B

nano revive_fossils.py
python -m revive_fossils --part1 top --part2 top --count 2
python -m reset
```
