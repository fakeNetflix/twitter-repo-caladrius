""" This module contains abstract base classes for the heron metrics clients
"""
import datetime as dt

from abc import abstractmethod

from caladrius.metrics.client import MetricsClient

class HeronMetricsClient(MetricsClient):
    """ Abstract base class for all Heron metric client classes. """

    @abstractmethod
    def __init__(self, config: dict) -> None:
        super().__init__(config)

    @abstractmethod
    def get_service_times(self, topology_id: str, start: dt.datetime,
                          end: dt.datetime, **kwargs):
        """ Gets a time series of the service times of each of the bolt
        instances in the specified topology"""
        pass

    @abstractmethod
    def get_receive_counts(self, topology_id: str, start: dt.datetime,
                           end: dt.datetime, **kwargs):
        """ Gets a time series of the receive counts of each of the bolt
        instances in the specified topology"""
        pass

    @abstractmethod
    def get_emit_counts(self, topology_id: str, start: dt.datetime,
                        end: dt.datetime, **kwargs):
        """ Gets a time series of the emit count of each of the instances in
        the specified topology"""
        pass

    @abstractmethod
    def get_execute_counts(self, topology_id: str, start: dt.datetime,
                           end: dt.datetime, **kwargs):
        """ Gets a time series of the emit count of each of the instances in
        the specified topology"""
        pass
