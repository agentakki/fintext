from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)

callers = {
    "+13109808652" : "Akshay",
    "+14803820676" : "Harrison",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming text by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Thanks for the message, human."
 
    resp = twilio.twiml.Response()
    resp.message(message)
    
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
