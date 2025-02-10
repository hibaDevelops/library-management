## Library Management Webapp

This is a basic open source Library Management webapp. Its Tech Stack includes MySQL database, Python with Flask framework and Typescript with React framework.

We will be adding more features as we improve this software!

### Project set up:
1. Pull the repo with `git clone`
2. Set up the backend virtual env for python. Navigate to `server` directory and follow these steps!
```
python3 -m venv venv
```
### Windows venv activation
```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```
### Linux and MacOS venv activation
```
source venv/bin/activate
```
3. You should now see a `venv` activated for your directory in command line. It's time to install the dependency libraries for this project. This ensures that these dependencies are installed in your virtual env and not on your local machine!
```
pip3 install requirements.txt
```
5. Create a new `.env` file in root of `server` directory. It should contain the following variable to connect to your MySQL database
```
DATABASE_CONNECTION_URI='mysql+pymysql://root:<password_of_your_local_database>@localhost/<schema_name>’
```
4. Now that you have all set up done, it's now time to run your backend app, run it with the following python command
```
python3 run.py
```
5. Now, lets set up your React typescript frontend. Open a new terminal tab and navigate to `client` directory of the app
6. Install the required dependencies
```
npm install
```
7. Run your frontend project
```
npm run dev
```
8. You should now be able to run your project in a browser with http://localhost:5173/ url