from gen_fun import get_response

def main_bot():
    print("chatbot: hi how can i help you (abanob nabil) ?")
    
    while True:
        user_input=input("user: ").lower()
    
        responses=get_response(user_input)
        print("chatbot:",responses)
        
        if user_input == "goodbye":
            break
        

        