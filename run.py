from user.signup_text import login

with login() as bot:
    bot.first_page()
    bot.login_test('op1@gmail.com', 'Test12345_')