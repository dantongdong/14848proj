# Required docker images
### Main Terminal
main terminal application(source code available in terminal folder): https://hub.docker.com/repository/docker/dantongdong/proj-terminal-image
### Applications
1. Apache Hadoop: https://hub.docker.com/r/sequenceiq/hadoop-docker
2. Apache Spark: https://hub.docker.com/r/sequenceiq/spark
3. Juypter Notebook: https://hub.docker.com/r/jupyter/minimal-notebook
4. SonarQube and SonarScanner:
    <br> 4.1 SonarQube: https://hub.docker.com/_/sonarqube
    <br> 4.2 SonarScanner: https://hub.docker.com/r/sonarsource/sonar-scanner-cli
# Deploy terminal application on Kubernetes Engine(local)
1. pull from the application image -> https://hub.docker.com/repository/docker/dantongdong/proj-terminal-image
2. enable kubernetes cluster in docker
3. run the following command: 
    ```
    kubectl run termnial --rm -i --tty --restart=Never --image=dantongdong/proj-terminal-image:1
    ```
4. *Note:* the above line is used to deploy terminal application on local machine, 
and the terminal application is not connect to any big data application. The deployment result
can be found at terminal_Kubectl.png