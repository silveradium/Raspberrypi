# 🛻 Raspberry Pi Remote Car 

This is a simple Raspberry Pi-based web-controllable car.

## Features
- Motor control via keyboard (Arrow keys) (up,down,left,right)
- Flask web server
- GPIO control for motors

## Information
There are 2 files. 
- normal.py - 2 wheels are controlling the direction. With this configuration you can't simultaneously go forward and go left.
- with_servo.py - Here addictional wheel is attached at the backt o controll the direction. Here you can turn while moving forward or backwards. This feature will get added to the normal.py configuration in the future.

## 🛠 How to Run
```bash
python3 normal.py
python3 with_servo.py