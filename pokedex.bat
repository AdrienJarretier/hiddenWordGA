@echo off

if %1 == 1 (
    set /a start=1
    set /a end=25
) else (
    set /a start=25
    set /a end=1
)

for /l %%x in (%start%, %1, %end%) do (
    python algoGen.py %%x
)