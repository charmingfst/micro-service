# coding=utf-8
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from message.api import MessageService
import socket
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "18255029785@163.com"
authCode = 'chm111222'


class MessageServiceHandler:
    def sendMobileMessage(self, mobile, message):
        print "sendMobileMessage, mobile:" + mobile + ", message:" + message
        return True

    def sendEmailMessage(self, email, message):
        print "sendEmailMessage, email:" + email + ", message:" + message
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj["From"] = sender
        messageObj["To"] = email
        messageObj["Subject"] = Header("慕课网邮件", "utf-8")
        try:
            smtpObj = smtplib.SMTP("smtp.163.com")
            smtpObj.login(sender, authCode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print "send mail success"
            return True
        except smtplib.SMTPException, ex:
            print "send mail failed!"
            print ex.message
            return False


if __name__ == "__main__":
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket(None, "9090", socket_family=socket.AF_INET)
    tfactory = TTransport.TFramedTransportFactory()  # 传输方式
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()  # 传输协议

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "python thrift server start"
    server.serve()
