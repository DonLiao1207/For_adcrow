## Question:
### Please briefly introduce the version control tool Git on how it work and what it can do. It would be better if you could give several concise scenario.
### Answer:
######  Version control is a way to manage and track any changes you make to your files.    Git is a version control system that developers use all over the world. It helps you track different versions of your code and collaborate with other developers.

---
##### 1.設定config
```
#使用者及mail
git config --global user.name "<Your Name>"
git config --global user.email "<your@gmail.com>"
```
##### 2.新增git repository
```
#cd to work directory and generate .git file
git init
```
##### 3.add file to git space
```
git add file
```
##### 4.commit your change and comment
```
git commit file
git commit -m "your comment"
```
##### 5.github page create your repository
##### 6.add 本地commit檔案到遠端
```
git remote add origin http://token@github.com/<username>/repository
```  
##### 7.push to your master/branch
```
git push -u origin master (-f)
# git push origin master
# git checkout master
# delete repository
git push --delete <repository> <branchname>

git pull

```
##### 8.branch
```
# generate branch
git branch <branchname>
# change to branch
git checkout <branchname>
```
##### 9.get database
```
# clone the database
git clone <url>
git pull <options> <repository> <branch name>
```