from enum import Enum


class ServiceStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    STARTING = "starting"
    STOPPING = "stopping"
    ERROR = "error"