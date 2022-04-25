FROM python
EXPOSE 5000
WORKDIR /app
RUN pip install boto3 flask awscli
COPY . .
RUN chmod -R 755 config.sh
CMD ["./config.sh"]