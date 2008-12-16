#!/bin/sh

aterm &

cd /

xsetroot -solid black -cursor_name left_ptr
Esetroot -scale ~/images/blur4.png &
rempd start >/dev/null &
sh $HOME/scripts/xmodmap.sh
xset b off
xset m
xset s off
ax +repeatkeys
ax repeatinterval 12
ax repeatdelay 210
unclutter -idle 1.5 -jitter 1 &
if test -z "$DBUS_SESSION_BUS_ADDRESS"; then
    eval `dbus-launch --sh-syntax --exit-with-session`
fi

