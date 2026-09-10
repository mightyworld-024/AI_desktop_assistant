import os


def shutdown_system():

    os.system("shutdown /s /t 5")

    return "Shutting down the system in 5 seconds."


def restart_system():

    os.system("shutdown /r /t 5")

    return "Restarting the system in 5 seconds."


def cancel_shutdown():

    os.system("shutdown /a")

    return "Shutdown cancelled."