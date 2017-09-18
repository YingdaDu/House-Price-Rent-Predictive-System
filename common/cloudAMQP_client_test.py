from cloudAMQP_client import CloudAMQPClient

# REPLACE URL WITH YOUR OWN
CLOUDAMQP_URL = 'amqp://aznxmzpt:6d7ZMCa7u-xPcokLmLGf9qvQ0PHZj1rL@rhino.rmq.cloudamqp.com/aznxmzpt'
QUEUE_NAME = 'dataFetcherTaskQueue'

# Initialize a client
client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

# Send a message
client.sendDataFetcherTask({'zpid' : '83154148'})


# Receive a message
#client.getDataFetcherTask()
