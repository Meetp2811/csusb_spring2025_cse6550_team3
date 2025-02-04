## Prerequisites
Install the following before you begin:  
   [Git](https://git-scm.com/)  
   [Docker](https://www.docker.com/)  

## To create a simple, Dockerized web application:
1) Clone this GitHub repository
```
git clone https://github.com/DrAlzahraniProjects/csusb_spring2025_cse6550_team3.git
```
2) Navigate to the repository
```
cd csusb_spring2025_cse6550_team3 
```
3) Ensure repository is updated to the latest version
```
git pull origin main
```
4) Build the docker image
```
docker build -t team3s25-app .
```
5) Run the docker image
```
docker run -d -p 2503:2503 -p 8888:8888 team3s25-app
```
6) Follow the following links to access the app:  
App - http://127.0.0.1:2503/  
Jupyter - http://127.0.0.1:8888/  
   *For now, the token required for Jupyter is: token*
