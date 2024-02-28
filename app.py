from flask import Flask, request
import africastalking



app = Flask(__name__)
username = "whos.kendi"
api_key = "bc3f873946b3ff05cc9802da81cf1dcbda07186cf0ebe701ce231343675c6f5f"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])

def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    #ussd logic
    if text == "":
        #main menu
        response = "CON What would you like to do?\n"
        response += "1. Apply for cover\n"
        response += "2. Check my insurance policy status\n"
        response += "3. Apply for a claim"
    elif text == "1":
        #sub menu 1
        response = "CON Available insurance poilicies\n"
        response += "1. Car insurance"
        response += "2. Medical insurance"
    elif text == "2":
        #sub menu 1 
        response = "END Your insurance status is {}".format(phone_number)
    elif text == "3":
        try:
            #sending the sms
            sms_response = sms.send("Thank you for going through this tutorial", sms_phone_number)
            print(sms_response)
        except Exception as e:
            #show us what went wrong
            print(f"Houston, we have a problem: {e}")
    elif text == "1*1":
        #ussd menus are split using *
        account_number = "1243324376742"
        response = "END Your account number is {}".format(account_number)
    elif text == "1*2":
        account_balance = "100,000"
        response = "END Your account balance is USD {}".format(account_balance)
    else:
        response = "END Invalid input. Try again."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")
