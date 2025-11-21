Step 1: Build the Docker Image

Once you have created the Dockerfile, navigate to the directory where the Dockerfile is located and run the following command to build the Docker image:

docker build -t gemini-cli-container .


This command will build the Docker image with the tag gemini-cli-container.

Step 2: Run the Docker Container

Once the image is built, you can run the Docker container like this:

docker run -it gemini-cli-container


The -it flags allow you to interact with the container via the terminal. Since we set gemini-cli --help as the default command in the Dockerfile, this will show the help text for gemini-cli inside the container.

If you want to run a specific command with gemini-cli inside the container, you can override the default command as follows:

docker run -it gemini-cli-container gemini-cli <your-command-here>


For example, to list some gemini resources (assuming gemini-cli supports this):

docker run -it gemini-cli-container gemini-cli list

Step3 (Optional): Persistent Volume (Optional)

If you need to persist data from gemini-cli or mount files from your host system into the container, you can use Docker volumes. For example:

docker run -it -v /path/to/host/directory:/app gemini-cli-container


This command will mount the /path/to/host/directory on your local machine to /app inside the container.
