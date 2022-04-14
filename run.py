from user.signup_text import login

with login(teardown=True) as bot:
    bot.first_page()
    bot.sign_up_button()