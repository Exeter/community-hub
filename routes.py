import webapp2
from webapp2 import Route

config = {}
config['webapp2_extras.auth'] = {
    'user_model': 'handlers.account.User'
}
config['webapp2_extras.sessions'] = {
    'secret_key': 'ikrm~BbMF2/7v]yljeL|v^9K}]S+-@4?p-;^cCzrG9RjYda}is`:}=(n<S~o.J,z',
}

application = webapp2.WSGIApplication([
#    Route('/register', 'handlers.account.RegisterHandler'),
    Route('/login', 'handlers.account.LoginHandler'),
    Route('/logout', 'handlers.account.LogoutHandler'),
    Route('/main_page', 'handlers.account.MainPage'),
#    Route('/forgot', 'handlers.account.ForgotPasswordHandler'),
], debug=True, config=config)

