import subprocess
import requests
import os
import argparse

parser = argparse.ArgumentParser(
                    prog='RegSoundEditor',
                    description='Change Windows Sounds to one Specific sound using the registry.')

parser.add_argument('--set_default', default="1", required=False)
parser.add_argument('--url', default='https://github.com/mario872/windows-sound-bulk-changer/raw/main/beep-example.wav', required=False)

args = parser.parse_args()

home = os.path.expanduser('~')

with open(f'{home}\\Downloads\\beep.wav', 'wb') as beep_file:
    beep_file.write(requests.get(args.url).content)

new_sound_path = f'{home}\\Downloads\\beep.wav'

default_values = {'.Default': '%SystemRoot%/media/Windows Background.wav', 'Close': '', 'CriticalBatteryAlarm': 'C:/WINDOWS/media/Windows Foreground.wav',
                  'DeviceConnect': 'C:\\WINDOWS\\media\\Windows Hardware Insert.wav', 'DeviceDisconnect': 'C:\\WINDOWS\\media\\Windows Hardware Remove.wav',
                  'LowBatteryAlarm': 'C:\\WINDOWS\\media\\Windows Background.wav', 'Maximize': '', 'MessageNudge': 'C:\\WINDOWS\\media\\Windows Message Nudge.wav',
                  'Minimize': '', 'Notification.Default': 'C:\\WINDOWS\\media\\Windows Notify System Generic.wav', 'RestoreDown': '', 'RestoreUp': '',
                  'SystemAsterisk': 'C:\\WINDOWS\\media\\Windows Background.wav', 'SystemExclamation': 'C:\\WINDOWS\\media\\Windows Background.wav',
                  'SystemHand': 'C:\\WINDOWS\\media\\Windows Foreground.wav', 'SystemNotification': 'C:\\WINDOWS\\media\\Windows Background.wav',
                  'WindowsUAC': 'C:\\WINDOWS\\media\\Windows User Account Control.wav'}

new_values = {'.Default': new_sound_path, 'Close': '', 'CriticalBatteryAlarm': new_sound_path, 'DeviceConnect': new_sound_path, 'DeviceDisconnect': new_sound_path,
              'LowBatteryAlarm': new_sound_path, 'Maximize': new_sound_path, 'MessageNudge': new_sound_path, 'Minimize': new_sound_path, 'Notification.Default': new_sound_path,
              'RestoreDown': new_sound_path, 'RestoreUp': new_sound_path, 'SystemAsterisk': new_sound_path, 'SystemExclamation': new_sound_path, 'SystemHand': new_sound_path,
              'WindowsUAC': new_sound_path}

if args.set_default == "1":
    values = default_values
else:
    values = new_values

def pshell(cmd: str):
    full_cmd = f'powershell -c \"{cmd}\"'
    print(full_cmd)
    subprocess.run(full_cmd, shell=True)
    

for value in values.keys():
    cmd = f'set-itemproperty -path \\\"registry::HKCU\\AppEvents\\Schemes\\Apps\\.Default\\{value}\\.Current\\\" -name \\\"(Default)\\\" -value \\\"{values[value]}\\\"'
    pshell(cmd)
#print(cmd)    
