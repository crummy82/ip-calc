# ip-calc
## My own python IP Subnet Calculator
### This simple web app has 3 functions:
- Show you the details of an IP address (is it a loopback, private, etc.)
- Show you the details of a network based on a network IP and prefix
- Show you the details of a subnet based on any given IP with prefix

The output is then given directly below the input box

Demo server - [my-calc.crummynet.net](https://my-calc.crummynet.net)

### To deploy
1. Clone the repo to a folder you will run the docker compose command from
2. Edit the compose.yml file for any changes needed (http listen port, etc.)
3. Run "docker compose up -d" to build the site and run the Flask web server with the IP Calculator 

### To update
1. Edit any files in the app folder (site template edits, etc.)
2. Run "docker compose down" to bring down the site
3. Run "docker image rm ip-calc-web" to remove the old image
4. Run "docker compose up -d" to build the new site and run the web server 

*Note that this runs the Flask development server for simplicity and not a production-ready WSGI server backend*
