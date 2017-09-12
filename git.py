#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess

class git:
    def __init__(self,debug=False):
        self.debug = debug
        self.location = False
    def _getloc(self):
        if self.location:
            return self.location
        else:
            return os.getcwd()
    def _passset(self):
        if hasattr(self,'password'):
            return True
        else:
            return False
    def _userset(self):
        if hasattr(self,'username'):
            return True
        else:
            return False
    def _quote(self,string):
        return '\'' + string + '\''
    def _geturl(self):
        location = self._getloc()
        currloc = os.getcwd()
        os.chdir(location)
        return [subprocess.check_output(['git','config',
        '--get','remote.origin.url']),os.chdir(currloc)][0]
    def init(self,location=False,bare=False,args=''):
        '''This command creates an empty Git repository - basically a .git
        directory with subdirectories for objects, refs/heads, refs/tags, and
        template files. An initial HEAD file that references the HEAD of the
        master branch is also created.'''
        if not location:
            location = self._getloc()
        cmd = 'git init ' if self.debug else 'git init -q '
        cmd = cmd + args + ' ' if args != '' else cmd
        cmd = cmd + '--bare ' + location if bare else cmd + location
        os.system(cmd)
    def open(self,location=False):
        '''This command is used to select the dir that contains the local
        repository'''
        if not location:
            location = self._getloc()
        self.location = location
    def clone(self,url,location=False,args=''):
        '''Clones a repository into a newly created directory, creates
        remote-tracking branches for each branch in the cloned repository
        , and creates and checks out an initial branch that is forked
        from the cloned repository’s currently active branch.'''
        if not location:
            location = self._getloc()
        cmd = 'git clone ' if self.debug else 'git clone -q '
        cmd = cmd + args + ' ' if args != '' else cmd
        cmd = ' '.join([cmd,url,location])
        os.system(cmd)
    def add(self,location=False,args=''):
        '''This command updates the index using the current content found in
        the working tree, to prepare the content staged for the next commit.
        It typically adds the current content of existing paths as a whole,
        but with some options it can also be used to add content with only part
        of the changes made to the working tree files applied, or remove paths
        that do not exist in the working tree anymore.'''
        if not location:
            location = self._getloc()
        currloc = os.getcwd()
        os.chdir(self.location)
        if args != '':
            cmd = 'git add '+args
        else:
            cmd = 'git add -A '
        os.system(cmd)
        os.chdir(currloc)
    def commit(self,msg,location=False,args=''):
        '''Stores the current contents of the index in a new commit along
        with a log message from the user describing the changes'''
        if not location:
            location = self._getloc()
        currloc = os.getcwd()
        os.chdir(self.location)
        cmd = 'git commit -m \''+msg+'\' '+args
        os.system(cmd)
        os.chdir(currloc)
    def user(self,username,password=None,warn=True):
        '''Sets the username and password for the current session'''
        self.username = username
        if password:
            if warn:
                print('Warning: Never enter your password in a public computer.\n'
                '         Use Personal access tokens when possible.\n'
                '         https://github.com/blog/1509-personal-api-tokens')
            self.password = password
    def push(self,url=False,bname='master',location=False,args=''):
        '''Updates remote refs using local refs, while sending objects
        necessary to complete the given refs.'''
        if not location:
            location = self._getloc()
        if not url:
            url = self._geturl()
        currloc = os.getcwd()
        os.chdir(location)
        url = [url.split('://')[0]+'://',url.split('://')[-1].split('@')[0],
        url.split('://')[1].split('@')[-1]]
        url[1] = [] if url[1] == url[2] else url[1].split(':')
        if len(url[1]) == 2:
            url = url[0] + url[1][0] + ':' + url[1][1] + '@' + url[2]
        elif len(url[1]) == 1:
            url = url[0] + url[1][0] + '@' + url[2]
        elif self._userset() and self._passset():
            urlkey = self.username + ':' +self.password + '@'
            url = ''.join([url[0],urlkey,url[2]])
        elif self._userset():
            urlkey = self.username + '@'
            url = ''.join([url[0],urlkey,url[2]])
        else:
            pass
        cmd = 'git push '+args+' '
        cmd = ' '.join([cmd,self._quote(url),bname])
        print cmd
        os.system(cmd)
        os.chdir(currloc)
    def status(self,location=False,getoutput=False,args=''):
        '''Displays paths that have differences between the index file and the
        current HEAD commit, paths that have differences between the working
        tree and the index file, and paths in the working tree that are not
        tracked by Git (and are not ignored by gitignore). The first are
        what you would commit by running git commit; the second and third
        are what you could commit by running git add before running git commit.'''
        if not location:
            location = self._getloc()
        currloc = os.getcwd()
        os.chdir(location)
        if getoutput:
            cmd = ['git','status']
            if args != '':
                args = ['-'+item for item in args.split(' -')]
                cmd.extend(args)
            return [subprocess.check_output(cmd),
            os.chdir(currloc)][0]
        else:
            os.system('git status '+args)
            os.chdir(currloc)
    def cmd(self,cmdline,location=False):
        '''Runs a git command'''
        if not location:
            location = self._getloc()
        currloc = os.getcwd()
        os.chdir(location)
        os.system(cmdline)
        os.chdir(currloc)
    def pull(self,url=False,location=False,args=''):
        '''Incorporates changes from a remote repository into the current
        branch. In its default mode, git pull is shorthand for git fetch
        followed by git merge FETCH_HEAD'''
        if not location:
            location = self._getloc()
        if not url:
            url = self._geturl()
        currloc = os.getcwd()
        os.chdir(location)
        os.system('git pull ' +args + ' ' + url)
        os.chdir(currloc)
