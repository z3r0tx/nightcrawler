FROM python:3.9.4-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Copy the SQL script and the initialization script into the container
COPY scripts/init.sql /docker-entrypoint-initdb.d/
COPY scripts/init.sh /docker-entrypoint-initdb.d/

# Make the scripts executable
RUN chmod +x /docker-entrypoint-initdb.d/init.sql
RUN chmod +x /docker-entrypoint-initdb.d/init.sh

# Run the initialization script when the container starts
CMD ["docker-entrypoint-initdb.d/init.sh"]

EXPOSE 8000

ENV $(cat .env | xargs)

CMD ["scrapy", "crawlall"]
