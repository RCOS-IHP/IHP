# How to contribute to this repository

As IHP is a very new project, we are not currently accepting contributions from outside the IHP GitHub organization. 

Contributors who are members of IHP should create a branch within the IHP repo. 
Once the feature has been implemented or the bug has been fixed, a pull request should be made to merge the branch into main.
All branches should be related to an issue, and pull requests should generally address/close the issue. 

## Setting up the respotory on your local machine

You will need Git installed. If you do not have Git installed, you can find out how to do it [here](https://github.com/git-guides/install-git).

Once Git is installed, go to the place where you want the project folder to reside. Clone the repository (`git clone https://github.com/RCOS-IHP/IHP.git`).

## Installing the Dependencies

### Frontend

You will need to install [node.js](https://nodejs.org/en/). Once it's installed, go to the project folder and then run these commands:

```bash
cd frontend
npm install 
cd ..
```

### Backend

You will need [Python](https://www.python.org/downloads/) installed. Once it's installed, go to the project folder and then run these commands:

```bash
cd backend
pip install pipenv
pipenv sync
```
