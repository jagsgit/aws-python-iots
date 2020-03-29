import paho.mqtt.client as mqtt
import ssl

rootca=r'AmazonRootCA1.pem.txt'
certificatefile=r'f1fec06bc3-certificate.pem.crt'
mykeyfile=r'f1fec06bc3-private.pem.key'

clientconnect= mqtt.Client()
clientconnect.tls_set(ca_certs=rootca, certfile=certificatefile, keyfile=mykeyfile, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
clientconnect.connect('a8osgt7o1c657-ats.iot.us-west-2.amazonaws.com', 8883)

def onc(clientconnect,userdata,flags,rc):
    print("Successfully Connected to Amazon RC=",rc)
    clientconnect.subscribe("mytopic/iot")

def onm(c,userdata,msg):
    m=msg.payload.decode()
    print(m.strip())
    if (m.strip() =="Jags"):
        clientconnect.publish("mytopic/iot",payload='message from Jags')
    
clientconnect.on_connect =onc
clientconnect.on_message =onm 
clientconnect.loop_forever()
