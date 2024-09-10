#!/bin/bash

############################################################
# Help                                                     #
############################################################
Help()
{
    # Display Help
    echo "Run the following commands"
    echo
    echo "Syntax: scripts.sh [-c|h]"
    echo "options:"
    echo "h     Print this Help."
    echo
    echo "arguments:"
    echo "run         Command to run in dev mode"
    echo "docs        Generate docs"
    echo "postgres    Run postgres db"
    echo "redis       Run redis"
    echo "celery      Run celery worker"
    echo "celery_beat Run celery beat"
}

AvailableCommands="""Available commands:
run
docs
postgres
redis
celery
celery_beat
"""

############################################################
# Main program                                             #
############################################################

# Get the options
while getopts ":h" option; do
    case $option in
        h) # display Help
            Help
        exit;;
    esac
done

# continue running if only 1 argument else print invalid argument
if [ $# -eq 1 ]; then
    case $1 in
        run)
            python manage.py runserver --settings=core.settings.development
        ;;
        docs)
            cd docs && make html && cd ..
        ;;
        postgres)
            docker run --name glancefy-postgres -e POSTGRES_DB=glancefy_db -e POSTGRES_USER=glancefy_user -e POSTGRES_PASSWORD=glancefy_password -p 5432:5432 -d postgres:14
        ;;
        redis)
            docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
        ;;
        celery)
            celery -A core worker -l info
        ;;
        celery_beat)
            celery -A core beat -l info
        ;;
        *)
            echo $AvailableCommands
        ;;
    esac
else
    echo $AvailableCommands
fi