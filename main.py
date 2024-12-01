from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from app.spider import GenericSpider
from app.utils.store_config import store_config

def main():
    # Obtiene la configuración del proyecto Scrapy
    settings = get_project_settings()
    
    # Configura la salida en formato JSON
    settings.set('FEEDS', {
        'products.json': {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'indent': 4,
        },
    })

    # Crea el proceso del crawler
    process = CrawlerProcess(settings)
    
    # Recorre las tiendas definidas en `store_config` y añade un spider por cada una
    for store_name, config in store_config.items():
        process.crawl(GenericSpider, store_name=store_name)
    
    # Inicia el proceso de scraping
    process.start()

if __name__ == '__main__':
    main()
