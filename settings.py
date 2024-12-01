BOT_NAME = 'my_crawler'

SPIDER_MODULES = ['app.spiders']
NEWSPIDER_MODULE = 'app.spiders'
LOG_LEVEL = 'DEBUG'

ROBOTSTXT_OBEY = True

# Encabezados personalizados
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

# Delays
DOWNLOAD_DELAY = 3
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 5
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Timeouts
DOWNLOAD_TIMEOUT = 60

# Manejo de reintentos
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [503, 500, 502, 504, 429]

# Conexiones simultáneas
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Salida
FEED_FORMAT = 'json'
FEED_URI = 'products.json'


