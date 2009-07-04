#!/bin/sh

cd /

xsetroot -solid black -cursor_name left_ptr
Esetroot -scale ~/images/blur4.png &
xset b off
xset m
xset s off
xmodmap -e 'pointer = 1 2 3 6 7 4 5 8 9'
xset r rate 210 83

#if test -z "$DBUS_SESSION_BUS_ADDRESS"; then
#    eval `dbus-launch --sh-syntax --exit-with-session`
#fi

sh ~/.metacity.conf
metacity &

