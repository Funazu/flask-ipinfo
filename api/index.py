from flask import Flask, render_template, request, abort
import requests
import ipaddress
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def fetch_ip_info(ip_address=''):
    try:
        url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch IP data: {e}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.route('/')
def my_ip_info():
    # Get the IP of the user accessing the application
    user_ip = request.remote_addr
    data = fetch_ip_info(user_ip)
    return render_template("ipinfo.html", data=data)

@app.route('/<ip>')
def show_ip_info(ip):
    if not is_valid_ip(ip):
        return render_template("ipinfo.html", data={"error": "Invalid IP address!"})
    
    data = fetch_ip_info(ip)
    return render_template("ipinfo.html", data=data)

# Vercel requires the app to be exposed like this
app = app
