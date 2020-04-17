"""
Single purpose file to determine the absolute path to the "agents/queries" folder.
"""
import inspect
import os.path as path

def get_queries_path():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    return path.dirname(path.abspath(filename))
