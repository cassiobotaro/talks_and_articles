#!/usr/bin/python3


class Explorer:

    def search(self):
        print('Searching...')


class DeepExplorer(Explorer):

    def search(self):
        print('Go deep')
        super().search()

dexp = DeepExplorer()
dexp.search()
