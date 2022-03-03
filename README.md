# concordia
## Description coming soon

### Getting started
1. Stop any serices on host machine that use ports 80 or 5432 (such as apache2, postgresql) e.g. `service apache2 stop`
2. Run `docker-compose up -d --build`
3. Create the database schema using the provided script `docker-compose exec web python create_db.py`
4. Inspect the DB server to verify that tables have been created successfully `docker-compose exec db psql -U postgres --dbname=site_db`
5. Verify that the volume has been created `docker volume inspect flask-template_db_data`
6. For use in production, set environment variables in `env.prod` and then set that file as the `env_file` for the web and db containers in `docker-compose.yml`

Finally, set the Nginx image to a specific verison in the nginx docker file to avoid upsteam changes breaking the build.
