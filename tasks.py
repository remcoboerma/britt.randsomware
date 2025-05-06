import invoke.exceptions
from invoke import task
from invoke import Context
from edwh import tasks
from pathlib import Path

#REQUIRED
if not Path(".env").exists():
    with open(Path(".env"), "x") as env_file:
        env_file.close()


context = Context()
check_env = tasks.check_env
generate_password = tasks.generate_password

def voorbeelden(c):
    # Hiermee zet je een .env value "key=value"
    check_env(
        "ENV_NAME/ENV_KEY",
        default="geef hier een default waarde aan. In het geval van geen opgave.",        
        comment="UITLEG OVER DE .env key en value",
    )  

#genereert automatisch een wachtwoord, plaats op de plaats van default, geen ""
#generate_password(nummer=lengte van wachtwoord)
wachtwoord = generate_password(context, 20)


@task
def setup(c):
    try:
        c.sudo("chmod +x captain-hooks/*.sh")
    except invoke.exceptions.AuthFailure:
        print("Execute 'sudo ls' before executing this command!")
        return
    print("nog geen voorbeelden :(")
#plaats op de plaats van de print de check_env per variabele om zo de setup compleet te maken
