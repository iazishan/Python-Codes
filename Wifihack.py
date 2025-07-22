import subprocess

# Get the list of Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

profiles = []
for line in data:
    if "All User Profile" in line:
        profile = line.split(":")[1].strip()
        profiles.append(profile)

# Print each profile and its password (if available)
for profile in profiles:
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    password = None
    for line in result:
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            break
    print(f"Profile: {profile}, Password: {password}")