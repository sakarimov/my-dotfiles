#!/bin/sh
feh --bg-scale /home/sulthan/Pictures/wallpaper/midjourney_ai_sunset_aurora_borealis_4k_wallpaper_by_darkprncsai_dfeiukg-fullview.jpg
picom &
disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh &
disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
disown # start polkit agent from GNOME

#blueman-applet &
greenclip daemon &
dunst &
