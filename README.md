

Quick Guide to operate:

* Put the Json files holding the binary trees in the data folder under this project
* In the docker-compose file, under the volumes section of the "app" service, Change the "Data folder mount" and the "Log folder mount"
  to the absolute path from your machine to this project + /data or /logs (respectively)
* Activate containers with the "docker-compose up --build" command
* In a different terminal (or after putting the previous process in the background) enter the app container with the 
  "docker exec -it exploriuminterview_app_1 bash" command
* Inside the container run "python /app/application.py"
* You will then be prompt if you want to run the program or exit it
* At any time you can add more files to the shared mounted directory (project_dir/data) and run the program again
* Logs will be written to the project_dir/logs folder 


----------------------------------------------------------------------------------------------------------------------


