sed -i 's|${POSTGRES_SERVER}|'"$POSTGRES_SERVER"'|' ./Dockerfile
sed -i 's|${POSTGRES_USER}|'"$POSTGRES_USER"'|' ./Dockerfile
sed -i 's|${POSTGRES_PASSWORD}|'"$POSTGRES_PASSWORD"'|' ./Dockerfile
sed -i 's|${POSTGRES_DB}|'"$POSTGRES_DB"'|' ./Dockerfile
sed -i 's|${POSTGRES_DATABASE_URI}|'"$POSTGRES_DATABASE_URI"'|' ./Dockerfile
sed -i 's|${DATASOURCE}|'"$DATASOURCE"'|' ./Dockerfile