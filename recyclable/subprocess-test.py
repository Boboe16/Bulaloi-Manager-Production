import subprocess
import os
import json

# Clone the repo and run `npm install` in its directory DONEEE
# first command execute `npm install` inside the repo
# command = subprocess.run(['git', 'clone', 'https://github.com/Boboe16/Bulaloi-App-Development-Experiment', '&&', 'cd', 'Bulaloi-App-Development-Experiment/next-app', "&&", "npm", "install"], shell=True, capture_output=True, text=True)
# second command doesn't (this is faster, try this method first)
if os.path.exists('./Bulaloi-App-Development-Experiment'):
    print("Repo already cloned, skipping clone step")
else:
    print("Cloning repo...")
    subprocess.run(['git', 'clone', 'https://github.com/Boboe16/Bulaloi-App-Development-Experiment', '&&', 'cd', 'Bulaloi-App-Development-Experiment/next-app'], shell=True, capture_output=True, text=True)


# Run `npm run dev`
# command = subprocess.run(['cd', 'Bulaloi-App-Development-Experiment/next-app', "&&", "npm", "run", "dev"], shell=True, capture_output=True, text=True)

# print(command.stdout)
# print(command.returncode)
# print(command.stderr)

# It seems we will have to use && to run syncnronous operation of commands in subprocess

# Create a replica of "Bulaloi-App-Development", add "-Experiment" at the last character  DONEEEE
# then create it as github repo DONEEE
# then clone it and use it with subprocess test DONE


# next is adding/deleting/updating new file to the repo and pushing it
# dirToEdit = 'Bulaloi-App-Development-Experiment/next-app/public/apps-games-data/apps'


#Checks the dir
# command = subprocess.run(['cd', dirToEdit, "&&", 'dir'], shell=True, capture_output=True, text=True)


# Read json files, parse each of them and put them in array


# Create json files in `apps` directory. DONEEE
# We could use `class` to create objects and just convert them into json then create it
# class AppOrGame:
#     def __init__(self, appOrGame, appPicture, appName, appRating, appDownloadLink, appDescription, appCategory, appVersion=None, appRequirement=None, appSize=None):
#         self.appOrGame = appOrGame
#         self.appPicture = appPicture
#         self.appName = appName
#         self.appRating = appRating
#         self.appDownloadLink = appDownloadLink
#         self.appDescription = appDescription
#         self.appCategory = appCategory
#         self.appVersion = appVersion
#         self.appRequirement = appRequirement
#         self.appSize = appSize
   
# new_data = AppOrGame(
#     appOrGame="Game",
#     appPicture="http://example.com/picture.jpg",
#     appName="Super Fun Game",
#     appRating="4.5",
#     appDownloadLink="http://example.com/download",
#     appDescription="An exciting adventure game.",
#     appCategory="Adventure",
#     appVersion="1.0.2",
#     appRequirement="Android 4.0+",
#     appSize="100MB"
# )

# print(new_data.__dict__)

# directory_path = r'\Users\richill rectin\Documents\doc\pyqt6 app\Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps'

# filename = 'app_data.json'

# full_path = os.path.join(directory_path, filename)

# with open(full_path, 'w') as file:
#     json.dump(new_data.to_dict(), file, indent=4)


# Modify json file DONEEE
# with open('app_data.json', 'r') as file:
#     data = json.load(file)

# def modifyJson(appOrGameValue=None, appPictureValue=None, appNameValue=None, appRatingValue=None, 
#                appDownloadLinkValue=None, appDescriptionValue=None, appCategoryValue=None, 
#                appVersionValue=None, appRequirementValue=None, appSizeValue=None):
    
#     def argumentHasValue(property=None, argument=None):
#         if argument:
#             data[property] = argument

#     argumentHasValue("appOrGame", appOrGameValue) 
#     argumentHasValue("appPicture", appPictureValue)
#     argumentHasValue("appName", appNameValue)
#     argumentHasValue("appRating", appRatingValue)
#     argumentHasValue("appDownloadLink", appDownloadLinkValue)
#     argumentHasValue("appDescription", appDescriptionValue)
#     argumentHasValue("appCategory", appCategoryValue)
#     argumentHasValue("appVersion", appVersionValue)
#     argumentHasValue("appRequirement", appRequirementValue)
#     argumentHasValue("appSize", appSizeValue)

# modifyJson(appNameValue="Not a fun game anymore", appDownloadLinkValue="asdassdsadsads")

# with open('app_data.json', 'w') as file:
#     json.dump(data, file, indent=4)


# Delete json file DONEEE
# jsonFileToDelete = 'Paypal.json'
# command = subprocess.run(['cd', dirToEdit, "&&", 'del', jsonFileToDelete], shell=True, capture_output=True, text=True)


# Now iterate list of json file names and delete them.  DONEEE
# dir = os.path.join(r'.\Bulaloi-App-Development-Experiment\next-app\public\apps-games-data\apps')
# jsonFilesToDelete = ['Paypal.json', 'Orgzly.json', 'Rar.json']

# for json in jsonFilesToDelete:
#     command = subprocess.run(['cd', dir, "&&", 'del', json], shell=True, capture_output=True, text=True)

#     print(command.stdout)
#     print(command.returncode)
#     print(command.stderr)

# The logic of deleting apps & games will be based on the checked boxes of apps names.
# Ex: You check a checkbox(es) the checkbox(es)'s name(s) will be put in an array
# Ex: If you uncheck a checked checkbox its name will be deleted in the array
# Ex: Now if you clicked the `delete button`, a message with text `Do you want to continue` will appear with options `Yes` & `No`

# after creating json files do git add/commit/push DONEEE

# directory_path = r'.\Bulaloi-App-Development-Experiment'

# full_path = os.path.join(directory_path)

# command = subprocess.run(['cd', full_path, '&&', 'dir', '/a:h', '&&', 'git', 'add', '.', '&&', 'git', 'commit', '-m', '"taeeee"', '&&', 'git', 'push', 'origin', 'main'], shell=True, capture_output=True, text=True)

# print(command.stdout)
# print(command.returncode)
# print(command.stderr)