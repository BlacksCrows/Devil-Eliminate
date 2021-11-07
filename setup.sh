#!/bin/bash
# Base command (termux only!): pkg install python && apt upgrade && apt install && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py
echo "Welcome to SMSBomberPRO setup! Bomber by: ilya1391. Setup script by: fsvk74.
PS3='Select your distro: '
options=("Debian-based" "RPM-based" "Arch-based" "Slackware-based" "SuSE-based" "Gentoo-based" "Vo!d-based" "Alpine-based" "FreeBSD-based" "Termux" "Exit")
select opt in "${options[@]}"
do
    case $opt in
        "Debian-based")
			     echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo apt install python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "RPM-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo dnf install python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "Arch-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo pacman -Sy python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "Slackware-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "SuSE-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo zypper in python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "Gentoo-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo emerge -av python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "Vo!d-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo xbps-install -S python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "Alpine-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo apk add python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "FreeBSD-based")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) sudo pkg install python3 && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
        "Termux")
     			echo "Do you have python3 installed?"
				select yn in "Yes" "No"; do
    				     case $yn in
        				Yes ) pip install --upgrade pip && pip install colorama && pip install requests && python pro.py; break;;
        				No ) pkg install python && apt upgrade && apt install && pip install --upgrade pip && pip install colorama && pip install requests && python pro.py;;
    				     esac
				done
            ;;
