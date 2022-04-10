# college-apps

![Notion](https://img.shields.io/badge/-Notion-333333?style=flat&logo=notion&logoColor=F1F1F1)
![Figma](https://img.shields.io/badge/-Figma-333333?style=flat&logo=figma&logoColor=F1F1F1)
![GitHub](https://img.shields.io/badge/-Github-333333?style=flat&logo=github&logoColor=F1F1F1)
![CockroachDB](https://img.shields.io/badge/-CockroachDB-333333?style=flat&logo=cockroach&logoColor=F1F1F1)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python&logoColor=F1F1F1)
![Flask](https://img.shields.io/badge/-Flask-333333?style=flat&logo=flask&logoColor=F1F1F1)
![Glitch](https://img.shields.io/badge/-Glitch-333333?style=flat&logo=glitch&logoColor=F1F1F1)


## Introduction and Inspiration

When we think about graduate school admissions, here are some things that come to mind: grades, test scores, statement of purpose, letter of recommendations, deadlines, and fees. Keeping track of all this during the application process can be pretty overwhelming, especially when you're applying to multiple universities. 
As aspiring students, we find it hard to hunt for information online. This motivated us to build a solution! With our app, we hope to make a part of this challenging process simpler and help you get closer to your dream admit. 

All you have to do is sync your Notion workspace, enter some details about the course you're looking at, and we'll provide you with all the relevant and important information right in your Notion.

## What It Does

Head over to the website and sign up as a new user. This will prompt you to sign up with your email and create a password. Please note, we don't store your password. But more about this later. Once you're in, you will be able to access the dashboard. Here you get to sync your Notion workspace and grant access to our Notion integration. Now, you can enter some details about the program you're considering applying to. We require the link to the program's webpage. Once this has been added, add some more information like - Course name, Track (if any), and whether you're an Internation or Domestic student. This will help us provide accurate and relevant information for you. We don't store any of this information, we only use it to parse the website at our end. When you hit "Add to Notion" you should see relevant information related to this program created in a page in a database in your Notion workspace!

## Tech Stack + Tools Used

1. Project Management + Ideation - Notion, Figma (FigJam)
2. Design - Figma 
3. Project Development - GitHub
4. Database - Cockroach DB
5. Languages and Frameworks - Python, Flask, Beautiful Soup, notion-py, psycopg2
6. Web Hosting - Glitch
 

## How We Made It

Since we were working remotely and only had a day to complete this project, we were big on project mangement and ensured there were no communication gaps. We made use of a Kanban board on Notion to track our progress and inform each other of blockers. 

We ideated on a FigJam board in Figma and understood concepts together on Microsoft Whiteboard.

Once we had a clear idea of what each of us will be doing, we started coding! We made use of GitHub as our development platform. Since our project is modular, we created different branches (cockroach-scripts, bs-scripts, etc) containing scripts of each module. In the end, we combined everything in the main branch by opening pull requests. We made sure our commit messages were descriptive (and had an emoji at the end - no idea why we did that!).

Each branch contains a descriptive README so you can read more about each individual aspect of our project. Click to understand more about:

1. [Database + authentication](https://github.com/gaurigupta31/college-apps/tree/cockroach-scripts#cockroach-scripts--authentication-process-cockroach-key): Instructions to setup the database yourself (we use Cockroach DB), how we use of Secure Remote Password (SRP), an implementation of Zero Knowledge Proof (ZPK) to securely register and authenticate users in our DB without storing their password.
2. [Web Scraping](): How we use Beautiful Soup to parse the data from websites and filter out the relevant information.
