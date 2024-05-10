import requests

def get_version(router_ip):
    try:
        url = f"http://{router_ip}/index.html"
        response = requests.get(url)
        if response.status_code == 200:
            version_start_index = response.text.index("Firmware Version: ")
            if version_start_index != -1:
                version_start_index += len("Firmware Version: ")
                version_end_index = response.text.find("<", version_start_index)
                version = response.text[version_start_index:version_end_index].strip()
                return version
            else:
                return "Version not found"
        else:
            return f"error status code: {response.status_code}"
    except Exception as e:
        return f"error getting version: {e}"
router_ip = input("Enter router ip address: ")
print("Checking version...")
version = get_version(router_ip)
print(f"Version: {version}")