@echo off
REM Check if the argument %1 is provided

IF "%~1"=="" (
    echo Setting description to Updt
    echo .
    set Desc=Updt
) ELSE (
  set Desc=%1
)

rem IF "%~1"=="" (
rem    echo Rerun code with commit description
rem ) ELSE (
    cd D:\Resumes
    set GIT_TRACE=1
    echo FORCE A RE-READING OF THE .gitignore list IF IT CHANGES
    git rm -r --cached .
    REM adds new + modified files
    git add .
    REM ADDS EVERYTHING
    rem git add -A
    REM BELOW MAY NOT BE NEEDED ANYMORE
    REM git branch -M main
    git commit -m %Desc%
    REM COMMENTED OUT CODE FORCES A PUSH
    REM It loses track of remote updates
    REM git push origin main --force
    git push origin main
    REM echo sem nada mostra o echo status
    echo.
    echo.
    echo VIEWS IF BATCH SUCCEEDED
    REM USING "git log -n 1" IS NOT TOO USEFUL
    git log -1 --name-status 
rem )
