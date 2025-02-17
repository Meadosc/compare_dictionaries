"""
Data Fetcher module is responsible for fetching data from various sources.
It provides two classes: DataFetcher and FetcherFactory. DataFetcher is an abstract class
that defines the interface for fetching data. FetcherFactory is a factory class that creates
the appropriate fetcher based on the input type.
"""

from abc import ABC, abstractmethod
import gzip
import json
import os

import boto3

from helper import Constants


"""
DataFetcher class is responsible for fetching data from various sources.
"""
class DataFetcher(ABC):
    @abstractmethod
    def return_generator(self):
        pass


def LocalDataGenerator(DataFetcher):
    def return_generator(self):
        pass


class S3DataGenerator(DataFetcher):
    def __init__(self):
        self.const = Constants()
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(name=self.const.bucket)

    def return_generator(self):
        s3_keys = self._get_filtered_keys()
        for fname in s3_keys:
            obj = self.s3.Object(bucket_name=self.const.bucket, key=fname)
            data = obj.get()['Body'].read() # read raw bytes
            data = gzip.decompress(data) # decompress from gzip
            data = json.loads(data) # read json data
            yield data, fname

    def _get_filtered_keys(self):
        """
        Two filters are run in the next few lines. First for the prefix, which is intended
        to be the folder you're interested in analyzing. The next is a 'start' point that
        is intended to be used if the process failed partway through and you want to jump
        to the middle of the list instead of starting over.
        """
        s3_keys = [obj.key for obj in self.bucket.objects.filter(Prefix=self.const.prefix)]
        start = f"{self.const.prefix}{self.const.prefix_start}"	
        s3_keys = [key for key in s3_keys if key >= start and key.endswith('json.gz')]
        return s3_keys


class TestDataGenerator(DataFetcher):
    def return_generator(self):
        fnames = self._read_fnames()
        for fname in fnames:
            with open(fname) as f:
                data = json.load(f)
            yield data, fname

    def _read_fnames(self):
        path = f"comp_dict/test_data/"
        fnames = os.listdir(path)
        fnames = [path + fname for fname in fnames]
        return fnames



"""
FetcherFactory class is responsible for creating the appropriate fetcher.
"""
class FetcherFactory():
    @classmethod
    def get_fetcher(self, fetcher_type):
        if fetcher_type == "test":
            return TestDataGenerator()
        elif fetcher_type == "s3":
            return S3DataGenerator()
        else:
            raise ValueError("Fetcher type not recognized.")