from flask import Flask, render_template, request
import requests
import ipaddress
import socket
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def resolve_domain_to_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

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
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    data = fetch_ip_info(user_ip)
    return render_template("ipinfo.html", data=data)

@app.route("/ip")
def ip_lookup():
    query = request.args.get("query")
    if query:
        return redirect(f"/{query}")
    # kalau tidak ada query, pakai IP client
    user_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    return redirect(f"/{user_ip}")

@app.route('/<target>')
def show_ip_info_or_domain(target):
    ip = None
    domain_resolved = None

    if is_valid_ip(target):
        ip = target
    else:
        resolved_ip = resolve_domain_to_ip(target)
        if resolved_ip:
            ip = resolved_ip
            domain_resolved = target
        else:
            return render_template("ipinfo.html", data={"error": "Invalid IP address or domain!"})

    data = fetch_ip_info(ip)
    if domain_resolved:
        data["domain"] = domain_resolved
    return render_template("ipinfo.html", data=data)

# Needed for Vercel
app = app
