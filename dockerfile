FROM python:3.12
EXPOSE 5000
WORKDIR /app
COPY . .
RUN pip install -r req.txt

CMD ["flask","run","--host","0.0.0.0"]
