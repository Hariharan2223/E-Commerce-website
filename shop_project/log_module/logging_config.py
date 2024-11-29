import logging
import json
import logging.config
from decouple import config
from datetime import datetime
import traceback

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.environment = config('ENVIRONMENT', default='dev')
        record.application = config('APPLICATION', default='my_django_project')
        return True

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'environment': getattr(record, 'environment', 'dev'),
            'application': getattr(record, 'application', 'BookCatalog'),
        }

        if record.exc_info:
            log_record['traceback'] = self.format_exception(record.exc_info)

        return json.dumps(log_record)
    
    def format_exception(self, exc_info):
        return ''.join(traceback.format_exception(*exc_info))

def setup_logging():
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'add_context': {
                '()': ContextFilter,
            },
        },
        'formatters': {
            'json': {
                '()': JSONFormatter,
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'json',
                'filters': ['add_context'],
            },
        },
        'loggers': {
            'custom_logger': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }

    logging.config.dictConfig(LOGGING)
    return logging.getLogger('custom_logger')


# import logging
# from django.conf import settings
# from decouple import config
# import json
# import traceback
# from datetime import datetime

# class ContextFilter(logging.Filter):
#     def filter(self, record):
#         record.environment = settings.ENVIRONMENT
#         record.application = settings.APPLICATION
#         if hasattr(record, 'taskName') and record.taskName is None:
#             del record.taskName
#         return True
    
# class JSONFormatter(logging.Formatter):
#     def format(self, record):
#         log_record = {
#             'timestamp': datetime.utcnow().isoformat(),
#             'level': record.levelname,
#             'message': record.getMessage(),
#             'environment': getattr(record, 'environment', 'dev'),
#             'application': getattr(record, 'application', 'BookCatalog'),
#         }

#         if record.exc_info:
#             log_record['traceback'] = self.format_exception(record.exc_info)

#         return json.dumps(log_record)
    
#     def format_exception(self, exc_info):
#         return ''.join(traceback.format_exception(*exc_info))
    
# def setup_logging():
#     settings.ENVIRONMENT = config('ENVIRONMENT', default='dev') 
#     settings.APPLICATION = config('APPLICATION', default='shop_project')

#     handler = logging.StreamHandler()
#     handler.setFormatter(JSONFormatter())
#     handler.addFilter(ContextFilter())

#     custom_logger = logging.getLogger('custom_logger')
#     custom_logger.setLevel(logging.INFO) 
#     custom_logger.addHandler(handler)


#     return custom_logger
