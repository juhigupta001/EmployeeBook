FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install pymongo tweepy flask
RUN pip install -r requirements.txt
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "python" "run.py" ]
