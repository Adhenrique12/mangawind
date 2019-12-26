# MangaWind  
MangaWind is a command-line utility for downloading manga in pdf and/or as images.


<!-- vscode-markdown-toc -->
* 1. [Features](#Features)
* 2. [Installation](#Installation)
* 3. [Dependencies](#Dependencies)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->  

##  1. <a name='Features'></a>Features  
It let's you download the episodes you specify without having to worry about converting it to pdf and organizing it. It's perfect for those that want to read manga offline on their phones or computers.

##  2. <a name='Installation'></a>2. Installation  
Make sure you have pip install:

Arch  
`sudo pacman -S pip`  

Ubuntu  
`sudo apt install pip3`  

Install mangawind:  

Arch  
`sudo pip install .`  

Ubuntu  
`sudo pip3 install .`  

##  3. <a name='Dependencies'></a>Dependencies  
If you want to use it without using pip you will have to install the dependencies manually.

LXML  
`sudo pip install lxml`  

Pillow  
`sudo pip install Pillow`  

Requests  
`sudo pip install requests`  

BeutifulSoup  
 `sudo pip install beautifulsoup4` 

Shutil  
`sudo pip install shutil`

Progress Bar  
`sudo pip install progress`
