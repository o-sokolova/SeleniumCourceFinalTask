*** Settings ***
Library     Selenium2Library

*** Variables ***
${FIRST_PRODUCT_PAGE}   http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209
${BROWSER}  Chrome
${ALERT_PRICE}    css=.alert:nth-child(3) .alertinner p strong
${EXPECTED_PRICE}     css=.product_main .price_color
${ALERT_NAME}    css=.alert:nth-child(1) .alertinner strong
${EXPECTED_NAME}     css=.product_main h1
${ADD_BTN}      css=.btn-add-to-basket

*** Keywords ***
open
    open browser    ${FIRST_PRODUCT_PAGE}   ${BROWSER}

add to basket
    click button    ${ADD_BTN}

check book name
    ${result}=    get text    ${ALERT_NAME}
    ${expected}=    get text    ${EXPECTED_NAME}
    should be equal as strings    ${result}     ${expected}

check book price
    ${result}=    get text    ${ALERT_PRICE}
    ${expected}=    get text    ${EXPECTED_PRICE}
    should be equal as strings    ${result}     ${expected}

*** Test Cases ***
test user can add product to basket
    open
    add to basket
    check book name
    check book price