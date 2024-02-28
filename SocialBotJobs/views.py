from django.shortcuts import redirect, render
import requests
from SocialBotJobs.forms import LoginForm, RegistrationForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import RegistrationForm

# login view
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("Redirecting to index")
            return redirect("index2")
    else:
        form = LoginForm()
    return render(request, "Authentication/login.html", {"form": form})

# sign up view
class SignupView(View):
    template_name = "Authentication/register.html"

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("login")
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")

            print(f"Form data: {request.POST}")

            return render(request, self.template_name, {"form": form})

# logout view
def logout_view(request):
    logout(request)
    return redirect("login")

# main page
def index2(request):
    return render(request, "index2.html")

#add_proxy
def add_proxy(request):
    return render(request, "add_proxy.html")

# social module page
def tiktok_module_page(request):
    return render(request, "tiktok_module_base.html")

def insta_module_page(request):
    return render(request, "insta_module_base.html")

# add_automation_profile
def add_automation_profiles(request):
    return render(request, "add_automation_profile.html")

# log page
def log(request):
    return render(request, "log.html")

# batch page
def batch(request):
    return render(request, "batch.html")

# profile view
def profile(request):
    api_url = "https://7159-2400-adc5-491-1500-18bd-e7c3-5a81-a222.ngrok-free.app/sessionbot/api/resource/profile/"
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        profiles = response.json()

        return render(request, "profile.html", {"profiles": profiles["results"]})
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching profile data: {str(e)}"
        return render(request, "profile.html", {"error_message": error_message})

# SMSPVA page
def AntiCap(request):
    return render(request, "Anti-Captcha.html")

# SMSPVA page
def SMSPVA(request):
    return render(request, "SMSPVA.html")

# Automation Task page
def AutomationTask(request):
    return render(request, "AutomationTask.html")

# available server
def available_server(request):
    api_url = "https://7159-2400-adc5-491-1500-18bd-e7c3-5a81-a222.ngrok-free.app/sessionbot/api/resource/server/"
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        servers = response.json()

        return render(request, "available_server.html", {"servers": servers["results"]})
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching server data: {str(e)}"
        return render(request, "available_server.html", {"error_message": error_message})


def available_proxies(request):
    return render(request, "available_proxies.html")

def add_device(request):
    return render(request, "add_device.html")

def add_server(request):
    return render(request, "add_server.html")

def add_profile_via_excel_sheet(request):
    if request.method == "POST" and "add_proxies" in request.POST:
        google_sheets_url = request.POST.get("google_sheets_url")
        creds_file_path = "D:\\NorthRaysWebsite\\vividmind-408110-57338752d236.json"

        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_path, scope)
            client = gspread.authorize(creds)
            sheet = client.open_by_url(google_sheets_url).get_worksheet(0)

            records = sheet.get_all_records()

            for record in records:
                bot_records = {
                    "action": record.get("action", ""),
                    "spreadsheet_url": record.get("spreadsheet_url", ""),
                    "resource_type": record.get("resource_type", ""),
                }

                sessionbot_ngrok_url = "https://7159-2400-adc5-491-1500-18bd-e7c3-5a81-a222.ngrok-free.app/"
                sessionbot_endpoint = "sessionbot/api/resource/create/"
                sessionbot_url = sessionbot_ngrok_url + sessionbot_endpoint

                try:
                    payload = bot_records
                    response = requests.post(sessionbot_url, json=payload)
                    response.raise_for_status()

                    response_data = response.json()
                    

                except requests.RequestException as e:
                    error_message = f"Error sending data to SESSIONBOT: {e}"
                    print(error_message)

        except Exception as e:
            error_message = f"Error accessing Google Sheets: {e}"
            print(error_message)

    return render(request, "add_automation_profile.html")

# Available devices
def available_devices(request):
    api_url = "https://7159-2400-adc5-491-1500-18bd-e7c3-5a81-a222.ngrok-free.app/sessionbot/api/resource/device/"
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        devices = response.json()

        return render(request, "available_devices.html", {"devices": devices["results"]})
    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching device data: {str(e)}"
        return render(request, "available_devices.html", {"error_message": error_message})



# add device via excel
def add_device_via_excel_sheet(request):
    if request.method == "POST" and "add_proxies" in request.POST:
        google_sheets_url = request.POST.get("google_sheets_url")
        creds_file_path = "D:\\NorthRaysWebsite\\vividmind-408110-57338752d236.json"

        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_path, scope)
            client = gspread.authorize(creds)
            sheet = client.open_by_url(google_sheets_url).get_worksheet(0)

            records = sheet.get_all_records()

            for record in records:
                device_records = {
                    "action": record.get("action", ""),
                    "spreadsheet_url": record.get("spreadsheet_url", ""),
                    "resource_type": record.get("resource_type", ""),
                }

                print(device_records)

                sessionbot_ngrok_url = "https://7159-2400-adc5-491-1500-18bd-e7c3-5a81-a222.ngrok-free.app/"
                sessionbot_endpoint = "sessionbot/api/resource/create/"
                sessionbot_url = sessionbot_ngrok_url + sessionbot_endpoint

                try:
                    payload = device_records
                    response = requests.post(sessionbot_url, json=payload)
                    response.raise_for_status()

                    response_data = response.json()
                    print(response_data)
                    

                except requests.RequestException as e:
                    error_message = f"Error sending data to SESSIONBOT: {e}"
                    print(error_message)

        except Exception as e:
            error_message = f"Error accessing Google Sheets: {e}"
            print(error_message)

    return render(request, "add_device.html")


def add_server_via_excel_sheet(request):
    if request.method == "POST" and "add_proxies" in request.POST:
        google_sheets_url = request.POST.get("google_sheets_url")
        creds_file_path = "D:\\NorthRaysWebsite\\vividmind-408110-57338752d236.json"

        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_path, scope)
            client = gspread.authorize(creds)
            sheet = client.open_by_url(google_sheets_url).get_worksheet(0)

            records = sheet.get_all_records()

            for record in records:
                server_records = {
                    "action": record.get("action", ""),
                    "spreadsheet_url": record.get("spreadsheet_url", ""),
                    "resource_type": record.get("resource_type", ""),
                }

                print(server_records)

                sessionbot_ngrok_url = "https://7159-2400-adc5-491-1500-18bd-e7c3-5a81-a222.ngrok-free.app/"
                sessionbot_endpoint = "sessionbot/api/resource/create/"
                sessionbot_url = sessionbot_ngrok_url + sessionbot_endpoint

                try:
                    payload = server_records
                    response = requests.post(sessionbot_url, json=payload)
                    response.raise_for_status()

                    response_data = response.json()
                    print(response_data)
                    

                except requests.RequestException as e:
                    error_message = f"Error sending data to SESSIONBOT: {e}"
                    print(error_message)

        except Exception as e:
            error_message = f"Error accessing Google Sheets: {e}"
            print(error_message)

    return render(request, "add_server.html")