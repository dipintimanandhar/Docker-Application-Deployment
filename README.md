# Indian Institute of Technology Jodhpur 
## Virtualization and Cloud Computing
### Assessment-1 : Virtual Machines and Docker
#### Dipinti Manandhar(M20CS020)

##### _Question 2 : Docker Application Deployment_


Web Application: Iris dataset classification web application

---
#### Process followed

In order to deploy docker application, first of all we need to install Docker in our machine. We can download docker from https://www.docker.com/get-started . 
We need to have a full working of a web application so that we can dockerize the app. The step by step process followed is listed below:

1.	Create a new file without extension. Name it as ‘Dockerfile’. (capitalize the letter‘D’)
2.	Then we need to define our base image, from where we want to build our file. The base image I have used is ubuntu20.04 from Docker. We need to define it as: 
``` FROM ubuntu:20.04 ```
3.  To update all the packages of Ubuntu and upgrade them, we will define it as:
  ```RUN apt update && apt -y upgrade```
4.	Then, installing python3 in our image as :
``` RUN apt install -y python3-pip```
5.	Create a requirements.txt file which contains all the required libraries to run the application.
6.	Copy the requirements.txt file from the machine to our Ubuntu base image (i.e from source to destination):
``` COPY requirements.txt ./requirements.txt```
7.	Install the requirements.txt file in the docker image: 
```RUN pip3 install -r requirements.txt```
8.	Then, expose the port to be used for running the application:
```sh
EXPOSE 8501
Overall the Docerfile contains the following commands:
FROM ubuntu:20.04
RUN apt update && apt -y upgrade
RUN apt install -y python3-pip
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
```
By following the above steps, the setup for base image is done and we need to push it to the webserver of dockerhub. By doing so, we can pull it into our own webapplication’s Dockerfile. To do these process, the commands are listed below:
1.	```docker image build –t dipintimanandhar/ubuntum20cs020:v1 .```
Output is shown as:
![1](https://user-images.githubusercontent.com/82838972/131710907-5290bdb0-39a5-43e7-9525-874ebca6ece8.JPG)
2. ```	docker image push dipintimanandhar/ubuntum20cs020:v1```
Output is shown as: 
![2](https://user-images.githubusercontent.com/82838972/131711006-56308b2a-eb86-4835-9ff2-2c35a13a66bb.JPG)
3.	Navigate to the folder to the web application file and created a new Dockerfile and add the following commands:
a.	Pull the webserver image from the dockerhub’s repository
      ```  FROM dipintimanandhar/ubuntum20cs020:v1```
b.	Create a work directory where the server/local host runs
      ```  WORKDIR /app```
c.	For building, copy the entire project into the container
    ```   COPY . .```
d.	Create an entry point to make our image executable
   ```    ENTRYPOINT ["streamlit", "run"]```
    ```   CMD ["Application.py"]```
Overall the Dockerfile should contain the following commands:
```ssh
FROM dipintimanandhar/ubuntum20cs020:v1
WORKDIR /app
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["Application.py"]
```
4.	Build the docker image with the command : ``` build . -t dipinti123```
Output is shown as:
![3](https://user-images.githubusercontent.com/82838972/131711402-438e7c4a-0a49-4277-aff2-d1ceb52d654a.JPG)

5.	Creating a container:``` docker run -p 8501:8501 dipinti123```
We will start the web application in the url : ```localhost:8501```
Output is shown as:
![2021-09-01 (1)](https://user-images.githubusercontent.com/82838972/131712247-37b9d99c-39ca-4899-b152-96f88d43b88c.png)
---
#### Application Functionality

For learning application deployment for Machine Learning projects, I have created is a simple Iris dataset classification where we need to provide sepal length, sepal width, petal length, petal width in cm. The dataset used is imported from the sklearn.dataset. Logistic Regression algorithm is used for prediction. It will predict the plant type and its probability. The Web application is developed in Python3 and Streamlit is used to deploy it in web application. Streamlit is an opensource framework for building the Machine Learning related web application in a faster way.

---
#### Description of the files

--->Base image creation

--->Application.py

--->Dockerfile

--->Readme.md

The 'Base image creation' folder-> consists of the requirements.txt file, Dockerfile which is used to define our base image. This image has been pushed to webserver of dockerhub.

The Application.py is the Iris dataset classification Web Application.
The Dockerfile is our web application Dockerfile
---
#### Steps to run this web application using Docker

1. Clone this repository
2. Install docker and run it
3. Navigate to the folder M20CS020
4. Build docker image with the command ``` docker build . -t dipinti123```
5. Run the image with the command ```docker run -p 8501:8501 dipinti123```
6. In your favourite web brower, access it with the url ```localhost:8501```
---
##### Details of Author
DIPINTI MANANDHAR 
M20CS020















