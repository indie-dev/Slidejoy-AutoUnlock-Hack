@ECHO OFF
TIMEOUT 2
echo Locking!
adb shell input keyevent 26
TIMEOUT 2
echo Unlocking!
adb shell input keyevent 26
TIMEOUT 2
echo Opening ad!
adb shell input swipe 540 960 -1000 960
TIMEOUT 5

echo Locking!
adb shell input keyevent 26
TIMEOUT 2
echo Unlocking!
adb shell input keyevent 26
TIMEOUT 2
echo Opening!
adb shell input swipe 540 960 1000 960
TIMEOUT 2

echo AGAIN!
TIMEOUT 2
lock.bat
@ECHO ON