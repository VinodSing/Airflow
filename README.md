# Airflow
Project to demonstrate how Apache Airflow works on GCP.

This Project is based on a frequent use case analysis of fetching the data from a table in BigQuery and creating a new table from it. 

# Tools Used
<li> Google Cloud Composer </li>
<li> BigQuery </li>
<li> Airflow </li>

# Note
Please install required dependencies to run this project

</br>
Before begining with the project, ensure to enable <strong> 'Cloud Composer API' </strong> in your Google Cloud Project

# Prerequisites
<li> Understanding of DAG </li>
<li> Understanding of BigQuery </li>
<li> Understanding of MySQL </li>

# To begin with the project, (Steps to be followed on VSCode)

<li> install Virtual Environment on your local machine (if not already installed) using the command -- pip install virtualenv </li> </br>
<li> Create a folder for your virtual Environment using command -- virtualenv your_folder_name </li> </br>
<li> Activate the Virtual environment using the command -- source your_folder_name/bin/activate </li> </br>
<li> Access Virtual environment folder that was just created in your local editor. </li> </br>
<li> Create a folder named 'dags' in your virtualenvironment folder. This folder will contain your dag which will perform certain actions. </li> </br>
<li> Create a .yml file for Docker & name it as <strong> docker-compose.yml </strong>. This will be used to run your airflow set up. In this file, under web-server, modifiy the path for dags under (volume) to be the path of your dag file in Virtual env. </li> </br>
<li> Create a bqdag.py file (inside dags folder) and mention the tasks that you want the dag to perform. </li> </br>
<li> Mention the below command to run your dag -- </br> 
     <strong>  docker-compose -f your_folder_name/docker-compose.yml up --abort-on-container-exit </strong> </li> </br>
<li> Mention the below command to stop your dag, (if you do not wish to use it) </br>
<strong> docker-compose -f your_folder_name/docker-compose.yml down </strong></li>
