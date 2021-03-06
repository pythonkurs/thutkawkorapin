#!/usr/bin/python
import requests
import sys
import os
import getpass
from dateutil import parser
from pandas import DataFrame

class Repos(object):
    """ Github repositories """


    def __init__(self, owner='pythonkurs'):
        self.owner = owner
        self.__get_login_name()
        self.__get_git_password()

    def __get_git_password(self):
        self.__git_password = getpass.getpass('git password : ')

    def __get_login_name(self):
        sys.stdout.write('git user name : ')
        self.__login_name = sys.stdin.readline().strip()

    def __call_git_api(self, url):
        response = requests.get(url, auth=(self.__login_name, self.__git_password))
        return response.json()

    def __load_repos(self):
        repos = self.__call_git_api("https://api.github.com/orgs/%s/repos" % (self.owner))
        commit_days      = []
        commit_hours     = []
        for repo in repos:
            commits = self.__call_git_api("https://api.github.com/repos/%s/%s/commits" % (self.owner, repo["name"]))
            for commit in commits:
                if "commit" not in commit:
                    continue
                commit_datetime = parser.parse(commit["commit"]["author"]["date"])
                commit_days.append(commit_datetime.strftime("%A"))
                commit_hours.append(commit_datetime.hour)
        self.__repo_info = DataFrame({'day'     : commit_days,
                                      'hour'    : commit_hours,
                                      },
                                     index = commit_days)
        return self.__repo_info


    def load_repos(self):
        return self.__load_repos()

    @property
    def most_common_day_and_hour(self):
        #get the most common day
        day_grouped     = self.__repo_info.groupby("day")
        most_common_day = max(day_grouped.groups.iterkeys(), key=(lambda x: day_grouped.count()["day"][x]))
        #get the most common hour
        hour_grouped     = self.__repo_info.ix[most_common_day].groupby("hour")
        most_common_hour = max(hour_grouped.groups.iterkeys(), key=(lambda x: hour_grouped.count()["hour"][x]))
        return most_common_day, most_common_hour


def assignment4():
    repos = Repos()
    repos.load_repos()
    print repos.most_common_day_and_hour

if __name__=="__main__":
    assignment4()

