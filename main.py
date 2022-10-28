import subprocess

print("Welcome to the development build of r34 downloader!")
print('Please select the type of content you want')
print('For r34 site enter the number 1')
mediasourcechoice = input('')
if mediasourcechoice == "1":
    subprocess.call('r34.py', cwd='src', shell=True)
else:
    print("ok bye")