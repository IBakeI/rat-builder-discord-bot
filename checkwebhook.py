import requests

def validatewebhook(webhook):

    if not webhook.startswith("https://discord.com/api/webhooks") and not webhook.startswith("https://discordapp.com/api/webhooks") and not webhook.startswith("https://canary.discord.com/api/webhooks") and not webhook.startswith("https://ptb.discord.com/api/webhooks") or not webhook.startswith("https://discord.com/api/webhooks"):
        return False
    try:
        check = requests.get(webhook)
        if check.status_code == 404:
            return False
        elif check.status_code == 200:
            return True
    except:
        return