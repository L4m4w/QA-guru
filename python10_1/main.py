from selene import browser, be, have


browser.open('https://demoqa.com/text-box')
browser.element('[id="userName"]').should(be.blank).type('QA-Guru').press_enter()
browser.element('[id="submit"]').click()

try:
    browser.element('[id="name"]').should(have.text('Name:QA-Guru'))
    print("Успешный успех!")
except:
    print("Ошибонька")

