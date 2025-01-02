from abc import ABC, abstractmethod
import logging

class ReflexLogger(ABC):
    
    def __init__(self, next : 'ReflexLogger' = None):
        self.next = next
    
    def info(self, message):
        self._info(message)
        if self.next:
            self.next.info(message)
    
    def error(self, message):
        self._error(message)
        if self.next:
            self.next.error(message)
    
    def debug(self, message):
        self._debug(message)
        if self.next:
            self.next.debug(message)
    
    def warning(self, message):
        self._warning(message)
        if self.next:
            self.next.warning(message)
    
    def critical(self, message):
        self._critical(message)
        if self.next:
            self.next.critical(message)

    def set_next(self, next : 'ReflexLogger'):
        self.next = next
    
    @abstractmethod
    def _critical(self, message):
        pass
    
    @abstractmethod
    def _warning(self, message):
        pass
    
    @abstractmethod
    def _debug(self, message):
        pass
    
    @abstractmethod
    def _error(self, message):
        pass
    
    @abstractmethod
    def _info(self, message):
        pass

class ConsoleLogger(ReflexLogger):
    
    def __init__(self, next = None):
        super().__init__(next)
        self.logger = logging.getLogger(__name__)
        self.handler = logging.StreamHandler()
        self.logger.setLevel(logging.DEBUG)
        self.handler.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            self.logger.addHandler(self.handler)
    
    def _critical(self, message):
        self.logger.critical(message)
    
    def _warning(self, message):
        self.logger.warning(message)
    
    def _debug(self, message):
        self.logger.debug(message)
    
    def _error(self, message):
        self.logger.error(message)
    
    def _info(self, message):
        self.logger.info(message)
    
class FileLogger(ReflexLogger):
    
    def __init__(self, next = None, file_name = 'reflex.log'):
        super().__init__(next)
        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler(file_name)
        self.logger.setLevel(logging.DEBUG)
        self.handler.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            self.logger.addHandler(self.handler)
    
    def _critical(self, message):
        self.logger.critical(message)
    
    def _warning(self, message):
        self.logger.warning(message)
    
    def _debug(self, message):
        self.logger.debug(message)
    
    def _error(self, message):
        self.logger.error(message)
    
    def _info(self, message):
        self.logger.info(message)