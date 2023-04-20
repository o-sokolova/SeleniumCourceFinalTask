*** Settings ***
Documentation   test robot framework
Library     Selenium2Library

*** Variables ***
${HOMEPAGE}     http://www.google.com
${BROWSER}  Chrome

*** Keywords ***
open the browser
    open browser    ${HOMEPAGE}   ${BROWSER}

search topic
    [Arguments]     ${topic}
    Input Text  name=q  ${topic}
    Press Key   name=q  \\13

*** Test Cases ***
Open Browser
    open the browser

Search on Google
    search topic    BrowserStack
