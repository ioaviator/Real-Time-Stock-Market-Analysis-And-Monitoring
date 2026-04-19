from kafka import KafkaConsumer
import logging
import json


topic='stock_analysis'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9094'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group',
    consumer_timeout_ms=3000,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
