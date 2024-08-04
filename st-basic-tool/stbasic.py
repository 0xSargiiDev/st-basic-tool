from colorama import Fore, init

init()


print(f"""{Fore.GREEN}                         
 ____ _____   ____            _      
/ ___|_   _| | __ )  __ _ ___(_) ___ 
\___ \ | |   |  _ \ / _` / __| |/ __|
 ___) || |   | |_) | (_| \__ \ | (__ 
|____/ |_|   |____/ \__,_|___/_|\___|  
                                                                                                      
                                                                                                      
                                                                                                      """)
print(f"""{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0] Resends Logo/Options\n[1] Webhook Spammer\n[2] Vanity Checker\n[3] Viper Nuker\n[4] Phone-Number Generator\n[5] Nitro-Gen\n[6] Nitro-Checker\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def logo():
  print(f"""{Fore.GREEN}                         
 ____ _____   ____            _      
/ ___|_   _| | __ )  __ _ ___(_) ___ 
\___ \ | |   |  _ \ / _` / __| |/ __|
 ___) || |   | |_) | (_| \__ \ | (__ 
|____/ |_|   |____/ \__,_|___/_|\___|   
                                                                                                      
                                                                                                      
                                                                                                      """)
  print(f"""{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0] Resends Logo/Options\n[1] Webhook Spammer\n[2] Vanity Checker\n[3] Viper Nuker\n[4] Phone-Number Generator\n[5] Nitro-Gen\n[6] Nitro-Checker\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


while True:
    q = input("\n> ")
    if q == "1":
      import WebhookSpam
      logo()
    elif q == "2":
      import vanity_checker
      logo()
    elif q == "0":
      logo()
    elif q == "3":
      import nuker
    elif q == "4":
      import numgen
    elif q == "5":
      import nitrogen
    elif q == "6":
      import nitrocheck
    else:
      print(f"\nNo such choice {q}.")