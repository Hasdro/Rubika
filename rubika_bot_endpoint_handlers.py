import requests
import json

def send_rubika_message():
    token = "JJBIG0RIHWLMKCMTHTRMUQZLZCSYCEEZQESGLWYVFOKWIAYCSRBNNWPFUGEOTDUF"
    chat_id = "b0Bn6EC01fA08b4b6678ceef57ebfcf1"
    response_text = "Hi"
    
    url = f"https://botapi.rubika.ir/v3/{token}/sendMessage"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "chat_id": chat_id,
        "text": response_text
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
