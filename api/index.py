from flask import Flask, render_template, abort
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
        return {"error": f"Gagal mengambil data IP: {e}"}
    except Exception as e:
        return {"error": f"Terjadi kesalahan: {e}"}

@app.route('/')
def my_ip_info():
    data = fetch_ip_info()
    return render_template("ipinfo.html", data=data)

@app.route('/<ip>')
def show_ip_info(ip):
    if not is_valid_ip(ip):
        return render_template("ipinfo.html", data={"error": "IP address tidak valid!"})
    
    data = fetch_ip_info(ip)
    return render_template("ipinfo.html", data=data)

# Vercel pakai `app` dari sini
app = app
