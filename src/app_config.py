import os

b2c_tenant = "contoso"
signupsignin_user_flow = "B2C_1_signupsignin"
editprofile_user_flow = "B2C_1_profileediting"
resetpassword_user_flow = "B2C_1_passwordreset"
authority_template = "https://{tenant}.b2clogin.com/{tenant}.onmicrosoft.com/{user_flow}"
redirect_uri = "http://localhost/auth-response"
CLIENT_ID = "dfa891d9-2ad4-4aae-9639-fdf0423c9d22" # Application (client) ID of app registration
CLIENT_SECRET = "J6v8Q~04Slf6c6Ffd44z3Waq4MBZVLHbbqVLKc_9"