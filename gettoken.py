import requests
import json

_banner_ = '''
\033[1;91m ooooooooo.                                o8o  
\033[1;92m`888   `Y88.                              `"'  
\033[1;97m 888   .d88'  .ooooo.  ooo. .oo.  .oo.   oooo  
\033[1;98m 888ooo88P'  d88' `88b `888P"Y88bP"Y88b  `888  
\033[1;99m 888`88b.    888   888  888   888   888   888  
\033[1;93m 888  `88b.  888   888  888   888   888   888  
\033[1;97mo888o  o888o `Y8bod8P' o888o o888o o888o o888o 
                                               
                                               
                                                   
                                       
                                       
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  +++=== GET TOKEN FACEBOOK ===+++   
 ++== Tools Get Token Facebook ==++
+= No Spam Dettect Server Facebook =+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

# author : Romi
# contact: 0327*******
'''
user=raw_input('username/email: ')
passw=raw_input('password: ')
get = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+passw+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

up = get.content
pu = json.loads(up)
if "session_key" in up:
    print
    print _banner_
    print 'username:' + pu['identifier']
    print 'token:' + pu["access_token"]
    open(user+'-token.txt', 'a').write(pu["access_token"])
    print
    print 'saved file to '+user+'-token.txt'
else:
    print 'maaf username/password salah'
