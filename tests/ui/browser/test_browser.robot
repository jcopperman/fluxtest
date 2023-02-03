*** Settings ***
Library    Browser
Variables    variables.py

*** Test Cases ***
Example Test
    Open Browser To Google
    New Page    https://robotsparebinindustries.com
    Type Text    input#username    maria
    Type Text    input#password   password
    Click    button.btn-primary
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Google
    Open Browser    https://www.google.com    browser=chromium


