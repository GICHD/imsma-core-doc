# Using Git and Github for IMSMA Core Development

* [Git](https://git-scm.com/) is a distributed version control system, that lets us manage changes to files and documents used for IMSMA Core. 
* [Github](https://github.com/GICHD/) is a website that makes Git easier to use and provides extra tools like Issue tracking.

By using github we are able to;

* Monitor and track the rollout of IMSMA Core to national authorities and other users. 
* Manage core resources for IMSMA Core, such as scripts, documents and other files.

## Getting Started

### 1. Register on Github

To access resources for IMSMA Core you need an account on Github.

You can register with [Github.com](https://github.com/join). 

If you are a member of the IM division at GICHD, or working on a rollout of IMSMA core you can request access to the [GICHD organisation](https://github.com/GICHD). 

### 2. Install Git and Github Desktop

The easiest way to use Git is to download and install [Github desktop](https://desktop.github.com/), if you are already familiar with Git command line or other options then of course these are compatible with the GICHD repositories.

If you work at the GICHD there are special steps to install and use Github on the local network* so follow this process;

a. Install and configure Git SCM for Windows

   This is the command line version of git and is required to configure Git with our proxy server.  

   1. Download [Git for Windows](https://git-scm.com/download/win)
   2. Install, ensuring you select schannel for HTTPS.     
    ![Screenshot of install selecting sChannel for SSL on Git](git_scm_install_HTTPS.png)

      Accept the other default options or change as you wish, for example to choose a different text editor for commit messages.
      
    3. Disable SSL Certificate Revocation Check 
    
       Open the command prompt and enter the following command:

        `git config --global http.schannelCheckRevoke false`

b. Install Github Desktop.  Download from [desktop.github.com](https://desktop.github.com/) and follow the wizard.

When configuring git it's a good idea to enter the anonymous github e-mail address for your account instead of your real email. This keeps your e-mail address out of the commit history.  You can find this email in your [user settings](https://github.com/settings/emails#toggle_visibility) under 'keep my email address private', for example  _123456+kes1@users.noreply.github.com_.


## Resources for Learning Git

The [Git Book](https://git-scm.com/book/en/v2) is a great place to start for learning about git, though is mostly focussed on the command line application.  The book is available under a free licence, including in e-book formats. 

## How we Use Github for IMSMA Core

For each implementation of IMSMA Core we create a github repository to store resources related to that implementation, and also record progress.

The repository can contain;

* Migration Scripts or SQL Queries
  e.g.  [Tajikistan](https://github.com/GICHD/tnmac-tajikistan/tree/master/migration))
* Web Application or Widget Code
  e.g. [IMSMA Core Demo Data Viewer](https://github.com/GICHD/imsma-core-demo/tree/master/apps/external-data-viewer)
* Scripts for Data Management or Import/Export
  e.g. [UNMAS Syria Jupyter notebooks](https://github.com/GICHD/UNMAS-Syria/blob/e696b13e6dbf936c2df929733e8e7646f2201bbc/formImport/VA%20-%201st%20step%20-%20Check%20Excel%20Report-.ipynb)
* Documentation in [Markdown](https://guides.github.com/features/mastering-markdown/), such as this IMSMA Core Docs repo.

# Issue logging & project planning

Alongside files for code, documentation and SQL queries Github also offers issue recording at the repository level. 

We can use this to record and monitor tasks, or bugs to be worked on. You can see the [issues from all our repositories in one place](https://github.com/issues?q=is%3Aopen+is%3Aissue+org%3Agichd+archived%3Afalse+sort%3Aupdated-desc). 
