import requests
import os

def main(context):
    # 1. Configuration from Environment Variables (Security Best Practice)
    # Get the zapikey from Appwrite settings instead of hardcoding
    zapikey = os.environ.get("ZOHO_ZAPIKEY")
    
    if not zapikey:
        context.error("ZOHO_ZAPIKEY is missing from environment variables.")
        return context.res.json({"error": "Configuration error"}, 500)

    # 2. Extract user_input from the incoming request body
    # Appwrite provides the body as a dictionary if it's JSON
    user_input_raw = context.req.body
    user_input = json.dumps(user_input_raw)

    

    # 3. Construct the Zoho URL
    # Using params= in requests handles the URL encoding (encodeUrl) automatically
    base_url = "https://www.zohoapis.com/crm/v7/functions/general_rubika_standalone/actions/execute"
    query_params = {
        "auth_type": "apikey",
        "zapikey": zapikey,
        "user_input": user_input
    }

    try:
        # 4. Execute the POST request to Zoho
        context.log(f"Forwarding input to Zoho: {user_input}")
        response = requests.post(base_url, params=query_params, timeout=15)
        
        # If Zoho returns a success status
        response.raise_for_status()
        zoho_data = response.json()

        return context.res.json({
            "status": "success",
            "zoho_response": zoho_data
        })

    except requests.exceptions.RequestException as e:
        context.error(f"Zoho API call failed: {str(e)}")
        return context.res.json({"error": "Failed to trigger Zoho function"}, 500)
