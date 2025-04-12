### 📡 Flask IP Info Checker

A simple and lightweight web application built with **Flask** to display public IP address information — whether it's your own or a specific IP input by the user.

🔎 **Features:**
- Get your own public IP info at `/`
- Check any IP address at `/<ip>`
- IP address validation included
- Clickable elements:
  - **ASN** → Redirects to [ipinfo.io](https://ipinfo.io) ASN details
  - **IP Network** → Redirects to subnet range (e.g., `/ips/103.242.104.0/24`)
  - **Coordinates** → Opens location in Google Maps

📦 **Built With:**
- Python + Flask
- `requests` for API integration with [ipinfo.io](https://ipinfo.io)
- Simple responsive HTML template

🚀 **Deployment:**
- Ready to deploy on [Vercel](https://vercel.com) using `@vercel/python` runtime
- Auto-deployment via GitHub integration

---

### 🌐 Example Usage

```bash
# Your own IP info:
https://ipinfo.kontrakita.web.id

# Specific IP info:
https://ipinfo.kontrakita.web.id/8.8.8.8
```

---

### 📁 Project Structure
```
.
├── api/
│   └── index.py         # Main Flask application
├── templates/
│   └── ipinfo.html      # HTML view
├── requirements.txt     # Python dependencies
└── vercel.json          # Vercel deployment config
```