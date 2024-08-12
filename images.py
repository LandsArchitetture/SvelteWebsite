import io
import os
import paramiko
import requests
import json
import shutil
import googletrans
import deepl


HOST = os.environ["HOST"]
USERNAME = os.environ["USERNAME"]
SSH = os.environ["SSH2"]
PASSWORD = os.environ["PASSWORD"]
DEEPL_KEY = os.environ["DEEPL_KEY"]
SSH_KEY = paramiko.RSAKey.from_private_key(io.StringIO(SSH), password=PASSWORD)

API = "https://admin.lands.swiss"
REMOTE_DIR = "www/free-lands.com"
DIRECTORY = "images"
TRANSLATIONS_FILE = "Translations.json"

LANGUAGES = ["en-US", "it-IT"]

LANGUAGES_CODES = {"en-US": "EN", "it-IT": "IT"}

def get_files_images_ids_in_remote():
    _, stdout, _ = ssh.exec_command(f"ls {REMOTE_DIR}")
    files = stdout.read().decode().splitlines()
    return files


def get_translations_file_in_remote():
    _, stdout, _ = ssh.exec_command(f"cat {REMOTE_DIR}/{TRANSLATIONS_FILE}")
    files = stdout.read().decode("utf-8")
    return files


def translate_text_google(text, target_language):
    translator = googletrans.Translator()
    translated = translator.translate(text, target_language)
    return translated.text


def translate_text_deepl(text, target_language):
    translator = deepl.Translator(DEEPL_KEY)
    language_code = LANGUAGES_CODES[target_language]

    result = translator.translate_text(text, target_lang=language_code)
    return result.text


# Connect to remote server

print("Connecting to FREELANDS ...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USERNAME, pkey=SSH_KEY)
print("Connected to FREELANDS")

# Open SFTP session

sftp = ssh.open_sftp()
print("Opened SFTP session")

# Get images and posts from Directus

files = requests.get(f"{API}/files", params={"limit": -1}).text
posts = requests.get(f"{API}/items/posts", params={"limit": -1}).text
print("Got images and posts from DIRECTUS")

# Generate posts ids array

IDS_FILES = []
for _, image in enumerate(json.loads(files)["data"]):
    IDS_FILES.append(image["id"])
print(f"Generated posts ids array: {IDS_FILES}")

# check that remote directory exists

sftp.stat(REMOTE_DIR)

# List of fileimage_ids already in the remote dir

already_there = get_files_images_ids_in_remote()

translations = {
    "AboutUs": {
        "Profession": {"en-US": "Architect"},
        "Description": {"en-US": "Owner of the LANDS architecture laboratory"},
        "Introduction": {
            "en-US": "LANDS is an architecture laboratory. It is based in Lugano, a city on the edge of a beautiful lake and surrounded by mountains. We are motivated, capable and passionate people. We work within, between, and with the following words"
        },
        "Environment": {"en-US": "Environment"},
        1: {
            "en-US": "We build it, consciously or not, every day. It was once called Nature."
        },
        "Architecture": {"en-US": "Architecture"},
        2: {
            "en-US": "Every definition of architecture today is obsolete and every attempt to harness it in codes. Architecture can only be researched. Sometimes it offers itself, for a strange set of circumstances, others it escapes."
        },
        "City": {"en-US": "City"},
        3: {
            "en-US": "Is a collection of buildings and citizens. It takes both to make a living city."
        },
        "Competitions": {"en-US": "Competitions"},
        4: {"en-US": "Are useful project tools, if their purpose is not ideological."},
        "Construction": {"en-US": "Construction"},
        5: {
            "en-US": "Is the technological ability to think and develop projects. The true knowledge of the architect."
        },
        "Culture": {"en-US": "Culture"},
        6: {
            "en-US": "Is the care, of the Earth, on which we live. But do we still have an Earth culture?"
        },
        "Economy": {"en-US": "Economy"},
        7: {"en-US": "Still and always the house ... it is the DNA of our times."},
        "Edifice": {"en-US": "Edifice"},
        8: {
            "en-US": "Is the construction of man's dwelling on Earth. In a landscape. Each building is unique."
        },
        "Building": {"en-US": "Building"},
        9: {
            "en-US": "Is the complex of human activities related to the construction of buildings."
        },
        "Hybrid": {"en-US": "Hybrid"},
        10: {
            "en-US": "Is the state of affairs of the contemporary world. Architecture is hybrid, never pure. The construction as well."
        },
        "Innovation": {"en-US": "Innovation"},
        11: {"en-US": "Could it be our personal ability to respond to real problems?"},
        "Landscape": {"en-US": "Landscape"},
        12: {
            "en-US": "It was not there before, now it is determined by man's footprints on Earth and by his gaze."
        },
        "Projects": {"en-US": "Projects"},
        13: {
            "en-US": "Are a look ahead and therefore the process that leads to the construction of an artifact. Without a vision of the world, one cannot design."
        },
        "Renovations": {"en-US": "Renovations"},
        14: {
            "en-US": "Is the remodeling of an artifact. The main activity of the 21st century. Renovating the buildings, the city ... the whole world."
        },
        "Valuation": {"en-US": "Valuation"},
        15: {
            "en-US": "Is the giving of value to things and turning them into money. Strength without which it makes no sense to talk about this profession."
        },
        "Society": {"en-US": "Society"},
        16: {
            "en-US": "Today is the largest transformation taking place since the Neolithic. But has man always been the same?"
        },
        "Technique": {"en-US": "Technique"},
        17: {
            "en-US": "Is the quality of our daily life. Our DNA is technical. We live technically."
        },
        "3333": {"en-US": "3333"},
        18: {
            "en-US": "Our first project for a low-cost residential building. Architecture for everyone!"
        },
        "Recap": {
            "en-US": "From this small office, in a small town on the edge of the world, we are lucky enough to have an open mind. Our daily work, which takes place thanks to our clients, allows us to create buildings that have a single ultimate purpose: to make the life of those who live there happy. How to build them is our humble profession."
        },
    },
    "Navbar": {
        "Projects": {"en-US": "Projects"},
        "About": {"en-US": "About"},
        "Competitions": {"en-US": "Competitions"},
        "Buildings": {"en-US": "Buildings"},
        "Miscellaneous": {"en-US": "Miscellaneous"},
        "About us": {"en-US": "About us"},
        "Contact": {"en-US": "Contact"},
        "Language": {"en-US": "Language"},
        "Search": {"en-US": "Search"},
    },
}

try:
    old_translations = json.loads(get_translations_file_in_remote())
except Exception as e:
    print(e)
    old_translations = {}

print("Initialized translations dictionary")

os.makedirs(DIRECTORY)

########################################################################
# NAVBAR AND ABOUT US TRANSLATIONS
########################################################################

print("Translating navbar and about us ...")
for location in translations:
    for identifier in translations[location]:
        for language in filter("en-US".__ne__, LANGUAGES):
            text = translations[location][identifier]["en-US"]
            # print(f'{location}, {identifier}, {language} : {text}')
            if (
                location in old_translations
                and identifier in old_translations[location]
                and language in old_translations[location][identifier]
            ):
                translations[location][identifier][language] = old_translations[
                    location
                ][identifier][language]
            else:
                translations[location][identifier][language] = translate_text_deepl(
                    text, language
                )
            print(f"Translated {identifier} in {language}")
print("Translated all necessary words")

# Create the translation file and add all the translations

print("Creating the translation file ...")
with open(f"{DIRECTORY}/Translations.json", "w") as json_file:
    json.dump(translations, json_file, indent=4)
print("Translation file created")

# Send the file to the free-lands DB

print("Transferring translation file to FREELANDS ...")
local_path2 = os.path.join(DIRECTORY, TRANSLATIONS_FILE)
remote_path2 = os.path.join(REMOTE_DIR, TRANSLATIONS_FILE)
sftp.put(local_path2, remote_path2)
print("Transferred translations file to FREELANDS")

########################################################################
# POSTS TRANSLATIONS
########################################################################

print("Downloading all posts and transfering them to FREELANDS...")
for post in json.loads(posts)["data"]:
    image_id = post["image"]
    size = post["size"]
    text = post["text"]
    id = post["id"]
    index = IDS_FILES.index(image_id)
    file = json.loads(files)["data"][index]
    width = file["width"]
    height = file["height"]

    # flip if horizontal
    if height > width:
        size = size[::-1]

    # Add right size of the image to the database
    if f"{image_id}_{size}.jpeg" not in already_there:

        image = requests.get(f"{API}/assets/{image_id}?key={size}")

        if image.status_code:
            with open(f"{DIRECTORY}/{image_id}_{size}.jpeg", "wb") as photo:
                photo.write(image.content)

        print(f"Downloaded image: {image_id}_{size}.jpeg")

        local_path1 = os.path.join(DIRECTORY, f"{image_id}_{size}.jpeg")
        remote_path1 = os.path.join(REMOTE_DIR, f"{image_id}_{size}.jpeg")
        sftp.put(local_path1, remote_path1)

        print(f"Transferred image: {image_id}_{size}.jpeg to FREELANDS")

    # Add modal version of the image to the database
    if f"{image_id}_modal.jpeg" not in already_there:

        image = requests.get(f"{API}/assets/{image_id}?key=modal")

        if image.status_code:
            with open(f"{DIRECTORY}/{image_id}_modal.jpeg", "wb") as photo:
                photo.write(image.content)

        print(f"Downloaded image: {image_id}_modal.jpeg")

        local_path2 = os.path.join(DIRECTORY, f"{image_id}_modal.jpeg")
        remote_path2 = os.path.join(REMOTE_DIR, f"{image_id}_modal.jpeg")
        sftp.put(local_path2, remote_path2)

        print(f"Transferred image: {image_id}_modal.jpeg to FREELANDS")
print("Transferred all necessary images to FREELANDS")

shutil.rmtree(DIRECTORY)

# Close SFTP session and SSH connection
sftp.close()
ssh.close()