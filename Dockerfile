# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

# EXPOSE port 80 to allow communication to/from server
EXPOSE 80

# set correct permision for start script
RUN chmod +x start.sh

# CMD specifcies the command to execute to start the server running.
CMD ["./start.sh"]
# done!