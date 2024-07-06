import yaml
import click
import htpasswd
from pprint import pprint

# TODO: pass len
# TODO: check if user.db exists
# TODO: verbose pprint
# TODO: delete
# TODO: different compose files


def get_compose(compose_name):
    with open(compose_name, 'r') as file_descriptor:
        compose_file = yaml.safe_load(file_descriptor)
    file_descriptor.close()
    return compose_file

def htpasswd_gen(user, password):
    with htpasswd.Basic("user.db", mode='md5') as userdb:
        try:
            userdb.add(user, password)
        except htpasswd.basic.UserExists:
            answer = input("User exits, want to change password [Y/N]? ").lower()
            if answer == 'y':
                userdb.change_password(user, password)
    with open("user.db", "r") as userdb_read:
        for line in userdb_read.readlines():
            line_user = line.split(':')[0]
            if line_user == user:
                return line.strip("\n")
        else:
            print('Error in htpasswd_gen')
            exit(2)


def pass_check(password, confirm):
    pass_len = 4
    if password != confirm:
        click.echo("Password didnt match!")
        return False
    if len(password) < pass_len: # TODO: change pass len
        click.echo("Password too short! Must be longer than {}".format(pass_len))
        return False
    return True


@click.command()
@click.option("--file", default="docker-compose.yml", help="Docker-compose file name")
@click.option("--action", default="add", help="Add/Delete")
@click.option("--user", help="Username")
@click.option("--password", prompt="Password", help="prompt password", hide_input=True)
@click.option("--confirm", prompt="Confirm", help="prompt password", hide_input=True)
def main(file, action, user, password, confirm):
    domain = 'example.com'
    service = {'image': '2xnone/study:gotty',
        'labels': [
            'traefik.frontend.auth.basic.users='
            'traefik.frontend.rule=',
            'traefik.enable=true',
            'traefik.port=80',
        ],
        'restart': 'always',
        'volumes': ['./gotty.conf:/root/.gotty']
    }

    admin = "shellshock:$$apr1$$WFsfykJx$$XDyyif9VZqIQHWptk0om5/"
    if not pass_check(password, confirm): exit(1)


    compose = get_compose(file)
    click.echo("[{}] Going to *{}* {}".format(file, action, user))

    hash_password = htpasswd_gen(user, password).replace('$', '$$')


    service_password =  'traefik.frontend.auth.basic.users=' + admin + ',' + hash_password
    service_host =      'traefik.frontend.rule=Host:' + '{}.'.format(user) + domain

    service["labels"][0] = service_password
    service["labels"][1] = service_host
    pprint(service)

    if user in compose["services"]:
        click.echo("[{}] {} exits".format(file, user))
    compose["services"][user] = service

    with open(file, 'w') as compose_file:
        yaml.dump(compose, compose_file, default_flow_style=False)


if __name__ == "__main__":
    main()
