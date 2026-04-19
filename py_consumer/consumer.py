from config import consumer, logger, topic


logger.info(f"Starting Kafka consumer. Waiting for messages from topic {topic}...")

try:
  while True:
    ready_data = consumer.poll(timeout_ms=3000)  # wait 3 seconds

    if not ready_data:
      logger.info(f"Waiting for messages from topic {topic}...")
      continue
    
    # tp==TopicPartition
    for tp_info, messages in ready_data.items():
      for message in messages:
        data = message.value
        logger.info(f"Value (Deserialized): {data}")
finally:
  consumer.close()