#!/bin/sh

APP_DIR=/app                                                           # current application directory

export PYTHONPATH="${PYTHONPATH}:${APP_DIR}"

echo "Starting project as `whoami`"
# Activate the virtual environment

cd ${APP_DIR} || exit

echo "Waiting for Postgres database..."
until PGPASSWORD=${POSTGRES_PASSWORD} psql -h "db" -U "${POSTGRES_USER}" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Established database connection."

echo "Migrating..."
python manage.py makemigrations
python manage.py migrate
echo "Done."

echo "Flushing database (just to be sure there are no surprises)..."
python manage.py flush --noinput
echo "Done."

echo "Starting dev server..."
exec python manage.py runserver_plus 0.0.0.0:8000
echo "Done."
