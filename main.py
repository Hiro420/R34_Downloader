import subprocess

print("Welcome to the development build of r34 downloader!")
print('Please select the type of content you want')
print('For r34 site enter the number 1')
print('For downloading from discord nsfw channels enter the number 2')
print('Just letting you know that discord downloading is more complicated because fuck discord')
mediasourcechoice = input('')
if mediasourcechoice == "1":
    subprocess.call('r34.py', cwd='src', shell=True)
elif mediasourcechoice == "2":
    subprocess.call('discord.py', cwd='src', shell=True)
else:
    print("ok bye")